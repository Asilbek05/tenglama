import telebot
from telebot import types
from module import esolve
bot = telebot.TeleBot("Bot tokenini joylang")

admin_test="id ingizni joylang"
roy=[]
royxat=[]
@bot.message_handler(commands=['start'])
def welcome(message):
  welcome_photo = open('welcome.png','rb')
  obuna = open('obuna.png', 'rb')
  start_message = '<b>Assalomu alaykum hurmatli</b> <a href ="tg://user?id={}">{.first_name}</a> !!!!\n<b>Bizning botimizga xush kelibsiz!!!</b>\n\n<b><i>Siz bu botda Matematikaga oid faqat x no`malumli tenglamani javobini bilib olishinggiz mumkin</i>\n\nBotni qanday ishlatishni 👉 /help 👈 buyrug`ini bosish orqali bilib olishinggiz mumkin</b>\n\n👉 @tenglama_robot'.format(message.chat.id,message.from_user)
  if(message.from_user.id!=admin_test):
    asd=0
    status = ['creator', 'administrator', 'member']
    for chri in status:
      if chri == bot.get_chat_member(chat_id="@cpp_python_uz", user_id=message.from_user.id).status:
        asd=1
        welcome_photo = open('welcome.png', 'rb')
        start_message = '<b>Assalomu alaykum hurmatli</b> <a href ="tg://user?id={}">{.first_name}</a> !!!!\n<b>Bizning botimizga xush kelibsiz!!!</b>\n\n<b><i>Siz bu botda Matematikaga oid faqat x no`malumli tenglamani javobini bilib olishinggiz mumkin</i>\n\nBotni qanday ishlatishni 👉 /help 👈 buyrug`ini bosish orqali bilib olishinggiz mumkin</b>\n\n👉 @tenglama_robot'.format(message.chat.id,message.from_user)
        kk=message.from_user.id
        if(kk in roy):
          bot.send_chat_action(message.chat.id, "upload_photo")
          bot.send_photo(message.chat.id, welcome_photo, caption=start_message, parse_mode='html')
        else:
          
          ob=dict(link=f"@{message.from_user.username}",idsi=f"{message.from_user.id}",name=f"{message.from_user.first_name}")
          royxat.append(ob)
          bot.send_chat_action(message.chat.id, "upload_photo")
          bot.send_photo(message.chat.id, welcome_photo, caption=start_message, parse_mode='html')
        roy.append(kk)
    if(asd!=1):
      markup_inline8 = types.InlineKeyboardMarkup(row_width=1)
      item_yes = types.InlineKeyboardButton(text='➕ Kanalga o`tish', callback_data='yess',
                                            url="https://t.me/cpp_python_uz")
      markup_inline8.add(item_yes)
      kanal_message = '<b>⚠️⚠️⚠️ Bu telegram kanalimizga obuna bo`lmasanggiz Botni ishlata olmaysiz!!!</b>'
      bot.send_chat_action(message.chat.id, "upload_photo")
      bot.send_photo(message.chat.id, obuna,caption="❗️❗️❗️DIQQAT❗️❗️❗️Pastdagi tugma orqali kanalga obuna bo'lib qayta 👉👉 /start 👈👈 ni bosib botdan foydalanishinggiz mumkin!!!",reply_markup=markup_inline8)
  else:
    bot.send_chat_action(message.chat.id, "upload_photo")
    bot.send_photo(message.chat.id, welcome_photo, caption=start_message, parse_mode='html')
 

@bot.message_handler(commands=['help'])
def help_(message):
    bot.send_message(message.chat.id, "Bu bot orqali ixtiyoriy tenglamalarni osongina yechish mumkin\nShunchaki bir no'malumli x tenglama yuboring\n\nMisol: <code>2022/x-(1010+x)*2=0</code>\n\nBot dasturchisi: @Asilbek_developer_oo1\nBizning kanal: @cpp_python_uz",parse_mode="html")

@bot.message_handler(content_types=['text'])
def send_text(message):
  if bool(message.text):
    try:
      res = esolve((message.text).replace(" ", "").lower())
      bot.send_message(message.chat.id, f"🥳 Javob tayyor!\nx = {res}\n\nYana tenglama yuborish uchun xuddi oldingidek ishni bajaring! Ya'ni <b> bir no'malumli x tenglama yuboring!</b>",parse_mode="html")
    except:
      bot.send_message(message.chat.id, "Xato buyruq!!!\n👉 /help 👈 buyrug'i orqali botdan qanday foydalanishni ko'rib chiqing!")

bot.polling(none_stop=True)
