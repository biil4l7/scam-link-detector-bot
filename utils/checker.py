import re
import socket
import base64
import os
import requests
from urllib.parse import urlparse

# ── API Keys (loaded from .env via bot.py's load_dotenv) ─────────────────────
VIRUSTOTAL_API_KEY   = os.getenv("VIRUSTOTAL_API_KEY", "")
SAFE_BROWSING_API_KEY = os.getenv("SAFE_BROWSING_API_KEY", "")

# ── Known scam / phishing keyword patterns ───────────────────────────────────
SCAM_KEYWORDS = [
    "free-money", "freemoney", "free_money",
    "win-prize", "winprize", "win_prize",
    "claim-reward", "claimreward",
    "verify-account", "verifyaccount",
    "suspended", "urgent-login",
    "confirm-payment", "confirmepayment",
    "lucky-winner", "luckywinner",
    "click-here-now", "limited-offer",
    "100%-free", "earn-fast", "earnfast",
    "update-your", "secure-login", "securelogin",
    "account-locked", "accountlocked",
]

# ── Trusted domains whitelist ─────────────────────────────────────────────────
TRUSTED_DOMAINS = {
    "google.com", "youtube.com", "facebook.com", "instagram.com",
    "twitter.com", "x.com", "telegram.org", "t.me", "github.com",
    "wikipedia.org", "amazon.com", "apple.com", "microsoft.com",
    "bbc.com", "reuters.com", "rudaw.net", "kurdistan24.net",
    "linkedin.com", "reddit.com", "whatsapp.com", "tiktok.com",
}

# ── Known dangerous TLDs ─────────────────────────────────────────────────────
SUSPICIOUS_TLDS = [
    ".xyz", ".tk", ".ml", ".ga", ".cf", ".gq",
    ".pw", ".top", ".click", ".link", ".icu", ".buzz",
]

# ── URL shorteners ────────────────────────────────────────────────────────────
SHORTENERS = {
    "bit.ly", "tinyurl.com", "t.co", "ow.ly", "buff.ly",
    "cutt.ly", "rb.gy", "is.gd", "tiny.cc", "shorte.st",
    "adf.ly", "bc.vc",
}


def check_link(url: str) -> dict:
    """
    Analyses a URL and returns a risk report dict:
    {
      score: int (0=safe, 100=very dangerous),
      risk: "safe" | "medium" | "danger",
      flags: [list of (code: str, params: dict) tuples],
      domain: str
    }
    """
    if not url.startswith("http"):
        url = "https://" + url

    flags = []
    score = 0

    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace("www.", "")
        full_path = (parsed.netloc + parsed.path + parsed.query).lower()
    except Exception:
        return {"score": 80, "risk": "danger", "flags": [("parse_error", {})], "domain": url}

    # ── 1. Trusted domain → early exit ───────────────────────────────────────
    root = _root_domain(domain)
    if root in TRUSTED_DOMAINS:
        # Extra safety: make sure the trusted part is the REAL root,
        # not a subdomain trick like "google.com.evil.xyz"
        if domain == root or domain.endswith("." + root):
            return {"score": 5, "risk": "safe", "flags": [], "domain": domain}

    # ── 2. Google Safe Browsing ───────────────────────────────────────────────
    if SAFE_BROWSING_API_KEY:
        gsb_hit = _check_google_safe_browsing(url)
        if gsb_hit:
            flags.append(("gsb_threat", {"type": gsb_hit}))
            score += 75          # Near-certain danger

    # ── 3. VirusTotal ─────────────────────────────────────────────────────────
    if VIRUSTOTAL_API_KEY and score < 75:   # Skip if GSB already flagged
        vt_result = _check_virustotal(url)
        if vt_result["malicious"] > 0:
            flags.append(("virustotal", {
                "malicious": vt_result["malicious"],
                "total":     vt_result["total"],
            }))
            # Scale: 1 engine = +20, 3+ = +50, 10+ = +70
            if vt_result["malicious"] >= 10:
                score += 70
            elif vt_result["malicious"] >= 3:
                score += 50
            else:
                score += 20

    # ── 4. Suspicious TLD ─────────────────────────────────────────────────────
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            flags.append(("suspicious_tld", {"tld": tld}))
            score += 30
            break

    # ── 5. Scam keywords in URL ───────────────────────────────────────────────
    for kw in SCAM_KEYWORDS:
        if kw in full_path:
            flags.append(("scam_keyword", {"keyword": kw}))
            score += 20
            break  # Only count once

    # ── 6. Very long URL ──────────────────────────────────────────────────────
    if len(url) > 200:
        flags.append(("long_url", {}))
        score += 15

    # ── 7. Too many subdomains ────────────────────────────────────────────────
    parts = domain.split(".")
    if len(parts) > 4:
        flags.append(("too_many_subdomains", {}))
        score += 20

    # ── 8. IP address instead of domain ──────────────────────────────────────
    if _is_ip(domain):
        flags.append(("ip_address", {}))
        score += 35

    # ── 9. HTTP (not HTTPS) ───────────────────────────────────────────────────
    if parsed.scheme == "http":
        flags.append(("no_https", {}))
        score += 15

    # ── 10. URL shortener ─────────────────────────────────────────────────────
    if root in SHORTENERS:
        flags.append(("url_shortener", {}))
        score += 25

    # ── 11. Live HTTP check ───────────────────────────────────────────────────
    try:
        resp = requests.get(
            url, timeout=6, allow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        final_domain = urlparse(resp.url).netloc.lower().replace("www.", "")
        if final_domain != domain:
            flags.append(("redirect_diff_domain", {"domain": final_domain}))
            score += 20
        if resp.status_code in (403, 404, 500, 502, 503):
            flags.append(("server_error", {"code": resp.status_code}))
            score += 10
    except requests.exceptions.SSLError:
        flags.append(("ssl_error", {}))
        score += 30
    except requests.exceptions.ConnectionError:
        flags.append(("connection_error", {}))
        score += 25
    except Exception:
        pass

    score = min(score, 100)
    risk = "safe" if score <= 25 else ("medium" if score <= 55 else "danger")
    return {"score": score, "risk": risk, "flags": flags, "domain": domain}


# ── Google Safe Browsing ──────────────────────────────────────────────────────

def _check_google_safe_browsing(url: str) -> str | None:
    """
    Returns a threat-type string if flagged, else None.
    Docs: https://developers.google.com/safe-browsing/v4/lookup-api
    """
    endpoint = (
        "https://safebrowsing.googleapis.com/v4/threatMatches:find"
        f"?key={SAFE_BROWSING_API_KEY}"
    )
    payload = {
        "client": {"clientId": "scam-link-bot", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": [
                "MALWARE", "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION",
            ],
            "platformTypes":   ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries":    [{"url": url}],
        },
    }
    try:
        r = requests.post(endpoint, json=payload, timeout=5)
        data = r.json()
        matches = data.get("matches", [])
        if matches:
            return matches[0].get("threatType", "THREAT")
    except Exception:
        pass
    return None


# ── VirusTotal ────────────────────────────────────────────────────────────────

def _check_virustotal(url: str) -> dict:
    """
    Returns {"malicious": int, "total": int}.
    Uses the VT v3 URL scan endpoint (free tier: 4 req/min).
    Docs: https://developers.virustotal.com/reference/scan-url
    """
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    url_id  = base64.urlsafe_b64encode(url.encode()).rstrip(b"=").decode()

    try:
        # 1. Try to get an existing report first (avoids quota use)
        r = requests.get(
            f"https://www.virustotal.com/api/v3/urls/{url_id}",
            headers=headers, timeout=8,
        )
        if r.status_code == 200:
            stats = (
                r.json()
                 .get("data", {})
                 .get("attributes", {})
                 .get("last_analysis_stats", {})
            )
            return {
                "malicious": stats.get("malicious", 0),
                "total":     sum(stats.values()),
            }

        # 2. No existing report — submit for scanning
        r2 = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers, data={"url": url}, timeout=8,
        )
        if r2.status_code == 200:
            # Submission queued — we won't wait for results to avoid blocking
            # the user; return 0 and the async result can be checked later.
            return {"malicious": 0, "total": 0}

    except Exception:
        pass

    return {"malicious": 0, "total": 0}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _root_domain(domain: str) -> str:
    parts = domain.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else domain


def _is_ip(domain: str) -> bool:
    try:
        socket.inet_aton(domain.split(":")[0])
        return True
    except Exception:
        return False