# 🛡️ Scam Link Detector Bot

Telegram bot that checks if a link is safe or dangerous.
Supports 3 languages: Kurdish (Sorani), Arabic, English.

---

## 📁 Folder Structure

```
ScamLinkBot/
├── bot.py              ← Main bot file
├── .env                ← Your secret token (never share this!)
├── .env.example        ← Template for .env
├── .gitignore          ← Protects .env from being uploaded
├── requirements.txt    ← Python packages
└── utils/
    ├── __init__.py
    ├── checker.py      ← Link analysis engine
    └── languages.py    ← All 3 language texts
```

---

## ⚙️ Setup

### 1. Create a virtual environment (recommended)
```bash
py -3.13 -m venv venv
.\venv\Scripts\activate
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Create your .env file
Copy `.env.example` and rename it to `.env`:
```bash
copy .env.example .env
```
Then open `.env` and paste your token:
```
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ
```

### 4. Run the bot
```bash
python bot.py
```

---

## 🔒 Important — Keep .env Secret!

- ✅ `.env` is in `.gitignore` — it will NOT be uploaded to GitHub
- ❌ Never share your `.env` file with anyone
- ❌ Never paste your token in public chats

---

## 🤖 How the Bot Works

1. User sends /start
2. Bot asks: choose language (Kurdish / Arabic / English)
3. User picks a language
4. Bot asks for a link
5. User sends any link
6. Bot returns a full report:
   - 🟢 Safe
   - 🟡 Medium Risk
   - 🔴 Dangerous

---

## 🔍 What the Checker Analyses

| Check | Description |
|-------|-------------|
| Trusted domains | Google, Facebook, YouTube → always safe |
| Suspicious TLDs | .xyz .tk .ml .ga → risky |
| Scam keywords | "free-money", "win-prize" in URL |
| Long URLs | Over 200 chars → phishing sign |
| Too many subdomains | a.b.c.d.com → suspicious |
| IP address URLs | 192.168.1.1/login → very suspicious |
| No HTTPS | http:// only → not encrypted |
| URL shorteners | bit.ly, tinyurl → hides real destination |
| Live redirect check | Checks if it redirects to another domain |
| SSL errors | Fake certificate → dangerous |

---

## 💡 Risk Score

| Score | Risk Level |
|-------|------------|
| 0–25  | 🟢 Safe |
| 26–55 | 🟡 Medium |
| 56–100| 🔴 Dangerous |

---

## 🚀 Run 24/7 for Free (Railway.app)

1. Upload your files to a **private** GitHub repo
2. Go to railway.app and connect your repo
3. Add environment variable: `BOT_TOKEN` = your token
4. Set start command: `python bot.py`
5. Done — bot runs 24/7!

> ⚠️ On Railway, add BOT_TOKEN in their dashboard settings — do NOT upload your .env file.
