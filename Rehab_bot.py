from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توكن البوت
TOKEN = "7850763372:AAFXLGc5ch3BlmBhe3Bn1tO34lvSt6JU7dQ"

# معرف الأدمن (التليجرام ID الخاص بك)
ADMIN_CHAT_ID = "@Zyaad2000"

# دالة بدء البوت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟\n\n'
        'للاطلاع على خدماتنا وأسعار الجلسات، أرسل "تفاصيل".\n'
        'لحجز جلسة، أرسل "حجز جلسة".'
    )

# دالة عرض التفاصيل والأسعار
def show_details(update: Update, context: CallbackContext) -> None:
    details = '''
    🔹 *خدماتنا وأسعار الجلسات:*  
    1️⃣ حجامة + فوطة نارية – *250 جنيه*  
    2️⃣ مساج ظهر + فوطة نارية + تأهيل يدوي – *250 جنيه*  
    3️⃣ جهاز TENS + تأهيل يدوي – *200 جنيه*  
    4️⃣ حجامة + مساج ظهر + تأهيل يدوي + Infrared – *350 جنيه*  
    5️⃣ مساج للجسم كامل + فوطة نارية – *300 جنيه*  
    6️⃣ جلسة شاملة (مساج + TENS + فوطة نارية + حجامة + Infrared + تأهيل يدوي) – *450 جنيه*  

    📍 *المكان:* الإسكندرية  
    📞 *للحجز:* 01221903509  
    '''
    update.message.reply_text(details, parse_mode="Markdown")

# دالة حجز الجلسة
def book_session(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_info = f"🛎 *حجز جديد!*\n👤 الاسم: {user.first_name}\n📩 يوزر: @{user.username if user.username else 'لا يوجد'}\n🆔 ID: {user.id}"

    # إرسال رسالة تأكيد للمستخدم
    update.message.reply_text(
        "✅ تم استلام طلب الحجز بنجاح!\n"
        "📞 سنتواصل معك قريبًا لتأكيد التفاصيل.\n"
        "📍 المكان: الإسكندرية\n"
        "📩 رقم التواصل واتساب: 01221903509"
    )

    # إرسال إشعار للأدمن
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=user_info, parse_mode="Markdown")

# دالة خطأ للأوامر غير المعروفة
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("⚠️ لم أفهم طلبك، حاول مرة أخرى.")

def main():
    app = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("(?i)تفاصيل"), show_details))
    app.add_handler(MessageHandler(filters.Regex("(?i)حجز جلسة"), book_session))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # تشغيل البوت
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()


