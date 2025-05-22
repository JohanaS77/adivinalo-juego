from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import os

# Ruta donde guardar la captura
carpeta_evidencias = r"C:\Users\elgej\OneDrive\Desktop\ProyectoPruebasAdivinalo\evidencias\test_titulo_juego"
os.makedirs(carpeta_evidencias, exist_ok=True)

def tomar_pantalla_completa(nombre_archivo):
    ruta = os.path.join(carpeta_evidencias, f"{nombre_archivo}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(ruta)
    print(f"Captura de pantalla completa guardada: {ruta}")

# Configurar Chrome
options = Options()
options.headless = False  # Si quieres ejecutar en segundo plano, cambia a True

# Ruta al ChromeDriver
service = Service(executable_path=r"C:\Users\elgej\chromedriver-win64\chromedriver.exe")  # Ajusta si es necesario

# Iniciar navegador
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://adivinalo-juego.netlify.app/")
driver.maximize_window()
time.sleep(2)  # Espera para que cargue bien la página

# Captura de pantalla
tomar_pantalla_completa("01_titulo_pagina")

# Obtener y verificar el título
titulo = driver.title
print("Título de la página:", titulo)

titulo_esperado = "¡Adivínalo!"
if titulo == titulo_esperado:
    print("Título correcto.")
else:
    print("Título incorrecto.")

# Cerrar el navegador
driver.quit()

