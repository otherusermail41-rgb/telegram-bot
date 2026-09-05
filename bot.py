import telebot
bot = telebot.TeleBot("7898286437:AAFSg9c6HyNjsj7XqUZK2C8MFiYv0lShNsE")
OWNER = 8993216569

@bot.message_handler(content_types=['text','photo','video','document','sticker','voice'])
def handle(msg):
    try:
        bot.copy_message(msg.chat.id, msg.chat.id, msg.message_id)
        name = msg.from_user.first_name
        uid = msg.from_user.id
        header = f"From: {name}\nID: {uid}"
        if msg.text:
            bot.send_message(OWNER, header + "\n\n" + msg.text)
        elif msg.photo:
            bot.send_photo(OWNER, msg.photo[-1].file_id, caption=header)
        elif msg.video:
            bot.send_video(OWNER, msg.video.file_id, caption=header)
        elif msg.document:
            bot.send_document(OWNER, msg.document.file_id, caption=header)
        elif msg.sticker:
            bot.send_message(OWNER, header)
            bot.send_sticker(OWNER, msg.sticker.file_id)
        elif msg.voice:
            bot.send_voice(OWNER, msg.voice.file_id, caption=header)
    except Exception as e:
        print(e)

print("Bot Running...")
bot.infinity_polling()