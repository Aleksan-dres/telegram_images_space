import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv
from download_and_save_EPIC_images import download_file

def download_image_nasa_epic(nasa_token, date):
    url_nasa_epic = "https://api.nasa.gov/EPIC/api/natural/date"
    payload = {
        "date": date,
        "api_key": nasa_token
    }
    response = requests.get(url_nasa_epic, params=payload)
    response.raise_for_status()
    foto_epic = response.json()
    foto_epic_images = []
    image_data = []
    for foto in foto_epic:

        foto_epic_original = foto['image']
        foto_epic_images.append(foto_epic_original)
        foto_epic_date = foto['date']
        foto_epic_date_original = foto_epic_date.split(maxsplit=1)[0]
        parsed_date = datetime.datetime.fromisoformat(foto_epic_date_original)
        updated_data = f"{parsed_date:%Y/%m/%d}"
        image_data.append(updated_data)

    return foto_epic_images, image_data


def download_image_nasa_epic_day(nasa_token, foto_epic_images, image_data):
    
    images_quantily = 10
    for image in range(images_quantily):
        url_nasa_day = f"https://api.nasa.gov/EPIC/archive/natural/{image_data[image]}/png/{foto_epic_images[image]}.png"

        epic_foto_space = f"foto_space/space_epic{image}.png"
        download_file(url_nasa_day, epic_foto_space, nasa_token)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    parser = argparse.ArgumentParser(
        description="Загружает фото планеты Земля из космоса")
    parser.add_argument('-date', help='Введите дату(год(4 числа),месяц(2числа),день(2 числа))',
                        default=datetime.datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    date = args.date

    foto_epic_image, image_data = download_image_nasa_epic(nasa_token, date)
    download_image_nasa_epic_day(nasa_token, foto_epic_image, image_data)


if __name__ == '__main__':
    main()
