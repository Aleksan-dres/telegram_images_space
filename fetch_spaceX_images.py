import requests
import json
import os 
import argparse 
from download_and_save_fetch_spacex_image import download_file


def fetch_spacex_last_launch(ID_space_x):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{ID_space_x}")
    response.raise_for_status()
    photos_spacex = response.json()["links"]['flickr']['original'] 
    if not photos_spacex: 
        print("Фотографии отсутствуют для данного запуска")
        return  

    for image, number in enumerate(photos_spacex):
        spacex_image = f"foto_space/spacex{image}.jpg"
        download_file(number, spacex_image)

def main(): 
    parser = argparse.ArgumentParser(description="Загружает фото компании SpaceX")
    parser.add_argument('-id_spacex', help="Укажите id для загрузки фотографий с запуска, если ID нет используйте строку (latest)", default="latest") 
    args = parser.parse_args()

    launch_spacex = args.id_spacex 
    fetch_spacex_last_launch(id_space_x) 

if __name__ == '__main__':
    main()  
