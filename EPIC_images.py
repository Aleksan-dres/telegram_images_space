import argparse
import datetime
import json
import os
import requests
from dotenv import load_dotenv


if not os.path.exists("foto_space"):
    os.mkdir("foto_space")
foto_space = () 


url_nasa_epic = "https://api.nasa.gov/EPIC/api/natural/date" 
def image_nasa_epic(url_nasa_epic,nasa_token,date): 
    payload = {
        "date": date, 
        "api_key": nasa_token 
    }
    response = requests.get(url_nasa_epic, params=payload) 
    response.raise_for_status()
    foto_epic = response.json() 
    foto_epic_image = [] 
    replacement = []  
    for i,v in enumerate (foto_epic):

        foto_epic_original = response.json()[i]['image'] 
        foto_epic_image.append(foto_epic_original) 
        foto_epic_date = response.json()[i]['date'] 
        foto_epic_date_original = foto_epic_date.split(maxsplit=1)[0] 
        replacement_original = foto_epic_date_original.replace("-","/") 
        replacement.append(replacement_original)
    
    return  foto_epic_image, replacement


def image_nasa_epic_day(nasa_token,foto_epic_image,replacement): 
    payload = {  
        "api_key": nasa_token
    } 
    for i in range(1,11):
        url_nasa_day = f"https://api.nasa.gov/EPIC/archive/natural/{replacement[i]}/png/{foto_epic_image[i]}.png"
        response = requests.get(url_nasa_day, params=payload)
        response.raise_for_status()        
    
        filename = f"foto_space/space_epic{i}.png"
      
        with open(filename, 'wb') as foto_space:
            foto_space.write(response.content)


def main(): 
    load_dotenv()
    nasa_token = os.environ["NASA_API"] 

    parser = argparse.ArgumentParser(description="Загружает фото планеты Земля из космоса")
    parser.add_argument('-date', help='Введите дату(год(4 числа),месяц(2числа),день(2 числа))', default=datetime.datetime.now().strftime("%Y-%m-%d")) 
    args = parser.parse_args()

    date = args.date
  
    foto_epic_image,replacement = image_nasa_epic(url_nasa_epic,nasa_token,date)  
    image_nasa_epic_day(nasa_token,foto_epic_image,replacement) 
        
if __name__ == '__main__':
    main()  
