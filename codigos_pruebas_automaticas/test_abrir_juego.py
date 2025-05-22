from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import traceback

# Cargar el archivo .env
load_dotenv()

# Obtener la ruta del chromedriver
chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")

# Usar la ruta en Selenium
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Aquí puedes continuar con tu prueba...


# Configuración
options = Options()
options.headless = False  # Mostrar el navegador

# Ruta al chromedriver
service = Service(executable_path="C:\\Users\\elgej\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Ruta para guardar la evidencia
carpeta = r"C:\Users\elgej\OneDrive\Desktop\ProyectoPruebasAdivinalo\evidencias\abrir_juego"
os.makedirs(carpeta, exist_ok=True)

try:
    driver.get("https://adivinalo-juego.netlify.app/")

    # Esperar a que se cargue un elemento visible y confiable
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "botonIniciar"))
    )

    # Captura de pantalla
    ruta_captura = os.path.join(carpeta, "pantalla_inicio.png")
    driver.save_screenshot(ruta_captura)
    print(f"Evidencia guardada: {ruta_captura}")

except Exception as e:
    print("Error durante la prueba:")
    traceback.print_exc()

finally:
    driver.quit()
