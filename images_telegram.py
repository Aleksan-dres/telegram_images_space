import argparse
import os
import random
import telegram
import time

from dotenv import load_dotenv
from PIL import Image


def main():

    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN'] 
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

    parser = argparse.ArgumentParser(description="Загружает фото в телеграм канал через интервал времени")
    parser.add_argument('-interval', type=int, required=True, help='Укажите интервал времени через который будут публиковаться фотографии')
    args = parser.parse_args()
    interval = args.interval

    bot = telegram.Bot(token=telegram_token)
    

    while True:
        megabytes = 1048576 
        photo_size = 20
        folder_path = 'foto_space'
        file_names = []
        for file_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file_name)
            if os.path.isfile(full_path):
                file_names.append(full_path)

        random.shuffle(file_names)

        file_path = file_names[0]
        file_size = os.path.getsize(file_path)
        file_size_megabytes = file_size / megabytes
        if file_size_megabytes >= photo_size:
            image_file = file_path
            filename, file_extension = os.path.splitext(file_path) 
            optimized_image = f"{filename}_optimized{file_extension}"

            with Image.open(image_file, 'r') as source:
                source.save(optimized_image, format='JPEG',quality=50, optimize=True, progressive=True)
            upload_path = optimized_image
        else:
            upload_path = file_path
        
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=telegram_chat_id, document=file)

        time.sleep(interval)


if __name__ == '__main__':
    main()
