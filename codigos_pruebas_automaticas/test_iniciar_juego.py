from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import os
import traceback
import time

# Crear carpeta para evidencias
ruta_carpeta = "C:\\Users\\elgej\\OneDrive\\Desktop\\ProyectoPruebasAdivinalo\\evidencias\\test_iniciar_juego"
os.makedirs(ruta_carpeta, exist_ok=True)

# Ruta al ChromeDriver
service = Service("C:/Users/elgej/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://adivinalo-juego.netlify.app/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Paso 1: Ingresar cantidad de jugadores
    input_jugadores = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    input_jugadores.clear()
    input_jugadores.send_keys("1")
    print("Cantidad de jugadores ingresada")
    driver.save_screenshot(os.path.join(ruta_carpeta, "01_cantidad_jugadores.png"))

    # Paso 2: Clic en "Registrar Nombres"
    btn_registrar = driver.find_element(By.XPATH, "//button[contains(text(), 'Registrar Nombres')]")
    btn_registrar.click()

    # Paso 3: Manejar prompt y enviar nombre
    alert = wait.until(EC.alert_is_present())
    print("Texto del prompt:", alert.text)

    # Esperar un momento para asegurar que el prompt esté visible
    time.sleep(1)

    # Captura de pantalla de toda la pantalla incluyendo la alerta del sistema
    pyautogui.screenshot(os.path.join(ruta_carpeta, "02_alerta_prompt.png"))

    # Enviar nombre al prompt y aceptar
    alert.send_keys("Dafne")
    alert.accept()
    print("Nombre del jugador registrado")
    driver.save_screenshot(os.path.join(ruta_carpeta, "03_nombre_registrado.png"))

    # Paso 4: Clic en "Comenzar"
    btn_comenzar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Comenzar')]")))
    btn_comenzar.click()
    print("Clic en botón Comenzar")
    driver.save_screenshot(os.path.join(ruta_carpeta, "04_juego_iniciado.png"))

    # Paso 5: Verificar si se muestra el nombre del jugador
    jugador_en_juego = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dafne')]")))
    assert jugador_en_juego.is_displayed()
    print("El juego ha comenzado correctamente")
    driver.save_screenshot(os.path.join(ruta_carpeta, "05_nombre_mostrado.png"))

except Exception as e:
    print("Error durante la prueba:")
    traceback.print_exc()
    driver.save_screenshot(os.path.join(ruta_carpeta, "error.png"))

finally:
    # input("Presiona ENTER para cerrar el navegador...")
    driver.quit()
