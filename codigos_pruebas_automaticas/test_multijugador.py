from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time 
import traceback 
import os
from datetime import datetime
import pyautogui  # Para capturas de pantalla completa

# Crear carpeta para evidencias
nombre_prueba = "test_multijugador" 
carpeta_base = r"C:\Users\elgej\OneDrive\Desktop\ProyectoPruebasAdivinalo\evidencias"
carpeta_evidencias = os.path.join(carpeta_base, nombre_prueba)
os.makedirs(carpeta_evidencias, exist_ok=True)
print(f"Guardando capturas en: {carpeta_evidencias}")


def tomar_evidencia(nombre_archivo):
    try:
        ruta = os.path.join(carpeta_evidencias, f"{nombre_archivo}.png")
        driver.save_screenshot(ruta)
        print(f"Captura guardada: {ruta}")
        return True
    except Exception as e:
        print(f" Error al tomar captura {nombre_archivo}: {e}")
        return False

def tomar_pantalla_completa(nombre_archivo):
    try:
        ruta = os.path.join(carpeta_evidencias, f"{nombre_archivo}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(ruta)
        print(f"Captura de pantalla completa guardada: {ruta}")
    except Exception as e:
        print(f" Error al tomar captura de pantalla completa {nombre_archivo}: {e}")

def manejar_alerta(texto=None, timeout=10):
    """Maneja una alerta esperada, enviando texto si es necesario"""
    try:
        alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
        print(f"Alerta detectada: '{alert.text}'")
        
        if texto:
            alert.send_keys(texto)
            print(f"Texto enviado a la alerta: '{texto}'")
        
        time.sleep(0.5)
        tomar_pantalla_completa(f"alerta_{texto}")  # capturar alerta antes de aceptarla
        
        alert.accept()
        print("Alerta aceptada")
        
        WebDriverWait(driver, 3).until_not(EC.alert_is_present())
        print("Alerta cerrada correctamente")
        return True
    except TimeoutException:
        print("No apareció ninguna alerta en el tiempo esperado")
        return False
    except Exception as e:
        print(f"Error al manejar la alerta: {e}")
        return False

try:
    # Iniciar navegador Chrome
    service = Service("C:/Users/elgej/chromedriver-win64/chromedriver.exe")  # Ajusta si está en otra ruta
    driver = webdriver.Chrome(service=service)
    driver.get("https://adivinalo-juego.netlify.app/")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)
    print("Página cargada, esperando elementos...")
    wait.until(EC.presence_of_element_located((By.ID, "cantidadUsuarios")))
    time.sleep(1.5)
    tomar_evidencia("01_pagina_inicio")
    
    # Seleccionar 3 jugadores
    print("Configurando cantidad de jugadores: 3")
    campo_cantidad = wait.until(EC.presence_of_element_located((By.ID, "cantidadUsuarios")))
    campo_cantidad.click()
    time.sleep(0.5)
    campo_cantidad.clear()
    time.sleep(0.5)
    campo_cantidad.send_keys("3")
    time.sleep(0.5)
    tomar_evidencia("02_cantidad_jugadores")
    
    # Click en "Registrar Nombres"
    print("Haciendo clic en 'Registrar Nombres'...")
    boton_registrar = wait.until(EC.element_to_be_clickable((By.ID, "botonRegistrar")))
    boton_registrar.click()
    
    # Ingresar nombres por prompt
    nombres = ["Dafne", "Johana", "David"]
    for i, nombre in enumerate(nombres):
        print(f"Registrando jugador {i+1}: {nombre}")
        if manejar_alerta(nombre):
            time.sleep(1)
            tomar_pantalla_completa(f"03_nombre_{i+1}_{nombre}")
        else:
            print(f" Error al registrar el jugador {i+1}")
    
    time.sleep(1.5)
    
    # Click en "Comenzar"
    print("Iniciando el juego...")
    boton_comenzar = wait.until(EC.element_to_be_clickable((By.ID, "botonIniciar")))
    boton_comenzar.click()
    time.sleep(1.5)
    tomar_evidencia("04_juego_iniciado")
    
    rondas_por_jugador = 3
    total_turnos = rondas_por_jugador * len(nombres)
    turno_actual = 0
    
    print(f"Comenzando {total_turnos} turnos de juego...")
    
    while turno_actual < total_turnos:
        jugador_actual = nombres[turno_actual % len(nombres)]
        print(f"\n===== Turno {turno_actual+1}/{total_turnos} - Jugador: {jugador_actual} =====")
        
        intentos = 0
        numero = 1
        encontrado = False
        
        while intentos < 3 and numero <= 10:
            print(f"  Intento {intentos+1}: probando con número {numero}")
            
            input_valor = wait.until(EC.presence_of_element_located((By.ID, "valorUsuario")))
            input_valor.clear()
            input_valor.send_keys(str(numero))
            
            boton_intentar = wait.until(EC.element_to_be_clickable((By.ID, "verificar")))
            boton_intentar.click()
            time.sleep(1)
            
            try:
                mensaje = driver.find_element(By.ID, "mensajeJuego").text.lower()
                print(f"  Mensaje: {mensaje}")
                tomar_evidencia(f"05_turno{turno_actual+1}_intento{intentos+1}")
                
                if "correcto" in mensaje and "no" not in mensaje:
                    print(" ¡Número encontrado!")
                    encontrado = True
                    break
                if "sin intentos" in mensaje:
                    print(" Sin más intentos disponibles")
                    break
                    
                numero += 1
                intentos += 1
            except Exception as err:
                print(f"  Error al leer el mensaje: {err}")
                break
        
        time.sleep(1)
        print("  Reiniciando para el siguiente turno...")
        boton_reiniciar = wait.until(EC.element_to_be_clickable((By.ID, "reiniciar")))
        boton_reiniciar.click()
        turno_actual += 1
        time.sleep(1.5)
    
    print("\nVerificando tabla de resultados...")
    tabla_resultados = wait.until(EC.presence_of_element_located((By.ID, "tablaResultados")))
    
    if tabla_resultados.is_displayed():
        print("La tabla de resultados se muestra correctamente")
        tomar_evidencia("06_tabla_resultados")
    else:
        print("La tabla de resultados no se muestra")
        
    print("\nPrueba multijugador exitosa: jugadores completaron sus rondas y se muestra la tabla final.")

except Exception as e:
    print("\n Error durante la prueba:")
    traceback.print_exc()
    try:
        tomar_pantalla_completa("error")
    except:
        pass

finally:
    print("\nFinalizando prueba...")
    driver.quit()
    print("Prueba finalizada. Navegador cerrado.")
