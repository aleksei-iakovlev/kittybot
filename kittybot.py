from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import requests


TELEGRAM_TOKEN = '8756892456:AAG_j24G8NH8gS3BtHh1jeaeVxe7LLbyk4E' 
CHAT_ID = '1450780782'
cat_url = 'https://api.thecatapi.com/v1/images/search'  
#dog_url = 'https://api.thedogapi.com/v1/images/search'

bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN)
button = ReplyKeyboardMarkup([['Показать кота']], resize_keyboard=True)


def get_new_image():
    response = requests.get(cat_url).json()
    random_cat = response[0].get('url')
    return random_cat

def new_cat(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('new_cat', new_cat))
updater.dispatcher.add_handler(MessageHandler(Filters.text, new_cat))

updater.start_polling()
updater.idle()
