from telegram.ext import InlineQueryHandler, CommandHandler, Updater
import requests
import re

def get_url_func():  # Access the API & get URL of the content (image or GIF or video)
    b1 = requests.get('https://random.dog/woof.json').json()
    url1 = b1['url']
    return url1

def get_image_url_func():  # To select only pictures (not GIFs / videos) from 'https://random.dog/woof.json'
    valid_extensions = ['png', 'jpeg', 'jpg']
    extract_file_extension = ''
    while extract_file_extension not in valid_extensions:
        url3 = get_url_func()
        extract_file_extension = re.search("([^.]*)$", url3).group(1).lower()
    return url3

def go(update, context):  
    url2 = get_image_url_func()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url2)

def main():
    updater1 = Updater('Your-TOKEN')  # Enter your Bot's Token here. Telegram gives you this Token when you are registering a new Bot there.
    dp1 = updater1.dispatcher
    dp1.add_handler(CommandHandler('go', go))
    updater1.start_polling()
    updater1.idle()

if __name__ == '__main__':
    main()
