import telebot
from telebot import types
import time

bot = telebot.TeleBot('492567522:AAGIsULJPyQ7wfYFgZ4VDSefFcw10ERepTA')

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_address = types.InlineKeyboardButton('Адрес магазина')
btn_payment = types.InlineKeyboardButton('Способы оплаты')
btn_delivery = types.InlineKeyboardButton('Доставка')
btn_help = types.InlineKeyboardButton('/help')
markup_menu.add(btn_address, btn_delivery, btn_payment, btn_help)

markup_delivery = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_pochta = types.InlineKeyboardButton('Доставка почтой')
btn_kuryer = types.InlineKeyboardButton('Курьерская доставка(в пределах Казани)')
btn_back_to_menu = types.InlineKeyboardButton('Назад в меню')
btn_sam = types.InlineKeyboardButton('Самовывоз')
markup_delivery.add(btn_pochta, btn_kuryer, btn_sam, btn_back_to_menu)



@bot.message_handler(commands=['start', 'help'])
def say_welcome(message):
    bot.send_message(message.chat.id, "Привет! Меня зовут Marat test bot. Я - тестовый бот для обучения. Я помогаю своему создателю оттачивать навыки программирвоания =)"
                                     "\n"
                                      "Выбери один из пунктов:", reply_markup=markup_menu)

@bot.message_handler(content_types=['text'])
def answers(message):
    if (message.text == "привет" or message.text == "Привет"):
        bot.send_message(message.chat.id, "Привет! Хей, рад тебя видеть! =)")
    elif message.text == "Адрес магазина":
        bot.send_message(message.chat.id, "Хей, лови адрес!")
        bot.send_message(message.chat.id, "г. Казань, улица Баумана, 3")
        time.sleep(1)
        bot.send_message(message.chat.id, "увидимся")
    elif message.text == "Доставка":
        bot.send_message(message.chat.id, "Вы нажали кнопку доставка. Спасибо, выберите удобный способ:", reply_markup=markup_delivery)
    elif message.text == "Способы оплаты":
        bot.send_message(message.chat.id, "Сейчас посмотрю, какие способы есть...")
        time.sleep(1)
        bot.send_message(message.chat.id, "Можно оплатить переводом на карту Сбербанк, либо наличными, при получении товара")
        time.sleep(1)
        bot.send_message(message.chat.id, "К оплате также принимаюся монеты XRP")
    elif message.text == "Назад в меню":
        bot.send_message(message.chat.id, "ок.", reply_markup=markup_menu)
    elif message.text == "Самовывоз":
        bot.send_message(message.chat.id, "Адрес: г. Казань, улица Баумана, 3")
    elif message.text == "Доставка почтой":
        bot.send_message(message.chat.id, "Введите адрес доставки и почтовый индекс")



if __name__ == '__main__':
    bot.polling(none_stop=True)