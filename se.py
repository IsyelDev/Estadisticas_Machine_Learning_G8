from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://gallerosperuanos.com/Subasta.Pier-Figari/subasta.php?action=editar&id_animal=4")
time.sleep(5)  # Espera a que cargue
print("Revisa la pestaña 'Network' mientras el navegador está abierto.")
driver.quit()