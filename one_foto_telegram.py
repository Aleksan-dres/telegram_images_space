import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(telegram_token)
        
    file_path = 'foto_space/spacex2.jpg'

    with open(file_path, 'rb') as file:
        bot.send_document(chat_id=telegram_chat_id, document=file)


if __name__ == '__main__':
    main()
