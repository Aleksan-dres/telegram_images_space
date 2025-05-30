import requests
import json
import os 
import argparse 
from download_and_save_images import download_and_save_file


def fetch_spacex_last_launch(launch_spacex):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_spacex}")
    response.raise_for_status()
    spacex_photos = response.json()["links"]['flickr']['original'] 
    if not spacex_photos: 
        print("Фотографии отсутствуют для данного запуска")
        return  

    for image, number in enumerate(spacex_photos): 
        spacex_image = f"spacex{image}.jpg" 
        path_to_file_with_photos = f"foto_space/{spacex_image}"
        
        download_and_save_file(number, path_to_file_with_photos, None)

def main(): 
    parser = argparse.ArgumentParser(description="Загружает фото компании SpaceX")
    parser.add_argument('-id_spacex', help="Укажите id для загрузки фотографий с запуска, если ID нет используйте строку (latest)", default="latest") 
    args = parser.parse_args()

    launch_spacex = args.id_spacex 
    fetch_spacex_last_launch(launch_spacex) 

if __name__ == '__main__':
    main() 
