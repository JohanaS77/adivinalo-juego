from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import pyautogui
import time
import os

# Ruta donde guardar la evidencia
carpeta_evidencias = r"C:\Users\elgej\OneDrive\Desktop\ProyectoPruebasAdivinalo\evidencias\test_registro_nombre"
os.makedirs(carpeta_evidencias, exist_ok=True)

def tomar_pantalla_completa(nombre_archivo):
    ruta = os.path.join(carpeta_evidencias, f"{nombre_archivo}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(ruta)
    print(f"Captura de pantalla completa guardada: {ruta}")

# Configurar el WebDriver con Chrome
service = Service("C:/Users/elgej/chromedriver-win64/chromedriver.exe")  # Ajusta si es necesario
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://adivinalo-juego.netlify.app/")
    driver.maximize_window()
    time.sleep(2)

    # Verificar campo de cantidad de jugadores
    input_jugadores = driver.find_element(By.TAG_NAME, "input")
    assert input_jugadores.is_displayed()
    print("Campo de cantidad de jugadores visible")

    # Verificar botón "Registrar Nombres"
    btn_registrar = driver.find_element(By.XPATH, "//button[contains(text(), 'Registrar Nombres')]")
    assert btn_registrar.is_displayed()
    print("Botón 'Registrar Nombres' visible")

    # Clic en "Registrar Nombres"
    btn_registrar.click()
    time.sleep(1)

    # Manejar la alerta con prompt y capturar pantalla completa
    alert = Alert(driver)
    print("Texto del prompt:", alert.text)

    alert.send_keys("Jugador1")
    time.sleep(1)
    tomar_pantalla_completa("01_alerta_prompt_nombre")  # Captura con el nombre digitado
    alert.accept()
    print("Nombre del jugador ingresado en el prompt")

finally:
    time.sleep(2)
    driver.quit()
    print("Prueba finalizada. Navegador cerrado.")
