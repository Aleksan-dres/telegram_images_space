import requests
import json
import os 
import argparse 
from file import made_file

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    
    with open(filename, 'wb') as foto_space:
        foto_space.write(response.content)

def fetch_spacex_last_launch(ID_space_x):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{ID_space_x}")
    response.raise_for_status()
    foto_x = response.json()["links"]['flickr']['original'] 
    if not foto_x: 
        print("Фотографии отсутствуют для данного запуска")
        return  

    for image, value in enumerate(foto_x):
        filename_1 = f"foto_space/spacex{image}.jpg"
        download_file(value, filename)

def main(): 
    parser = argparse.ArgumentParser(description="Загружает фото компании SpaceX")
    parser.add_argument('-ID_spaceX', help="Укажите ID для загрузки фотографий с запуска, если ID нет используйте строку (latest)", default="latest") 
    args = parser.parse_args()

    ID_space_x = args.ID_spaceX 
    fetch_spacex_last_launch(ID_space_x) 

if __name__ == '__main__':
    main()  
