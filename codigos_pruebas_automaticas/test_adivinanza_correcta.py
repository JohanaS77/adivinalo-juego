import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback
import re
import os

# === CONFIGURACIÓN PARA GUARDAR CAPTURAS ===
evidencias_path = r"C:\Users\elgej\OneDrive\Desktop\ProyectoPruebasAdivinalo\evidencias\test_adivinanza_correcta"
os.makedirs(evidencias_path, exist_ok=True)

# Función para tomar captura de pantalla numerada (con selenium)
def tomar_captura(nombre):
    driver.save_screenshot(os.path.join(evidencias_path, f"{nombre}.png"))

# Función para capturar con pyautogui (alertas u otras ventanas del sistema)
def captura_alerta(nombre):
    ruta = os.path.join(evidencias_path, f"{nombre}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(ruta)

# === FUNCIÓN AUXILIAR ===
def intentos_agotados(mensaje):
    return "sin intentos" in mensaje.lower()

# === CONFIGURACIÓN DEL DRIVER ===
options = Options()
options.headless = False

service = Service("C:\\Users\\elgej\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# === INICIO DE PRUEBA ===
try:
    print("Abriendo juego...")
    driver.get("https://adivinalo-juego.netlify.app/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "cantidadUsuarios")))
    tomar_captura("01_inicio")

    print("Haciendo clic en 'Registrar'...")
    boton_registrar = driver.find_element(By.ID, "botonRegistrar")
    boton_registrar.click()

    print("Esperando alerta del nombre...")
    wait.until(EC.alert_is_present())
    time.sleep(1)  # dar tiempo a que se vea la alerta
    captura_alerta("02_alerta_nombre")  # captura del escritorio
    alert = driver.switch_to.alert
    alert.send_keys("Johana")
    alert.accept()
    tomar_captura("03_nombre_registrado")

    print("Iniciando juego...")
    boton_comenzar = driver.find_element(By.ID, "botonIniciar")
    boton_comenzar.click()
    tomar_captura("04_juego_iniciado")

    # Adivinar número secreto
    numero_encontrado = False
    intentos_restantes = 3

    for numero_intento in range(1, 10):
        if intentos_restantes <= 0:
            print("Reiniciando juego por intentos agotados...")
            boton_reiniciar = driver.find_element(By.ID, "reiniciar")
            boton_reiniciar.click()
            time.sleep(2)
            intentos_restantes = 3

        input_valor = wait.until(EC.presence_of_element_located((By.ID, "valorUsuario")))
        input_valor.clear()
        input_valor.send_keys(str(numero_intento))

        boton_intentar = driver.find_element(By.ID, "verificar")
        boton_intentar.click()

        time.sleep(2)
        mensaje = driver.find_element(By.ID, "mensajeJuego").text.lower()
        tomar_captura(f"intento_{numero_intento}")

        print(f"Intento con número {numero_intento}: '{mensaje}'")

        if "correcto" in mensaje:
            print(f"Número secreto encontrado: {numero_intento}")
            numero_encontrado = True

            imagen = driver.find_element(By.ID, "imagenJuego")
            src_imagen = imagen.get_attribute("src")
            assert "ia3.png" in src_imagen, f"La imagen no cambió a ia3.png. Actual: {src_imagen}"

            assert re.search(r'\+\d+ puntos?', mensaje), "No se muestran los puntos obtenidos en el mensaje"
            assert not boton_intentar.is_enabled(), "El botón 'Intentar' debería estar deshabilitado tras acertar"
            boton_reiniciar = driver.find_element(By.ID, "reiniciar")
            assert boton_reiniciar.is_enabled(), "El botón 'Siguiente Turno' debería estar habilitado tras acertar"

            tomar_captura("05_numero_encontrado")
            print("Prueba exitosa: El número secreto fue adivinado correctamente.")
            break
        elif intentos_agotados(mensaje):
            print(f"Se agotaron los intentos al probar el número {numero_intento}.")
            intentos_restantes = 0
        else:
            intentos_restantes -= 1

    if not numero_encontrado:
        raise Exception("No se pudo encontrar el número secreto después de probar todos los números del 1 al 10")

except Exception as e:
    print("Error durante la prueba:")
    traceback.print_exc()

finally:
    print("Cerrando navegador...")
    time.sleep(3)
    driver.quit()
