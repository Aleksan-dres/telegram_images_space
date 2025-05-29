import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from download_and_save_NASA_images import download_and_save_file

def download_images_nasa_every_day(nasa_token,initial_date,final_date): 
    url_nasa = "https://api.nasa.gov/planetary/apod" 
    payload = {
        "start_date": initial_date,
        "end_date": final_date,
        "api_key": nasa_token
    }
    response = requests.get(url_nasa, params=payload) 
    response.raise_for_status()
    fotos_every_day = response.json()  
    
    
    for number, foto in enumerate(fotos_every_day): 
        if 'media_type' not in foto or foto['media_type'] != 'image': 
            continue 
        foto_url = foto["url"] 
        format_link = urlparse(foto_url) 
        path_link = format_link.path
        splitext = os.path.splitext(path_link)
        format_foto = splitext[1] 
        if format_foto != ".jpg": 
            continue 

        nasa_image = f"nasa{number}.jpg" 
        path_to_file_with_photos = f"foto_space/{nasa_image}"

        download_and_save_file(foto_url, path_to_file_with_photos)



def main(): 
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]  
    date_now = datetime.datetime.now()
    days_30 = date_now - datetime.timedelta(days=30)

    parser = argparse.ArgumentParser(description="Загружает лучшее космические фото дня")
    parser.add_argument('-start_date', help='Введите дату начала отсчета(год(4 числа),месяц(2числа),день(2 числа))', default=days_30.strftime("%Y-%m-%d"))
    parser.add_argument('-end_date', help='Введите дату окончания отсчета(год(4 числа),месяц(2числа),день(2 числа))', default=datetime.datetime.now().strftime("%Y-%m-%d")) 
     
    args = parser.parse_args()

    initial_date = args.start_date
    final_date = args.end_date
    

    download_images_nasa_every_day(nasa_token, initial_date, final_date)  
        
if __name__ == '__main__':
    main() 
