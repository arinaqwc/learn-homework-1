"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import setting
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь!')

def get_planet_name(update, context):
  name = update.message.text
  planet=ephem.name()
  if hasattr(ephem, planet):
    planet.computer()
    print(ephem.constellation(planet))
    update.message.reply_text(ephem.constellation(planet))


  



#def talk_to_me(update, context):
    #text=update.message.text
    #print(text)
    #update.message.reply_text(text)

def main():
    mybot=Updater(setting.API_KEY, use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', get_planet_name))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()


