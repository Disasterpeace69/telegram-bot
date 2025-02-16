from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

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

# دالة حجز الجلسة
async def book_session(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    await update.message.reply_text(
        f"✅ تم إضافة {user.first_name} للحجز.\n📞 رقم التواصل واتساب: 01221903509\n📍 المكان: الإسكندرية"
    )

# دالة للأوامر غير المعروفة
async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("⚠️ لم أفهم طلبك، حاول مرة أخرى.")

def main():
    app = Application.builder().token("YOUR_BOT_TOKEN").build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("(?i)تفاصيل|السعر|الجلسات"), send_details))  # رد عند طلب التفاصيل
    app.add_handler(MessageHandler(filters.Regex("(?i)حجز جلسة"), book_session))  # رد عند طلب الحجز
    app.add_handler(MessageHandler(filters.COMMAND, unknown))  # رد للأوامر غير المعروفة

    # تشغيل البوت
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()


