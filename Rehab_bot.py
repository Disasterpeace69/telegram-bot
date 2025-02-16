from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# دالة بدء البوت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟')

# دالة عرض إعلان الوظيفة
def post_job_ad(update: Update, context: CallbackContext) -> None:
    job_ad = '''
    📢 *إعلان:*
    🏠 *اخصائي تأهيل حركي منزلي*  
    🏥 *أخصائي علاج طبيعي وتأهيل وظيفي*  
    🏋️‍♂️ *أخصائي علاج بالحجامة والتدليك الطبي*  

    🔹 تقديم جلسات تأهيل حركي في المنزل للأشخاص الذين يعانون من إصابات أو مشاكل حركية.  
    📩 للحجز أو الاستفسار، يرجى إرسال "حجز جلسة" وسنتواصل معك في أقرب وقت.
    '''
    update.message.reply_text(job_ad, parse_mode="Markdown")

# دالة إضافة شخص مهتم بحجز جلسة
def book_session(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(
        f"✅ تم إضافة {user.first_name} للحجز.\n📞 رقم التواصل واتساب: 01221903509\n📍 المكان: الإسكندرية"
    )

# دالة خطأ للأوامر غير المعروفة
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("⚠️ لم أفهم طلبك، حاول مرة أخرى.")

def main():
    # استبدل 'YOUR_BOT_TOKEN' بالتوكن الخاص بك
    app = Application.builder().token("YOUR_BOT_TOKEN").build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post_job_ad", post_job_ad))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, book_session))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # تشغيل البوت
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()
