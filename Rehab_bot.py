from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# دالة بدء البوت
async def start(update: Update, context) -> None:
    await update.message.reply_text('مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟')

# دالة عرض إعلان الوظيفة
async def post_job_ad(update: Update, context) -> None:
    job_ad = '''
    📢 *إعلان:*
    🏠 *اخصائي تأهيل حركي منزلي*  
    🏥 *أخصائي علاج طبيعي وتأهيل وظيفي*  
    🏋️‍♂️ *أخصائي علاج بالحجامة والتدليك الطبي*  

    🔹 تقديم جلسات تأهيل حركي في المنزل للأشخاص الذين يعانون من إصابات أو مشاكل حركية.  
    📩 للحجز أو الاستفسار، يرجى إرسال "حجز جلسة" وسنتواصل معك في أقرب وقت.
    '''
    await update.message.reply_text(job_ad, parse_mode="Markdown")

# دالة عرض الخدمات والأسعار
async def services(update: Update, context) -> None:
    services_list = '''
    💆‍♂️ *قائمة الخدمات والأسعار:*  
    1️⃣ حجامة + فوطة نارية - *250* جنيه  
    2️⃣ مساج ظهر + فوطة نارية + تأهيل يدوي - *250* جنيه  
    3️⃣ جهاز TENS + تأهيل يدوي - *200* جنيه  
    4️⃣ حجامة + مساج ظهر + تأهيل يدوي + Infrared - *350* جنيه  
    5️⃣ مساج للجسم كامل (ظهر + كتف + ذراع + رجلين) + فوطة نارية - *300* جنيه  
    6️⃣ مساج للجسم + TENS + فوطة نارية + حجامة + Infrared + تأهيل يدوي - *450* جنيه  

    📩 للحجز، أرسل "حجز جلسة" وسنقوم بالتواصل معك.
    '''
    await update.message.reply_text(services_list, parse_mode="Markdown")

# دالة إضافة شخص مهتم بحجز جلسة
async def book_session(update: Update, context) -> None:
    user = update.message.from_user
    await update.message.reply_text(
        f"✅ تم إضافة {user.first_name} للحجز.\n📞 رقم التواصل واتساب: 01221903509\n📍 المكان: الإسكندرية"
    )

# دالة خطأ للأوامر غير المعروفة
async def unknown(update: Update, context) -> None:
    await update.message.reply_text("⚠️ لم أفهم طلبك، حاول مرة أخرى.")

def main():
    # استبدل 'YOUR_BOT_TOKEN' بالتوكن الخاص بك
    app = Application.builder().token("7850763372:AAFXLGc5ch3BlmBhe3Bn1tO34lvSt6JU7dQ").build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post_job_ad", post_job_ad))
    app.add_handler(CommandHandler("services", services))  # إضافة أمر الخدمات
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, book_session))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # تشغيل البوت
    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == '__main__':
    main()


