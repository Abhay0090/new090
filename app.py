from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import os
import time
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram.ext.utils.request import Request

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define global variables
PHONE_NUMBER = "YOUR_PHONE_NUMBER_WITH_COUNTRY_CODE"
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# Define Telegram bot functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the WhatsApp Web bot. Please scan the QR code to log in to WhatsApp Web.")

def receive_message(update, context):
    message = update.message.text
    logging.info("Received message: %s", message)
    # Send the incoming message to the Telegram bot
    bot.send_message(chat_id=CHAT_ID, text=message)

# Initialize Telegram bot
bot = telegram.Bot(token=BOT_TOKEN)
request = Request(connect_timeout=60, read_timeout=60, con_pool_size=10)
updater = Updater(BOT_TOKEN, request=request)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.text, receive_message))
updater.start_polling()

# Define Chrome options to run Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Define WhatsApp Web login URL and Chrome driver path
WA_URL = "https://web.whatsapp.com/"
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"

# Start Chrome driver in headless mode and open WhatsApp Web login URL
driver = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options=chrome_options)
driver.get(WA_URL)

# Wait for QR code to load
time.sleep(5)

# Get QR code image URL
qr_element = driver.find_element_by_xpath("//div[@class='_2EZ_m']")
qr_image_url = qr_element.find_element_by_tag_name("img").get_attribute("src")

# Send QR code image to Telegram bot
qr_image = requests.get(qr_image_url).content
bot.send_photo(chat_id=CHAT_ID, photo=qr_image)

# Wait for user to log in to WhatsApp Web
while True:
    try:
        driver.find_element_by_xpath("//div[@class='_3NsgW']")
        break
    except:
        time.sleep(1)

# Get all incoming messages and send them to Telegram bot
while True:
    incoming_messages = driver.find_elements_by_xpath("//span[@class='_3Whw5 selectable-text invisible-space copyable-text']")
    for message in incoming_messages:
        text = message.text
        if text:
            logging.info("Received message: %s", text)
            bot.send_message(chat_id=CHAT_ID, text=text)
    time.sleep(1)
