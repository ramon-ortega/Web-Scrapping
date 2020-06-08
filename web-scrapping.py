import requests
from bs4 import BeautifulSoup
import urllib

def run():
    response = requests.get('https://xkcd.com/1')
    soup = BeautifulSoup(response.content, 'html.parser')
    image_container = soup.find(id='comic')

    image_url = image_container.find('img')['src']
    image_name = image_url.split('/')[-1]
    print('Descargando la imagen {}'.format(image_name))
    urllib.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
    print(run())