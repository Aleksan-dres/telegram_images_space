import requests 
def download_and_save_file(foto_url, path_to_file_with_photos):
    response = requests.get(foto_url)
    response.raise_for_status()
    
    with open(path_to_file_with_photos, 'wb') as foto_space:
        foto_space.write(response.content)
