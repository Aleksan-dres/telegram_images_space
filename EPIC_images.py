import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv
from file import made_file


def download_file(url, filename, token):

    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(filename, 'wb') as foto_space:
        foto_space.write(response.content)


def download_image_nasa_epic(nasa_token, date):
    url_nasa_epic = "https://api.nasa.gov/EPIC/api/natural/date"
    payload = {
        "date": date,
        "api_key": nasa_token
    }
    response = requests.get(url_nasa_epic, params=payload)
    response.raise_for_status()
    foto_epic = response.json()
    foto_epic_image = []
    modified_data = []
    for item in foto_epic:

        foto_epic_original = item['image']
        foto_epic_image.append(foto_epic_original)
        foto_epic_date = item['date']
        foto_epic_date_original = foto_epic_date.split(maxsplit=1)[0]
        parsed_date = datetime.datetime.fromisoformat(foto_epic_date_original)
        updated_data = f"{parsed_date:%Y/%m/%d}"
        modified_data.append(updated_data)

    return foto_epic_image, modified_data


def download_image_nasa_epic_day(nasa_token, foto_epic_image, modified_data):
    payload = {
        "api_key": nasa_token
    }
    quantily_images = 10
    for images in range(quantily_images):
        url_nasa_day = f"https://api.nasa.gov/EPIC/archive/natural/{modified_data[images]}/png/{foto_epic_image[images]}.png"

        filename = f"foto_space/space_epic{images}.png"
        download_file(url_nasa_day, filename, nasa_token)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    parser = argparse.ArgumentParser(
        description="Загружает фото планеты Земля из космоса")
    parser.add_argument('-date', help='Введите дату(год(4 числа),месяц(2числа),день(2 числа))',
                        default=datetime.datetime.now().strftime("%Y-%m-%d"))
    args = parser.parse_args()

    date = args.date

    foto_epic_image, modified_data = download_image_nasa_epic(nasa_token, date)
    download_image_nasa_epic_day(nasa_token, foto_epic_image, modified_data)


if __name__ == '__main__':
    main() 
