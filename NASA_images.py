import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


if not os.path.exists("foto_space"):
    os.mkdir("foto_space")
foto_space = () 


url_nasa = "https://api.nasa.gov/planetary/apod"


def image_nasa_every_day(url_nasa,nasa_token,initial_date,final_date): 
    payload = {
        "start_date": initial_date,
        "end_date": final_date,
        "api_key": nasa_token
    }
    response = requests.get(url_nasa, params=payload) 
    response.raise_for_status()
    foto_every_day = response.json()  
    
    
    for i, image in enumerate(foto_every_day): 
        if not foto_every_day or 'media_type' not in image or image['media_type'] != 'image': 
            continue 
        foto_url = image["url"] 
        format_link = urlparse(foto_url) 
        path_link = format_link.path
        splitext = os.path.splitext(path_link)
        format_foto = splitext[1] 
        if format_foto != ".jpg": 
            continue 

        filename_1 = f"foto_space/nasa{i}.jpg"

        response = requests.get(foto_url)
        response.raise_for_status()

        with open(filename_1, 'wb') as foto_space:
            foto_space.write(response.content) 



def main(): 
    
    
    load_dotenv()
    nasa_token = os.environ["NASA_API"]  
    date_now = datetime.datetime.now()
    monat = date_now - datetime.timedelta(days=30)

    parser = argparse.ArgumentParser(description="Загружает лучшее космические фото дня")
    parser.add_argument('-start_date', help='Введите дату начала отсчета(год(4 числа),месяц(2числа),день(2 числа))', default=monat.strftime("%Y-%m-%d"))
    parser.add_argument('-end_date', help='Введите дату окончания отсчета(год(4 числа),месяц(2числа),день(2 числа))', default=datetime.datetime.now().strftime("%Y-%m-%d")) 
     
    args = parser.parse_args()

    initial_date = args.start_date
    final_date = args.end_date
    

    image_nasa_every_day(url_nasa,nasa_token,initial_date,final_date)  
        
if __name__ == '__main__':
    main()  
