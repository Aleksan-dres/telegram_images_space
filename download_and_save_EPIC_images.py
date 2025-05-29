import requests
def download_and_save_file(url_nasa_day,path_to_file_with_photos, nasa_token):

    payload = {"api_key": nasa_token}
    response = requests.get(url_nasa_day, params=payload)
    response.raise_for_status() 
    

    with open(path_to_file_with_photos, 'wb') as foto_space:
        foto_space.write(response.content) 
