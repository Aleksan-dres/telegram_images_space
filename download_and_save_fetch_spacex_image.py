import requests
def download_and_save_file(number, path_to_file_with_photos):
    response = requests.get(number)
    response.raise_for_status()
    
    with open(path_to_file_with_photos, 'wb') as foto_space:
        foto_space.write(response.content)
