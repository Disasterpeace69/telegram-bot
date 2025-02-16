from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# دالة بدء البوت
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟')

# دالة عرض إعلان الوظيفة
def post_job_ad(update: Update, context: CallbackContext) -> None:
    job_ad = '''
    إعلان: 
    اخصائي تأهيل حركي منزلي
    أخصائي علاج طبيعي وتأهيل وظيفي
    أخصائي علاج يالحجامة والتدليك الطبي
    يقدم جلسات تأهيل حركي في المنزل للأشخاص الذين يعانون من إصابات أو مشاكل حركية.
    للحجز أو الاستفسار، يرجى إرسال "حجز جلسة" وسنتواصل معك في أقرب وقت.
    '''
    update.message.reply_text(job_ad)

# دالة إضافة شخص مهتم بحجز جلسة
def book_session(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    # يمكنك إضافة تفاصيل إضافية مثل رقم الهاتف أو المدينة لو كنت حابب
    update.message.reply_text(f"تم إضافة {user.first_name} للحجز. سنتواصل معك  قريبًا لتحديد موعد الجلسة.")
    
# دالة خطأ للأوامر غير المعروفة
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("لم أفهم طلبك، حاول مرة أخرى.")

def main():
    # استبدال 'YOUR_API_TOKEN' بـ API Token الخاص بك
    updater = Updater("8081186606:AAESLFefGZ69cKv-S1VODAf2UVgqbNOeIpE")

    # الحصول على الموزع
    dispatcher = updater.dispatcher

    # إضافة الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("post_job_ad", post_job_ad))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, book_session))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # بدء البوت
    updater.start_polling()

    # تشغيل البوت حتى التوقف
    updater.idle()

if __name__ == '__main__':
    main()