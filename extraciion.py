import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# URL de la página
url = "https://gallerosperuanos.com/Subasta.Pier-Figari/"

# Crear una sesión
session = requests.Session()

# Hacer solicitud a la página
response = session.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer datos (ejemplo: título)
    titulo = soup.find('h1')
    if titulo:
        print(f"Título: {titulo.text.strip()}")
    
    # Encontrar y descargar imágenes
    images = soup.find_all('img')
    if not os.path.exists('imagenes'):
        os.makedirs('imagenes')
    
    for index, img in enumerate(images):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(url, img_url)
            img_response = session.get(img_url, stream=True)
            if img_response.status_code == 200:
                img_name = f"imagen_{index}.jpg"
                img_path = os.path.join('imagenes', img_name)
                with open(img_path, 'wb') as f:
                    for chunk in img_response.iter_content(1024):
                        f.write(chunk)
                print(f"Imagen guardada: {img_name}")
            else:
                print(f"Error al descargar {img_url}: {img_response.status_code}")
else:
    print(f"Error al cargar la página: {response.status_code}")