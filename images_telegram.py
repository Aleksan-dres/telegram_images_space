import argparse
import os
import random
import telegram
import time

from dotenv import load_dotenv
from PIL import Image


BYTES_IN_MEGABYTES = 1048576 
PHOTO_SIZE_IN_MEGABYTES = 20

def optimize_photo(file_path): 
    filename, file_extension = os.path.splitext(file_path) 
    optimized_image = f"{filename}_optimized{file_extension}"

    with Image.open(file_path, 'r') as source:
        source.save(optimized_image, format='JPEG',quality=50, optimize=True, progressive=True)
    
    return optimized_image 

def generate_paths(folder_path): 
    file_paths = []
    for file_path in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_path)
        if os.path.isfile(full_path):
            file_paths.append(full_path) 
    return file_paths

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
        folder_path = 'foto_space'
        file_paths = generate_paths(folder_path)

        random.shuffle(file_paths)

        file_path = file_paths[0]
        file_size = os.path.getsize(file_path)
        file_size_megabytes = file_size / BYTES_IN_MEGABYTES
        if file_size_megabytes >= PHOTO_SIZE_IN_MEGABYTES:
            upload_path = optimize_photo(file_path) 
            
        else:
            upload_path = file_path
        
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=telegram_chat_id, document=file)

        time.sleep(interval)


if __name__ == '__main__':
    main()
