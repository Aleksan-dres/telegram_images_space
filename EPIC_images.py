import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv
from download_and_save_images import download_and_save_file

def download_images_nasa_epic(nasa_token, date):
    url_nasa_epic = "https://api.nasa.gov/EPIC/api/natural/date"
    payload = {
        "date": date,
        "api_key": nasa_token
    }
    response = requests.get(url_nasa_epic, params=payload)
    response.raise_for_status()
    epic_fotos = response.json()
    epic_images = []
    image_dates = []
    for foto in epic_fotos:

        epic_foto_original = foto['image']
        epic_images.append(epic_foto_original)
        epic_foto_date = foto['date']
        epic_foto_date_original = epic_foto_date.split(maxsplit=1)[0]
        parsed_date = datetime.datetime.fromisoformat(foto_epic_date_original)
        updated_date = f"{parsed_date:%Y/%m/%d}"
        image_date.append(updated_date)

    return epic_images, image_dates


def download_images_nasa_epic_day(nasa_token, epic_images, image_date):
    
    images_quantily = 10
    for photo in range(images_quantily):
        url_nasa_day = f"https://api.nasa.gov/EPIC/archive/natural/{image_date[photo]}/png/{epic_images[photo]}.png"

        epic_foto_space = f"space_epic{photo}.png" 
        path_to_file_with_photos = f"foto_space/{epic_foto_space}"
        download_and_save_file(url_nasa_day, path_to_file_with_photos, nasa_token)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    parser = argparse.ArgumentParser(
        description="Загружает фото планеты Земля из космоса")
    parser.add_argument('-date', help='Введите дату(год(4 числа),месяц(2числа),день(2 числа))',
                        default=datetime.datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    date = args.date

    epic_images, image_dates = download_images_nasa_epic(nasa_token, date)
    download_images_nasa_epic_day(nasa_token, epic_images, image_date)


if __name__ == '__main__':
    main()
