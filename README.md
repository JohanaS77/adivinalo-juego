# 🎮 Adivínalo - Juego de Adivinanza de Números

🎯 [Haz clic aquí para jugar en línea](https://adivinalo-juego.netlify.app/)

Bienvenidos al juego interactivo "¡Adivínalo!", desarrollado como proyecto para la asignatura de Pruebas de Software.

[🔼 Volver al índice](#-índice)

---

## 📋 Índice

- [🎮 Descripción del Juego](#-descripción-del-juego)
- [Tecnologías usadas](#tecnologías-usadas)
- [📌 Requisitos para la Configuración del Entorno de Pruebas](#-requisitos-para-la-configuración-del-entorno-de-pruebas)
- [🧪 Instalación y Configuración del Entorno de Pruebas](#-instalación-y-configuración-del-entorno-de-pruebas)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🚀 Ejecución de Pruebas](#-ejecución-de-pruebas)
- [📊 Reportes](#-reportes)
- [📥 Manejo de Descargas](#-manejo-de-descargas)
- [🧪 Casos de Prueba](#-casos-de-prueba)
- [🖼️ Evidencias de Pruebas](#-evidencias-de-pruebas)
- [💡 Recomendaciones](#-recomendaciones)
- [🧾 Conclusiones](#-conclusiones)
- [👩‍💻 Desarrolladoras](#-desarrolladoras)
- [🔝 Volver al inicio](#-tabla-de-contenidos)

---

## 🎮 Descripción del Juego

**¡Adivínalo!** es un juego web interactivo desarrollado como proyecto académico para la asignatura de Pruebas de Software. El objetivo principal es que los jugadores adivinen un número secreto entre 1 y 10, en un entorno amigable y competitivo.

### 🧠 ¿Cómo se juega?

- **Selección de jugadores:** Al iniciar, se solicita la cantidad de participantes, permitiendo una experiencia multijugador.
- **Registro de nombres:** Cada jugador ingresa su nombre, personalizando la partida.
- **Rondas y turnos:** El juego consta de 3 rondas, donde cada jugador tiene su turno para adivinar el número secreto.
- **Intentos limitados:** En cada turno, el jugador dispone de 3 intentos para acertar el número.
- **Feedback inmediato:** Después de cada intento, se proporciona retroalimentación indicando si el número ingresado es correcto o no.
- **Resultados finales:** Al concluir las rondas, se presenta una tabla con los resultados de cada jugador, destacando al ganador.

### 🎯 Objetivo del juego

El propósito es fomentar la lógica y la intuición de los jugadores al intentar adivinar el número secreto en el menor número de intentos posibles, promoviendo la competencia sana y el entretenimiento.

👉 Puedes jugarlo en línea aquí: [¡Probar Adivínalo!](https://adivinalo-juego.netlify.app/)

[🔼 Volver al índice](#-índice)

---

## ⚙️ Tecnologías usadas

Este proyecto combina desarrollo web y pruebas automatizadas. Las tecnologías empleadas fueron:

- **HTML** – Para la estructura del juego.
- **CSS** – Para los estilos visuales.
- **JavaScript** – Para la lógica interactiva del juego.
- **[Selenium](https://www.selenium.dev/)** – Para automatizar las pruebas de navegación y funcionalidades.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)** – Para capturar evidencias visuales de cada prueba.
- **GitHub** – Para el control de versiones y publicación del repositorio.

[🔼 Volver al índice](#-índice)

---

## 🧪 Requisitos para la Configuración del entorno de Pruebas

Para poder ejecutar correctamente las pruebas automatizadas desarrolladas para el juego **¡Adivínalo!**, es necesario contar con los siguientes elementos instalados y configurados en el entorno local:

### 🖥️ Software y herramientas necesarias

- **Python 3.12 o superior**  
  Lenguaje de programación utilizado para desarrollar los scripts de prueba.

- **Google Chrome**  
  Navegador utilizado en las pruebas.

- **ChromeDriver**  
  Driver compatible con la versión de Google Chrome instalada.  
  Es indispensable que el archivo `chromedriver.exe` esté en la misma carpeta que los scripts o agregado al PATH del sistema.  
  👉 [Descargar ChromeDriver](https://sites.google.com/chromium.org/driver/)

- **Selenium**  
  Biblioteca que permite controlar el navegador de forma automática.  
  Se instala con el siguiente comando:  
  ```bash
  pip install selenium
  ```

- **PyAutoGUI**  
  Librería utilizada para capturar pantallazos durante la ejecución de las pruebas.  
  Se instala con:
  ```bash
  pip install pyautogui
  
  ```

- **Extensión de Firefox y Geckodriver** *(opcional)*  
  Aunque el proyecto se ejecutó principalmente con Google Chrome, también es posible utilizar Firefox instalando:
  * El navegador **Mozilla Firefox**
  * El controlador **Geckodriver**, compatible con la versión del navegador.  
  👉 [Descargar Geckodriver](https://github.com/mozilla/geckodriver/releases)

[🔼 Volver al índice](#-índice)

---

## 💾 Instalación y Configuración del Entorno de Pruebas

Este proyecto incluye un conjunto de pruebas automatizadas desarrolladas con Selenium WebDriver para validar la funcionalidad del juego "¡Adivínalo!". La siguiente documentación describe los requisitos y procedimientos necesarios para configurar el entorno de testing.

### 🔧 Requisitos del Sistema

**Python 3.12+**  
Verificar la instalación actual del intérprete:
```bash
python --version
```

### 📦 Dependencias del Proyecto

Instalar las librerías requeridas mediante pip:

```bash
pip install selenium pyautogui
```

**Selenium**: Framework de automatización web para el control programático del navegador  
**PyAutoGUI**: Librería para automatización de GUI y captura de screenshots durante la ejecución de pruebas

### 🌐 Configuración de WebDriver

#### Chrome (Recomendado)
Descargar ChromeDriver compatible con la versión instalada del navegador Chrome. El ejecutable debe ubicarse en el directorio del proyecto o agregarse al PATH del sistema.

👉 [Descargar ChromeDriver](https://sites.google.com/chromium.org/driver/)

#### Firefox (Alternativo)
Para entornos que requieran Firefox, descargar GeckoDriver y configurar las variables de entorno correspondientes.

👉 [Descargar GeckoDriver](https://github.com/mozilla/geckodriver/releases)

### ✅ Validación de la Configuración

Ejecutar cualquier script de prueba para verificar la correcta configuración del entorno:

```bash
python test_multijugador.py
```

### 📁 Estructura de Archivos de Prueba

Los scripts de testing se encuentran organizados por funcionalidad y siguen las convenciones de nomenclatura `test_*.py` para facilitar su identificación y ejecución.

[🔼 Volver al índice](#índice)

---

## 📁 Estructura del proyecto

├── index.html
├── style.css
├── app.js
├── img/
│ ├── ia.png
│ ├── ia2.png
│ └── ...



---

## ✅ Pruebas automáticas

El proyecto incluye tres scripts de pruebas automáticas con Selenium + PyAutoGUI:

- `test_multijugador.py`: prueba completa con 3 jugadores, 3 rondas, y captura de pantalla por intento.
- `test_registro_nombre.py`: prueba del prompt de registro de nombre.
- `test_titulo_juego.py`: verifica que el título del sitio sea “¡Adivínalo!”.

Los archivos están organizados en una carpeta `pruebas-automaticas/`.

👉 [Ver pruebas en GitHub](./pruebas-automaticas)

---

## 🖼️ Evidencias

Las capturas de pantalla generadas automáticamente están guardadas en la carpeta:

Las evidencias generadas automáticamente están guardadas en la carpeta `evidencias/test_multijugador/` dentro del proyecto.


Estas evidencias respaldan cada prueba automatizada con imágenes reales de ejecución.

---

## 🔄 Volver al inicio

[⬆️ Volver al índice](#-índice)





