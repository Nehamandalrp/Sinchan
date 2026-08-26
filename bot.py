import os
from threading import Thread
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Dummy Web Server (Render ko 24/7 active rakhne ke liye)
web_app = Flask("")


@web_app.route("/")
def home():
    return "Bot is running 24/7!"


def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()


# ============================================================
# CONFIGURATION
# ============================================================

BOT_TOKEN = "8860299949:AAH4sI5zTCuIiq--KrYIKCv87QVT7Xy8ukc"

# Admin ka numeric Telegram Chat ID
ADMIN_CHAT_ID = 8200494184


# ============================================================
# CATEGORY DETAILS WITH IMAGES
# ============================================================

CATEGORY_DETAILS = {
    "category_1": {
        "name": "🌟 Premium VIP Pack",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr1.jpg",
    },
    "category_2": {
        "name": "🎬 Exclusive Collection",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr2.jpg",
    },
    "category_3": {
        "name": "🚀 Super Saver Pass",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr3.jpg",
    },
    "category_4": {
        "name": "💎 Ultra Access",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr4.jpg",
    },
    "category_5": {
        "name": "⚡ Special Bundle",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr5.jpg",
    },
    "category_6": {
        "name": "👑 Pro Unlimited",
        "text": (
            "🔥 300+ MEDIA / 700+ MEDIA\n"
            "🔥 LIFETIME MEMBERSHIP\n\n"
            "✅ SMALL PACK RS • 299₹/-\n"
            "✅ BIG PACK RS • 499₹/-\n\n"
            "INTERNATIONAL PRICE 👇\n"
            "✅ SMALL PACK • 15$\n"
            "✅ BIG PACK • 25$"
        ),
        "image": "qr6.jpg",
    },
}


# ============================================================
# PAYMENT DETAILS
# ============================================================

BINANCE_DETAILS = """
💳 Binance

UID:
1176282510

Username:
sanjudox

Step 1️⃣ Send Payment
Step 2️⃣ Send Payment Screenshot For Verification
Step 3️⃣ Wait For Reply
"""

PAYPAL_DETAILS = """
💳 PayPal

Username - @Rajkamalhero   

Step 1️⃣ Send Payment
Step 2️⃣ Send Payment Screenshot For Verification
Step 3️⃣ Wait For Reply
"""

REMITLY_DETAILS = """
💳 Remitly to UPI 

UPI: sanjubaba-international@cnrb

Step 1️⃣ Send Payment
Step 2️⃣ Send Payment Screenshot For Verification
Step 3️⃣ Wait For Reply
"""

UPI_DETAILS = """
💳 UPI

UPI ID:
sanjubaba-international@cnrb 
"""

REVOLUT_DETAILS = """
💳 Revolut

Contact @Raniivideo directly.
"""

CRYPTO_DETAILS = """
💳 USDT / Bitcoin / Crypto

⭐ USDT Address with Network 🛜 
ETH -  0x22c9fe0319ddad833f3fe13fb942140aa79dff34
SOL -  F7ANEJ8vfyFhR4VEnmobyeBPWqeJEWTLbWUgD8dr2UNe
TRX -  TBGsETLni6zfKbqhWLNanJ8DtswXgMcXoq 

⭐ BITCOIN Address with Network 🛜 
BTC -  15cxVVopFtrG3wxsjJEYj5LTEFFyb6sQ7P
ETH -  0x22c9fe0319ddad833f3fe13fb942140aa79dff34 
BSC -  0x22c9fe0319ddad833f3fe13fb942140aa79dff34
"""

PACKAGE_DETAILS = """
📦 Mega All-In-One Package

⭐ Complete Premium Channel Access
⭐ Unlimited Media Downloads
⭐ Direct High-Speed Cloud Drive Access

PRICE - 1999₹ 🪙  @Raniivideo 
INTERNATIONAL PRICE - 99$ 💰

📍 500 GB Cloud Storage Included Free
"""


# ============================================================
# KEYBOARDS
# ============================================================


def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🌟 Premium VIP", callback_data="category_1"
            ),
            InlineKeyboardButton(
                "🎬 Exclusive Collection", callback_data="category_2"
            ),
        ],
        [
            InlineKeyboardButton(
                "🚀 Super Saver", callback_data="category_3"
            ),
            InlineKeyboardButton("💎 Ultra Access", callback_data="category_4"),
        ],
        [
            InlineKeyboardButton("⚡ Special Bundle", callback_data="category_5"),
            InlineKeyboardButton("👑 Pro Unlimited", callback_data="category_6"),
        ],
        [
            InlineKeyboardButton(
                "📦 All Package", callback_data="all_package"
            )
        ],
        [InlineKeyboardButton("☎️ Helpline", callback_data="helpline")],
    ]
    return InlineKeyboardMarkup(keyboard)


def category_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "💳 How To Send Payment", callback_data="payment_menu"
            )
        ],
        [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)


def payment_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("✅ Binance", callback_data="payment_binance"),
            InlineKeyboardButton("✅ PayPal", callback_data="payment_paypal"),
        ],
        [
            InlineKeyboardButton("✅ Remitly", callback_data="payment_remitly"),
            InlineKeyboardButton("✅ QR", callback_data="payment_qr"),
        ],
        [
            InlineKeyboardButton("✅ UPI", callback_data="payment_upi"),
            InlineKeyboardButton("✅ Revolut", callback_data="payment_revolut"),
        ],
        [
            InlineKeyboardButton(
                "✅ USDT / Bitcoin / Crypto", callback_data="payment_crypto"
            )
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="back_category"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def payment_page_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📸 Send Payment Screenshot For Verification",
                url="https://t.me/Raniivideo",
            )
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="payment_menu"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


# ============================================================
# START
# ============================================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Welcome! Which Category Do You Want?"
    await update.message.reply_text(text, reply_markup=main_menu_keyboard())


# ============================================================
# CALLBACK HANDLER
# ============================================================


async def send_category_post(
    query, category, context: ContextTypes.DEFAULT_TYPE
):
    """Helper function to send category photo with text caption"""
    text = f"📢 {category['name']}\n\n{category['text']}"
    image_file = category.get("image")

    # Purana text message delete karke photo ke sath new message bhejte hain
    try:
        await query.message.delete()
    except Exception:
        pass

    if image_file and os.path.exists(image_file):
        with open(image_file, "rb") as photo:
            await context.bot.send_photo(
                chat_id=query.from_user.id,
                photo=photo,
                caption=text,
                reply_markup=category_keyboard(),
            )
    else:
        # Agar photo file nahi milti to text message bhej dega
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=text,
            reply_markup=category_keyboard(),
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        try:
            await query.message.delete()
        except Exception:
            pass
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text="Which Category Do You Want?",
            reply_markup=main_menu_keyboard(),
        )
        return

    # CATEGORY CLICKED
    if data in CATEGORY_DETAILS:
        category = CATEGORY_DETAILS[data]
        context.user_data["selected_category"] = data
        await send_category_post(query, category, context)
        return

    if data == "payment_menu":
        try:
            await query.message.delete()
        except Exception:
            pass
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text="💳 Select Your Payment Method",
            reply_markup=payment_keyboard(),
        )
        return

    if data == "back_category":
        category_id = context.user_data.get("selected_category", "category_1")
        category = CATEGORY_DETAILS[category_id]
        await send_category_post(query, category, context)
        return

    if data == "payment_qr":
        caption = (
            "💳 QR Payment\n\n"
            "Step 1️⃣ Send Payment\n\n"
            "Step 2️⃣ Send Payment Screenshot For Verification\n\n"
            "Step 3️⃣ Wait For Reply"
        )
        try:
            await query.message.delete()
        except Exception:
            pass

        if os.path.exists("Qr.jpg"):
            with open("Qr.jpg", "rb") as qr:
                await context.bot.send_photo(
                    chat_id=query.from_user.id,
                    photo=qr,
                    caption=caption,
                    reply_markup=payment_page_keyboard(),
                )
        else:
            await context.bot.send_message(
                chat_id=query.from_user.id,
                text=f"{caption}\n\n(Note: Qr.jpg image file not found on server)",
                reply_markup=payment_page_keyboard(),
            )
        return

    payment_details = {
        "payment_binance": BINANCE_DETAILS,
        "payment_paypal": PAYPAL_DETAILS,
        "payment_remitly": REMITLY_DETAILS,
        "payment_upi": UPI_DETAILS,
        "payment_revolut": REVOLUT_DETAILS,
        "payment_crypto": CRYPTO_DETAILS,
    }

    if data in payment_details:
        try:
            await query.message.delete()
        except Exception:
            pass
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=payment_details[data],
            reply_markup=payment_page_keyboard(),
        )
        return

    if data == "all_package":
        keyboard = [
            [
                InlineKeyboardButton(
                    "💳 How To Send Payment", callback_data="payment_menu"
                )
            ],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")],
        ]
        try:
            await query.message.delete()
        except Exception:
            pass
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=PACKAGE_DETAILS,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    if data == "helpline":
        keyboard = [
            [InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")]
        ]
        try:
            await query.message.delete()
        except Exception:
            pass
        await context.bot.send_message(
            chat_id=query.from_user.id,
            text=(
                "❓ Contact: @raniivideo , @sanju100K\n\n"
                "Please contact our support team and wait for a reply."
            ),
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return


# ============================================================
# SCREENSHOT HANDLER
# ============================================================


async def receive_screenshot(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    if not context.user_data.get("waiting_for_screenshot"):
        return

    user = update.effective_user
    username_text = (
        f"🔗 Username: @{user.username}"
        if user.username
        else "🔗 Username: Not Available"
    )

    caption = (
        "📸 NEW PAYMENT SCREENSHOT\n\n"
        f"👤 Name: {user.full_name}\n"
        f"🆔 User ID: {user.id}\n"
        f"{username_text}"
    )

    if update.message.photo:
        await context.bot.send_photo(
            chat_id=ADMIN_CHAT_ID,
            photo=update.message.photo[-1].file_id,
            caption=caption,
        )
        await update.message.reply_text(
            "✅ Screenshot received successfully.\nYour payment will be verified."
        )
    elif update.message.document:
        await context.bot.send_document(
            chat_id=ADMIN_CHAT_ID,
            document=update.message.document.file_id,
            caption=caption,
        )
        await update.message.reply_text(
            "✅ Payment proof received successfully."
        )
    else:
        await update.message.reply_text("❌ Please send a screenshot/image.")
        return

    context.user_data["waiting_for_screenshot"] = False


# ============================================================
# ERROR HANDLER
# ============================================================


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")


# ============================================================
# RUN BOT
# ============================================================


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(
        MessageHandler(
            filters.PHOTO | filters.Document.IMAGE, receive_screenshot
        )
    )

    app.add_error_handler(error_handler)

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    keep_alive()
    main()
