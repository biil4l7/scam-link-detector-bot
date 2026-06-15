TEXTS = {
    "ku": {
        "welcome": (
            "✅ *زمانی کوردی هەڵبژێردرا*\n\n"
            "🛡️ *بەخێربێیت بۆ Scam Link Detector*\n\n"
            "ئەم بۆتە بە چەند چرکەیەک هەر لینکێک شیکاری دەکات و پێت دەڵێت "
            "ئایا پارێزراوە یان مەترسیداری تێدایە — پێش ئەوەی کلیکی لەسەری بکەیت.\n\n"
            "📎 ئێستا لینکەکەت بنێرە بۆ دەستپێکردن."
        ),
        "send_link":     "📎 لینکێکی دیکە بنێرە بۆ شیکارکردن.",
        "not_a_link":    "⚠️ ئەمە لینکێکی دروست نییە. تکایە لینکێک بنێرە کە بە `http://` یان `https://` دەستپێ دەکات.",
        "checking":      "🔍 *لینکەکەت شیکاری دەکرێت...* تەنها چەند چرکەیەک پێویستە.",
        "status_safe":   "ئەم لینکە پارێزراو دیارە",
        "status_medium": "ئەم لینکە گومانی تێدایە — وریابە",
        "status_danger": "ئەم لینکە مەترسیداری بەرزە — کلیکی لەسەری مەکە",
        "risk_score":    "خاڵی مەترسی",
        "findings":      "دۆزینەوەکان",
        "no_flags":      "هیچ نیشانەیەکی مەترسیدار نەدۆزرایەوە",
        "advice": {
            "safe":   "✅ هیچ نیشانەی گرنگی مەترسیدار نەدۆزرایەوە. سەرەڕای ئەوە، هەمیشە لە ئینتەرنێتدا وریابە.",
            "medium": "⚠️ ئەم لینکە چەند نیشانەیەکی گومانلێکراوی هەیە. باشترە کلیکی لەسەری نەکەیت ئەگەر دڵنیا نیت لە سەرچاوەکەی.",
            "danger": "🚨 ئەم لینکە مەترسیداری زۆر بەرزە. کلیکی لەسەری مەکە و لەگەڵ کەسانی تریشدا بەشی مەکە.",
        },
        "btn_check_another": "🔄 لینکێکی دیکە بپشکنە",
        "btn_report":        "🚨 ڕاپۆرتکردنی فێڵ",
        "report_thanks":     "✅ سوپاس بۆ ڕاپۆرتەکەت. ئەم زانیارییە یارمەتیمان دەدات کەسانی تر باشتر بپارێزین.",
        "help_text": (
            "🛡️ *Scam Link Detector — یارمەتی*\n\n"
            "*فەرمانەکان*\n"
            "• /start — دەستپێکردنی دووبارە یان گۆڕینی زمان\n"
            "• /help — پیشاندانی ئەم پەیامە\n\n"
            "*چۆنیەتی کارکردن*\n"
            "تەنها هەر لینکێکی گومانلێکراو بنێرە، ئەم بۆتە بە دەیان پشکنین "
            "(دۆمەینی پارێزراو، کلمەسازی فێڵ، ئاراستەکردنی نادیار، بپارچەکانی SSL، هتد) "
            "شیکاری دەکات و ئاستی مەترسی دیاری دەکات.\n\n"
            "*ئاستەکانی مەترسی*\n"
            "🟢 پارێزراو — 0 تا 25\n"
            "🟡 گومانی تێدایە — 26 تا 55\n"
            "🔴 مەترسیداری بەرز — 56 تا 100\n\n"
            "هەر لینکێکی گومانلێکراوت پێگەیشت یان لە ئینتەرنێتدا بینیت، بینێرە بۆ پشکنین!"
        ),
        "use_start":    "تکایە فەرمانی /start بنووسە بۆ دەستپێکردن.",
        "rate_limited": "⏳ زۆر زیاد داواکاریت کرد. تکایە {seconds} چرکە چاوەڕوان بە.",
    },

    "ar": {
        "welcome": (
            "✅ *تم اختيار اللغة العربية*\n\n"
            "🛡️ *أهلاً بك في Scam Link Detector*\n\n"
            "يقوم هذا البوت بتحليل أي رابط في ثوانٍ معدودة، ويخبرك إن كان "
            "آمناً للزيارة أم يحتوي على علامات احتيال أو تصيّد إلكتروني — قبل أن تفتحه.\n\n"
            "📎 أرسل لي رابطاً الآن للبدء."
        ),
        "send_link":     "📎 أرسل رابطاً آخر لتحليله.",
        "not_a_link":    "⚠️ هذا لا يبدو رابطاً صالحاً. أرجو إرسال رابط يبدأ بـ `http://` أو `https://`.",
        "checking":      "🔍 *جاري تحليل الرابط...* لحظات فقط.",
        "status_safe":   "هذا الرابط يبدو آمناً",
        "status_medium": "هذا الرابط مشبوه — كن حذراً",
        "status_danger": "هذا الرابط خطير جداً — لا تفتحه",
        "risk_score":    "درجة الخطورة",
        "findings":      "النتائج",
        "no_flags":      "لم يتم رصد أي مؤشرات خطر",
        "advice": {
            "safe":   "✅ لم نعثر على أي مؤشرات خطر واضحة. مع ذلك، يُنصح دائماً بالحذر عند تصفح الإنترنت.",
            "medium": "⚠️ يحتوي هذا الرابط على بعض علامات الخطر. يُفضَّل تجنبه إلا إذا كنت متأكداً من مصدره.",
            "danger": "🚨 هذا الرابط خطير للغاية. لا تفتحه، ولا ترسله إلى أي شخص آخر.",
        },
        "btn_check_another": "🔄 فحص رابط آخر",
        "btn_report":        "🚨 الإبلاغ عن احتيال",
        "report_thanks":     "✅ شكراً لك، تم استلام بلاغك. مساهمتك تساعد في حماية الآخرين.",
        "help_text": (
            "🛡️ *Scam Link Detector — المساعدة*\n\n"
            "*الأوامر*\n"
            "• /start — البدء من جديد أو تغيير اللغة\n"
            "• /help — عرض هذه الرسالة\n\n"
            "*كيف يعمل البوت؟*\n"
            "أرسل أي رابط تشك فيه، وسيقوم البوت بفحصه عبر عشرات المعايير "
            "(النطاقات الموثوقة، الكلمات الاحتيالية، إعادة التوجيه المشبوهة، "
            "أخطاء شهادات SSL، وغيرها) لتحديد مستوى الخطورة.\n\n"
            "*مستويات الخطورة*\n"
            "🟢 آمن — 0 إلى 25\n"
            "🟡 مشبوه — 26 إلى 55\n"
            "🔴 خطر مرتفع — 56 إلى 100\n\n"
            "أرسل أي رابط مشبوه تستقبله أو تجده على الإنترنت!"
        ),
        "use_start":    "أرجو إرسال /start للبدء.",
        "rate_limited": "⏳ لقد أرسلت طلبات كثيرة. انتظر {seconds} ثانية.",
    },

    "en": {
        "welcome": (
            "✅ *English selected*\n\n"
            "🛡️ *Welcome to Scam Link Detector*\n\n"
            "This bot analyzes any link in seconds and tells you whether it's "
            "safe to visit or shows signs of phishing, malware, or scams — "
            "before you click.\n\n"
            "📎 Send me a link to get started."
        ),
        "send_link":     "📎 Send another link to analyze.",
        "not_a_link":    "⚠️ That doesn't look like a valid link. Please send a URL starting with `http://` or `https://`.",
        "checking":      "🔍 *Analyzing your link...* This will only take a moment.",
        "status_safe":   "This link appears to be Safe",
        "status_medium": "This link is Suspicious — proceed with caution",
        "status_danger": "This link is DANGEROUS — do not open it",
        "risk_score":    "Risk Score",
        "findings":      "Findings",
        "no_flags":      "No suspicious indicators detected",
        "advice": {
            "safe":   "✅ No major red flags were found. As always, stay cautious online.",
            "medium": "⚠️ This link shows some warning signs. We recommend avoiding it unless you're certain of its source.",
            "danger": "🚨 This link is highly dangerous. Do not open it, and do not share it with others.",
        },
        "btn_check_another": "🔄 Check another link",
        "btn_report":        "🚨 Report as scam",
        "report_thanks":     "✅ Thank you — your report has been recorded. You're helping keep others safe.",
        "help_text": (
            "🛡️ *Scam Link Detector — Help*\n\n"
            "*Commands*\n"
            "• /start — Restart or change language\n"
            "• /help — Show this message\n\n"
            "*How it works*\n"
            "Send me any link you're unsure about. I'll run it through dozens "
            "of checks — trusted domains, scam keywords, suspicious redirects, "
            "SSL errors, and more — and give you a clear risk rating.\n\n"
            "*Risk levels*\n"
            "🟢 Safe — 0 to 25\n"
            "🟡 Suspicious — 26 to 55\n"
            "🔴 High Risk — 56 to 100\n\n"
            "Send any suspicious link you receive or come across online!"
        ),
        "use_start":    "Please type /start to begin.",
        "rate_limited": "⏳ Too many requests. Please wait {seconds} seconds before checking another link.",
    },
}


def get_text(lang: str, key: str) -> str:
    return TEXTS.get(lang, TEXTS["en"]).get(key, "")


# Translatable templates for the technical findings returned by utils.checker
FLAGS = {
    "ku": {
        "suspicious_tld":     "پاشگری دۆمەینی گومانلێکراو ({tld})",
        "scam_keyword":       "وشەی گومانلێکراو لە لینکدا: '{keyword}'",
        "long_url":           "لینکێکی زۆر درێژ (نیشانەی باوی فێڵ)",
        "too_many_subdomains": "زیادبوونی ژێردۆمەینەکان (تەکنیکی فێڵ)",
        "ip_address":         "لینکەکە IP بەکاردەهێنێت لەجیاتی دۆمەین",
        "no_https":           "بەبێ HTTPS — پەیوەندییەکە کۆدنەکراوە",
        "url_shortener":      "کەمکەرەوەی لینک دۆزرایەوە — ئاکامی ڕاستەقینە شاراوەیە",
        "redirect_diff_domain": "ئاراستەکردن بۆ ماڵپەڕێکی جیاواز: {domain}",
        "server_error":       "سێرڤەرەکە هەڵەی کۆد {code} گەڕاندەوە",
        "ssl_error":          "هەڵەی بڕوانامەی SSL — ماڵپەڕەکە لەوانەیە درۆبوو بێت",
        "connection_error":   "نەتوانرا پەیوەندی بە ماڵپەڕەکەوە بکرێت",
        "parse_error":        "نەتوانرا لینکەکە شیکاری بکرێت",
        "gsb_threat":         "⛔ گووگڵ ئەم لینکە وەک مەترسیدار({type}) نیشانکردووە",
        "virustotal":         "🦠 VirusTotal: {malicious} لە {total} ئامرازی ئەمنیەت مەترسی دۆزیەوە",
    },
    "ar": {
        "suspicious_tld":     "امتداد نطاق مشبوه ({tld})",
        "scam_keyword":       "كلمة مشبوهة في الرابط: '{keyword}'",
        "long_url":           "رابط طويل بشكل غير معتاد (علامة تصيّد شائعة)",
        "too_many_subdomains": "عدد كبير من النطاقات الفرعية (أسلوب تصيّد)",
        "ip_address":         "الرابط يستخدم عنوان IP بدلاً من اسم نطاق",
        "no_https":           "بدون HTTPS — الاتصال غير مشفّر",
        "url_shortener":      "تم رصد رابط مُختصر — الوجهة الحقيقية مخفية",
        "redirect_diff_domain": "يُعيد التوجيه إلى موقع مختلف: {domain}",
        "server_error":       "السيرفر أعاد رمز خطأ {code}",
        "ssl_error":          "خطأ في شهادة SSL — قد يكون الموقع مزيفاً",
        "connection_error":   "تعذّر الاتصال بالموقع",
        "parse_error":        "تعذّر تحليل الرابط",
        "gsb_threat":         "⛔ Google صنّف هذا الرابط كخطر ({type})",
        "virustotal":         "🦠 VirusTotal: {malicious} من {total} محرك أمني اكتشف خطراً",
    },
    "en": {
        "suspicious_tld":     "Suspicious domain extension ({tld})",
        "scam_keyword":       "Suspicious keyword in URL: '{keyword}'",
        "long_url":           "Unusually long URL (common in phishing)",
        "too_many_subdomains": "Too many subdomains (phishing trick)",
        "ip_address":         "URL uses an IP address instead of a domain name",
        "no_https":           "No HTTPS — connection is not encrypted",
        "url_shortener":      "URL shortener detected — real destination is hidden",
        "redirect_diff_domain": "Redirects to a different site: {domain}",
        "server_error":       "Server returned error code {code}",
        "ssl_error":          "SSL certificate error — site may be fake",
        "connection_error":   "Could not connect to the site",
        "parse_error":        "Could not parse the URL",
        "gsb_threat":         "⛔ Google flagged this link as dangerous ({type})",
        "virustotal":         "🦠 VirusTotal: {malicious} of {total} security engines flagged this link",
    },
}


def format_flag(lang: str, flag_code: str, **params) -> str:
    templates = FLAGS.get(lang, FLAGS["en"])
    template = templates.get(flag_code, FLAGS["en"].get(flag_code, flag_code))
    return template.format(**params)