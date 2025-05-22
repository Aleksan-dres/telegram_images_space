import argparse
import os
import random
import telegram
import time
from dotenv import load_dotenv
from PIL import Image


def main():

    load_dotenv()
    token = os.environ['telegram_TOKEN']

    parser = argparse.ArgumentParser(description="Загружает фото в телеграм канал через интервал времени")
    parser.add_argument('-interval', type=int, required=True, help='Укажите интервал времени через который будут публиковаться фотографии')
    args = parser.parse_args()
    interval = args.interval

    bot = telegram.Bot(token=token)
    updates = bot.get_updates()

    while True:

        folder_path = 'foto_space'
        file_names = []
        for file_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file_name)
            if os.path.isfile(full_path):
                file_names.append(full_path)

        random.shuffle(file_names)

        file_path = file_names[0]
        file_size = os.path.getsize(file_path)
        file_size_megabytes = file_size / 1048576
        if file_size_megabytes >= 20:
            image_file = file_path
            filename, file_extension = os.path.splitext(file_path) 
            optimized_image = os.path.join( filename + '_optimized.jpg')

            with Image.open(image_file, 'r') as source:
                source.save(optimized_image, format='JPEG',quality=50, optimize=True, progressive=True)
            upload_path = optimized_image
        else:
            upload_path = file_path
        
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id='@spaccce_images', document=file)

        time.sleep(interval)


if __name__ == '__main__':
    main()
