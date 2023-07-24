import telebot
from telebot import types

bot = telebot.TeleBot('***********************************')

name = ''
surename = ''
age = 0 

@bot.message_handler(content_types=['text'])
def startReg(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Type your name")
        bot.register_next_step_handler(message, getName)  
    else:
        bot.send_message(message.from_user.id, "Type /reg")

def getName(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Type your sure name")
    bot.register_next_step_handler(message, getSureName) 

def getSureName(message):
    global surename
    surename = message.text
    bot.send_message(message.from_user.id, "Type your age")
    bot.register_next_step_handler(message, getAge)

def getAge(message):
    global age 
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Input must be integer")
        keyboard = types.InlineKeyboardMarkup()
        keyYes = types.InlineKeyboardButton(text="Yes", callback_data="yes")
        keyboard.add(keyYes)
        keyNo = types.InlineKeyboardButton(text="No", callback_data="no")
        keyboard.add(keyNo)
        question = "Your age " + str(age) + ", your name " + str(name)+ " " + str(surename)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard) 

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Success')
    elif call.data == "no":  
        bot.send_message(call.message.chat.id, "Type /reg if you want to repeat registration.") 
        

bot.polling(none_stop=True, interval=0)
