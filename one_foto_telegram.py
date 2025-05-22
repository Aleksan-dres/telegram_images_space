import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ['telegram_TOKEN']
    
    bot = telegram.Bot(token)
        
    file_path = 'foto_space/spacex2.jpg'

    with open(file_path, 'rb') as file:
        bot.send_document(chat_id='@spaccce_images', document=file)


if __name__ == '__main__':
    main()
