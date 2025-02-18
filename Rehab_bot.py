from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توكن البوت
TOKEN = "7850763372:AAFXLGc5ch3BlmBhe3Bn1tO34lvSt6JU7dQ"

# معرف الأدمن (التليجرام ID الخاص بك)
ADMIN_CHAT_ID = "1237924790"

# دالة بدء البوت
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟\n\nاكتب "تفاصيل" لمعرفة الأسعار والخدمات المتاحة.')

# دالة إرسال تفاصيل الخدمات والأسعار
async def send_details(update: Update, context: CallbackContext) -> None:
    details = """
    🔹 *الخدمات المتاحة والأسعار:*
    
    1️⃣ *حجامة + فوطه نارية* - 250 جنيه  
    2️⃣ *مساج ظهر + فوطه نارية + تأهيل يدوي* - 250 جنيه  
    3️⃣ *جهاز TENS + تأهيل يدوي* - 200 جنيه  
    4️⃣ *حجامة + مساج ظهر + تأهيل يدوي + Infra Red* - 350 جنيه  
    5️⃣ *مساج كامل للجسم (ظهر + كتف + ذراع + رجلين) + فوطه نارية* - 300 جنيه  
    6️⃣ *مساج للجسم + TENS + فوطه نارية + حجامة + Infra Red + تأهيل يدوي* - 450 جنيه  
    📩 للحجز أو الاستفسار، أرسل "حجز جلسة" وسنتواصل معك في أقرب وقت.
    """
    await update.message.reply_text(details, parse_mode="Markdown")

# دالة حجز الجلسة وإشعار الأدمن
async def book_session(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user

    # إرسال تأكيد الحجز للمستخدم
    await update.message.reply_text(
        f"✅ تم إضافة {user.first_name} للحجز.\n📞 رقم التواصل واتساب: 01221903509\n📍 المكان: الإسكندرية"
    )

    # إرسال إشعار للأدمن
    admin_message = (
        f"🛎 *حجز جديد!*\n"
        f"👤 *الاسم:* {user.first_name} {user.last_name if user.last_name else ''}\n"
        f"📩 *يوزر:* @{user.username if user.username else 'لا يوجد'}\n"
        f"🆔 *ID:* {user.id}"
    )
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message, parse_mode="Markdown")

# دالة للأوامر غير المعروفة
async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("⚠️ لم أفهم طلبك، حاول مرة أخرى.")

def main():
    app = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("(?i)تفاصيل|السعر|الجلسات"), send_details))
    app.add_handler(MessageHandler(filters.Regex("(?i)حجز جلسة"), book_session))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # تشغيل البوت
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()


