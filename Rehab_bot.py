from telegram import Update, InputMediaPhoto, InputMediaVideo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توكن البوت
TOKEN = "7850763372:AAFXLGc5ch3BlmBhe3Bn1tO34lvSt6JU7dQ"

# معرف الأدمن (التليجرام ID الخاص بك)
ADMIN_CHAT_ID = "1237924790"

# دالة بدء البوت مع إرسال الصور والفيديوهات
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'مرحبًا! أنا بوت اخصائي التأهيل الحركي المنزلي. كيف يمكنني مساعدتك؟\n\n'
        'اكتب "تفاصيل" لمعرفة الأسعار والخدمات المتاحة.'
    )
    
    # إرسال مجموعة من الوسائط (6 صور و 4 فيديوهات)
    media = [
        InputMediaPhoto("https://i.postimg.cc/T1xbdkSb/IMG-20250218-170701-055-1.jpg"),  # استبدل بالرابط المباشر للصورة 1
        InputMediaPhoto("https://i.postimg.cc/TPXfHZWn/Whats-App-Image-2025-02-18-at-5-17-12-PM-2.jpg"),  # استبدل بالرابط المباشر للصورة 2
        InputMediaPhoto("https://i.postimg.cc/Gt4WpQyc/Whats-App-Image-2025-02-18-at-5-17-12-PM-1.jpg"),  # استبدل بالرابط المباشر للصورة 3
        InputMediaPhoto("https://i.postimg.cc/9Qdvzzrq/Whats-App-Image-2025-02-18-at-5-17-00-PM.jpg"),  # استبدل بالرابط المباشر للصورة 4
        InputMediaPhoto("https://i.postimg.cc/BvQ402Mv/Whats-App-Image-2025-02-18-at-5-17-09-PM.jpg"),  # استبدل بالرابط المباشر للصورة 5
        InputMediaPhoto("https://i.postimg.cc/qRWTyS0t/Whats-App-Image-2025-02-16-at-11-41-28-PM.jpg"),  # استبدل بالرابط المباشر للصورة 6
    #     InputMediaVideo("https://ia904509.us.archive.org/27/items/vid-20250218-170807-820/VID_20250218_170807_820.ia.mp4") #,  # استبدل بالرابط المباشر للفيديو 1
    #     # InputMediaVideo("https://drive.google.com/uc?export=download&id=1berS2dwYYPqyZ7Mi3E458DSTlaP1-PJ1"),  # استبدل بالرابط المباشر للفيديو 2
    #     # InputMediaVideo("https://drive.google.com/uc?export=download&id=1bdth4G-l-J3Nty32icZKTi20ZAgo7nos"),  # استبدل بالرابط المباشر للفيديو 3
    #     # InputMediaVideo("https://drive.google.com/uc?export=download&id=1bda-VqD07rpV4TvIUrSZihm_wg459-bO")   # استبدل بالرابط المباشر للفيديو 4
    # ]
    await update.message.reply_media_group(media)

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
