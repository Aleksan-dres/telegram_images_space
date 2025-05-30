import requests
def download_and_save_file(url,path_to_file_with_photos,token):

    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status() 
    

    with open(path_to_file_with_photos, 'wb') as foto_space:
        foto_space.write(response.content) 
