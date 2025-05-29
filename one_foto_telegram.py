import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_token = os.environ['telegram_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token)
    photo_space = "space2.jpg"
    file_path = f'foto_space/{photo_space}'

    with open(file_path, 'rb') as file:
        bot.send_document(chat_id=telegram_chat_id, document=file)


if __name__ == '__main__':
    main()
