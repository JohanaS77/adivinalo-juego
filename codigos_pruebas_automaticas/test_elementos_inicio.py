from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import traceback

# Función para capturar pantalla
def tomar_captura(nombre_archivo):
    carpeta = "C:/Users/elgej/OneDrive/Desktop/ProyectoPruebasAdivinalo/evidencias/test_elementos_inicio"
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{nombre_archivo}.png")
    driver.save_screenshot(ruta)
    print(f"Captura guardada: {ruta}")

# Ruta al ChromeDriver (ajusta si está en otra carpeta)
service = Service("C:/Users/elgej/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://adivinalo-juego.netlify.app/")
    wait = WebDriverWait(driver, 10)

    print("\n Verificando elementos de la pantalla de inicio...")

    # Verificar campo para número de jugadores
    campo_jugadores = wait.until(EC.presence_of_element_located((By.ID, "cantidadUsuarios")))
    assert campo_jugadores.is_displayed(), "El campo para número de jugadores no está visible"
    print("Campo para número de jugadores visible")

    # Verificar botón "Registrar Nombres"
    btn_registrar = driver.find_element(By.ID, "botonRegistrar")
    assert btn_registrar.is_displayed(), "El botón 'Registrar Nombres' no está visible"
    print("Botón 'Registrar Nombres' visible")

    # Verificar botón "Comenzar"
    btn_comenzar = driver.find_element(By.ID, "botonIniciar")
    assert btn_comenzar.is_displayed(), "El botón 'Comenzar' no está visible"
    print("Botón 'Comenzar' visible")

    # Captura de pantalla final
    tomar_captura("01_elementos_visibles")

    print("Prueba exitosa: Todos los elementos esperados están visibles.")

except Exception as e:
    print("Error durante la prueba:")
    traceback.print_exc()

finally:
    driver.quit()
