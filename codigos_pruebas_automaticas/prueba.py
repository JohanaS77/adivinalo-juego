from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener la ruta del chromedriver
chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")

# Configurar el driver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Probar abriendo una página
driver.get("https://www.google.com")
