import logging
import os
import time
from collections import defaultdict
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, ConversationHandler, filters
)
from utils.checker import check_link
from utils.languages import get_text, format_flag

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CHOOSE_LANG = 0
WAIT_LINK   = 1

# ── Rate limiting ─────────────────────────────────────────────────────────────
# Allow each user MAX_REQUESTS checks per WINDOW_SECONDS
MAX_REQUESTS    = 5
WINDOW_SECONDS  = 60

# { user_id: [timestamp, timestamp, ...] }
_rate_tracker: dict[int, list[float]] = defaultdict(list)

def _is_rate_limited(user_id: int) -> tuple[bool, int]:
    """Returns (limited, seconds_to_wait)."""
    now   = time.monotonic()
    times = _rate_tracker[user_id]

    # Drop timestamps outside the current window
    times[:] = [t for t in times if now - t < WINDOW_SECONDS]

    if len(times) >= MAX_REQUESTS:
        wait = int(WINDOW_SECONDS - (now - times[0])) + 1
        return True, wait

    times.append(now)
    return False, 0


# ── Handlers ──────────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    keyboard = [
        [InlineKeyboardButton("🇹🇯 کوردی",   callback_data="lang_ku")],
        [InlineKeyboardButton("🇮🇶 العربية", callback_data="lang_ar")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
    ]
    await update.message.reply_text(
        "🛡️ *Scam Link Detector*\n\n"
        "Instantly check if a link is safe before you click it.\n\n"
        "Choose your language / زمانت هەڵبژێرە / اختر لغتك",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    return CHOOSE_LANG


async def language_chosen(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    ctx.user_data["lang"] = lang
    await query.edit_message_text(get_text(lang, "welcome"), parse_mode="Markdown")
    return WAIT_LINK


async def receive_link(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang    = ctx.user_data.get("lang", "en")
    user_id = update.effective_user.id
    text    = update.message.text.strip()

    # ── Rate limit check ─────────────────────────────────────────────────────
    limited, wait = _is_rate_limited(user_id)
    if limited:
        msg = get_text(lang, "rate_limited").format(seconds=wait)
        await update.message.reply_text(msg, parse_mode="Markdown")
        return WAIT_LINK

    # ── Basic URL validation ──────────────────────────────────────────────────
    if not ("http://" in text or "https://" in text or "." in text):
        await update.message.reply_text(get_text(lang, "not_a_link"), parse_mode="Markdown")
        return WAIT_LINK

    status_msg = await update.message.reply_text(
        get_text(lang, "checking"), parse_mode="Markdown"
    )
    result = check_link(text)
    report = _build_report(lang, text, result)

    keyboard = [[
        InlineKeyboardButton(get_text(lang, "btn_check_another"), callback_data="check_another"),
        InlineKeyboardButton(get_text(lang, "btn_report"),        callback_data="report_link"),
    ]]
    await status_msg.edit_text(
        report,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
    )
    return WAIT_LINK


def _build_report(lang: str, url: str, r: dict) -> str:
    score  = r["score"]
    risk   = r["risk"]
    emoji  = {"safe": "🟢", "medium": "🟡", "danger": "🔴"}[risk]
    status = get_text(lang, f"status_{risk}")

    flag_lines = []
    for code, params in r["flags"]:
        flag_lines.append(f"  ⚠️ {format_flag(lang, code, **params)}")

    flags_text = (
        "\n".join(flag_lines) if flag_lines
        else "  ✅ " + get_text(lang, "no_flags")
    )

    divider = "──────────────────"
    return "\n".join([
        f"{emoji} *{status}*",
        divider,
        f"🔗 `{r.get('domain', url[:50])}`",
        f"📊 {get_text(lang, 'risk_score')}: *{score}/100*",
        "",
        f"🔍 *{get_text(lang, 'findings')}:*",
        flags_text,
        divider,
        f"_{get_text(lang, 'advice')[risk]}_",
    ])


async def button_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    if query.data == "check_another":
        await query.message.reply_text(get_text(lang, "send_link"), parse_mode="Markdown")
    elif query.data == "report_link":
        await query.message.reply_text(get_text(lang, "report_thanks"), parse_mode="Markdown")
    return WAIT_LINK


async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    await update.message.reply_text(get_text(lang, "help_text"), parse_mode="Markdown")


async def unknown(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    await update.message.reply_text(get_text(lang, "use_start"), parse_mode="Markdown")


# ── App bootstrap ─────────────────────────────────────────────────────────────

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("❌ BOT_TOKEN not found in .env file!")

    app  = ApplicationBuilder().token(token).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE_LANG: [CallbackQueryHandler(language_chosen, pattern="^lang_")],
            WAIT_LINK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_link),
                CallbackQueryHandler(
                    button_callback, pattern="^(check_another|report_link)$"
                ),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
        allow_reentry=True,
    )
    app.add_handler(conv)
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT, unknown))
    logger.info("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()