from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time
import traceback
import os
import pyautogui

# === Función para tomar capturas de pantalla ===
def tomar_captura(nombre_archivo):
    carpeta = "C:/Users/elgej/OneDrive/Desktop/ProyectoPruebasAdivinalo/evidencias/test_adivinanza_incorrecta"
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, f"{nombre_archivo}.png")
    
    # Pequeña pausa para asegurar que la interfaz esté completamente cargada
    time.sleep(0.5)
    
    # Usar pyautogui para captura de pantalla completa
    pyautogui.screenshot(ruta)
    print(f"Captura guardada: {ruta}")
    return ruta

# === Función para manejar alertas con captura previa ===
def manejar_alerta_con_captura(texto_input=None, timeout=10):
    try:
        # Esperar a que aparezca la alerta
        print("Esperando que aparezca la alerta...")
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        print("Alerta detectada")
        
        # Dar tiempo para que la alerta se muestre completamente (crucial para la captura)
        time.sleep(1)
        
        # Tomar captura antes de interactuar con la alerta
        tomar_captura("02_alerta_nombre_visible")
        
        # Cambiar al contexto de la alerta
        alert = driver.switch_to.alert
        print(f"Texto de la alerta: '{alert.text}'")

        # Si se proporciona texto, enviarlo a la alerta
        if texto_input:
            alert.send_keys(texto_input)
            print(f"Texto enviado a la alerta: '{texto_input}'")
            
            # Captura después de escribir el texto (importante)
            time.sleep(0.5)
            tomar_captura("02b_alerta_con_texto")
        
        # Dar tiempo para que todo se vea claramente
        time.sleep(1)
        
        # Aceptar la alerta
        alert.accept()
        print("Alerta aceptada")
        
        # Esperar a que desaparezca la alerta
        WebDriverWait(driver, timeout).until_not(EC.alert_is_present())
        
        # Pequeña pausa para que se actualice la interfaz
        time.sleep(1)
        
        return True
    except TimeoutException:
        print("Error: La alerta no apareció dentro del tiempo especificado")
        return False
    except Exception as e:
        print(f"Error al manejar la alerta: {str(e)}")
        traceback.print_exc()
        return False

try:
    # Configuración del driver para Chrome usando la ruta específica
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Ruta completa al ejecutable chromedriver.exe dentro de tu carpeta
    driver_path = "C:\\Users\\elgej\\chromedriver-win64\\chromedriver.exe"
    
    # Usar la ruta específica para el ChromeDriver
    driver = webdriver.Chrome(
        service=Service(driver_path),
        options=options
    )
    
    driver.get("https://adivinalo-juego.netlify.app/")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)

    print("Esperando a que la página cargue completamente...")
    # Esperar a que el elemento esté presente y visible
    wait.until(EC.visibility_of_element_located((By.ID, "cantidadUsuarios")))
    wait.until(EC.presence_of_element_located((By.ID, "botonRegistrar")))
    print("Página inicial cargada correctamente")
    
    # Pausa para asegurar que la página esté estable
    time.sleep(1)
    tomar_captura("01_pantalla_inicial")

    # Registro del jugador
    print("Haciendo clic en botón registrar...")
    boton_registrar = wait.until(EC.element_to_be_clickable((By.ID, "botonRegistrar")))
    boton_registrar.click()
    print("Botón registrar presionado")

    print("Manejando alerta para ingresar nombre...")
    if manejar_alerta_con_captura("Dafne"):
        # Esperar a que se procese el nombre y se muestre la interfaz actualizada
        time.sleep(2)  
        
        # Tomar captura después de registrar el nombre
        tomar_captura("03_nombre_registrado")
        print("Nombre registrado correctamente")

        # Esperar a que el botón de iniciar esté presente y sea clickeable
        boton_comenzar = wait.until(EC.element_to_be_clickable((By.ID, "botonIniciar")))
        print("Botón comenzar detectado")
        
        # Iniciar juego
        print("Haciendo clic en botón comenzar...")
        boton_comenzar.click()
        print("Botón comenzar presionado")
        
        # Esperar a que se cargue la pantalla del juego
        wait.until(EC.visibility_of_element_located((By.ID, "valorUsuario")))
        wait.until(EC.visibility_of_element_located((By.ID, "verificar")))
        time.sleep(1)  # Pausa para estabilidad
        
        # Tomar captura de la pantalla del juego
        tomar_captura("04_juego_iniciado")
        print("Juego iniciado correctamente")

        # Ingresar intento
        print("Ingresando valor a adivinar...")
        input_valor = wait.until(EC.presence_of_element_located((By.ID, "valorUsuario")))
        input_valor.clear()  # Limpiar el campo por si acaso
        input_valor.send_keys("1")
        print("Valor '1' ingresado en el campo")

        # Hacer clic en el botón para verificar
        print("Haciendo clic en botón verificar...")
        boton_intentar = wait.until(EC.element_to_be_clickable((By.ID, "verificar")))
        boton_intentar.click()
        print("Botón verificar presionado")
        
        # Esperar a que se procese la respuesta
        time.sleep(1.5)

        # Verificar el resultado
        print("Verificando el resultado del intento...")
        mensaje = driver.find_element(By.ID, "mensajeJuego")
        texto_intentos = driver.find_element(By.ID, "textoIntentos")
        
        # Tomar captura después de adivinar
        time.sleep(0.5)  # Pausa para estabilidad
        tomar_captura("05_adivinanza_incorrecta")

        print(f"Mensaje mostrado: '{mensaje.text}'")
        print(f"Texto de intentos: '{texto_intentos.text}'")

        mensaje_texto = mensaje.text.lower()
        intentos_texto = texto_intentos.text.lower()

        if "correcto" in mensaje_texto and "no" not in mensaje_texto:
            print("El número elegido (1) resultó ser el número secreto. La prueba no puede verificar respuesta incorrecta.")
        else:
            assert any(p in mensaje_texto for p in [
                "mayor", "menor", "más alto", "más bajo", "incorrecto", 
                "fallaste", "inténtalo", "intenta"
            ]) or "intentos" in intentos_texto
            print("Prueba exitosa: Se muestra un mensaje al adivinar incorrectamente.")
    else:
        print("No se pudo manejar la alerta de nombre de usuario correctamente")

except Exception as e:
    print("Error durante la prueba:")
    traceback.print_exc()

finally:
    print("Finalizando prueba...")
    time.sleep(2)
    try:
        driver.quit()
        print("Prueba finalizada. Navegador cerrado.")
    except:
        print("El navegador no fue iniciado correctamente.")