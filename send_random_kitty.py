from telegram import Bot
import requests


TELEGRAM_TOKEN = '8756892456:AAG_j24G8NH8gS3BtHh1jeaeVxe7LLbyk4E'
CHAT_ID = '1450780782'

bot = Bot(token=TELEGRAM_TOKEN)

URL = 'https://api.thecatapi.com/v1/images/search'  

response = requests.get(URL).json()
random_cat_url = response[0].get('url')

bot.send_photo(CHAT_ID, random_cat_url)

# print(response)
# print(len(response))
# print(response[0])

# chat_id = '1450780782'
# text = 'Вам телеграмма!'
# bot.send_message(chat_id, text)
# bot.send_photo(chat_id, URL)