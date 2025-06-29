import requests

# URL del endpoint
url = "https://gallerosperuanos.com/Subasta.Pier-Figari/consulta_reniec.php"

# Datos a enviar (ajusta según el Payload)
payload = {
    "dni": "41213152"  # Reemplaza con el valor real del Payload
}

# Encabezados (ajusta según los observados en Network)
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://gallerosperuanos.com/Subasta.Pier-Figari/subasta.php?action=editar&id_animal=2",
    "Origin": "https://gallerosperuanos.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# Hacer la solicitud POST
response = requests.post(url, data=payload, headers=headers)

# Verificar la respuesta
if response.status_code == 200:
    print("Respuesta:", response.text)  # Imprime el HTML devuelto
else:
    print(f"Error: {response.status_code}, {response.text}")
    
    
    