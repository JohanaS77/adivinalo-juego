<h1 align="center">
  Adivínalo - Juego de Adivinanza de Números
  <img src="https://github.com/user-attachments/assets/47d228af-1fc6-4578-9421-79325ee6cf49" width="70" style="vertical-align: middle;" />
</h1>

<a href="https://adivinalo-juego.netlify.app/" target="_blank">
  
  <img src="https://github.com/user-attachments/assets/180c9412-af8a-4c71-9fcd-beb1b7b7026b" width="70" style="vertical-align: middle;"/>
  Haz clic aquí para jugar en línea
</a>

Bienvenidos al juego interactivo "¡Adivínalo!", desarrollado como proyecto para la asignatura de Pruebas de Software.

[🔼 Volver al índice](#-índice)

---

## 📋 Índice

- [ Descripción del Juego](#-descripción-del-juego)
- [Tecnologías usadas](#tecnologías-usadas)
- [ Requisitos para la Configuración del Entorno de Pruebas](#-requisitos-para-la-configuración-del-entorno-de-pruebas)
- [ Instalación y Configuración del Entorno de Pruebas](#-instalación-y-configuración-del-entorno-de-pruebas)
- [ Estructura del Proyecto](#-estructura-del-proyecto)
- [ Ejecución de Scripts de Pruebas Automatizadas](#-ejecución-de-scripts-de-pruebas-automatizadas)
- [ Manejo de Descargas](#-manejo-de-descargas)
- [ Casos de Prueba](#-casos-de-prueba)
- [ Evidencias de Pruebas Automatizadas](#-evidencias-de-pruebas-automatizadas)
- [ Recomendaciones](#-recomendaciones)
- [ Conclusiones](#-conclusiones)
- [ Desarrolladoras](#-desarrolladoras)
- [ Volver al inicio](#-tabla-de-contenidos)

---

<h2>
  Descripción del Juego
  <img src="https://github.com/user-attachments/assets/e543839e-7d97-4638-b236-326e18abb8ee" width="74" style="vertical-align: middle; margin-right: 8px;" />
  
</h2>


**¡Adivínalo!** es un juego web interactivo desarrollado como proyecto académico para la asignatura de Pruebas de Software. El objetivo principal es que los jugadores adivinen un número secreto entre 1 y 10, en un entorno amigable y competitivo.

###  ¿Cómo se juega?

- **Selección de jugadores:** Al iniciar, se solicita la cantidad de participantes, permitiendo una experiencia multijugador.
- **Registro de nombres:** Cada jugador ingresa su nombre, personalizando la partida.
- **Rondas y turnos:** El juego consta de 3 rondas, donde cada jugador tiene su turno para adivinar el número secreto.
- **Intentos limitados:** En cada turno, el jugador dispone de 3 intentos para acertar el número.
- **Feedback inmediato:** Después de cada intento, se proporciona retroalimentación indicando si el número ingresado es correcto o no.
- **Resultados finales:** Al concluir las rondas, se presenta una tabla con los resultados de cada jugador, destacando al ganador.

###  Objetivo del juego

El propósito es fomentar la lógica y la intuición de los jugadores al intentar adivinar el número secreto en el menor número de intentos posibles, promoviendo la competencia sana y el entretenimiento.

👉 Puedes jugarlo en línea aquí: [¡Probar Adivínalo!](https://adivinalo-juego.netlify.app/)

[🔼 Volver al índice](#-índice)

---

## Tecnologías usadas <img src="https://github.com/user-attachments/assets/8a1d8ac7-a2f1-4ba8-a216-2806de1e70bd" width="72" style="vertical-align: middle;" />



Este proyecto combina desarrollo web y pruebas automatizadas. Las tecnologías empleadas fueron:

- **HTML** – Para la estructura del juego.
- **CSS** – Para los estilos visuales.
- **JavaScript** – Para la lógica interactiva del juego.
- **[Selenium](https://www.selenium.dev/)** – Para automatizar las pruebas de navegación y funcionalidades.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)** – Para capturar evidencias visuales de cada prueba.
- **GitHub** – Para el control de versiones y publicación del repositorio.

[🔼 Volver al índice](#-índice)

---

## Requisitos para la Configuración del Entorno de Pruebas <img src="https://github.com/user-attachments/assets/9702dd0e-76e2-425d-9efc-94061c93739f" width="92" style="vertical-align: middle;" />


Para poder ejecutar correctamente las pruebas automatizadas desarrolladas para el juego **¡Adivínalo!**, es necesario contar con los siguientes elementos instalados y configurados en el entorno local:

### 🖥 Software y herramientas necesarias

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

<h2>
  Instalación y Configuración del Entorno de Pruebas
  <img src="https://github.com/user-attachments/assets/4675b1d5-bcc5-4ddf-a2d2-82b283ecdf9c" width="44" style="vertical-align: middle;" />
</h2>



Este proyecto incluye un conjunto de pruebas automatizadas desarrolladas con Selenium WebDriver para validar la funcionalidad del juego "¡Adivínalo!". La siguiente documentación describe los requisitos y procedimientos necesarios para configurar el entorno de testing.

###  Requisitos del Sistema

**Python 3.12+**  
Verificar la instalación actual del intérprete:
```bash
python --version
```

###  Dependencias del Proyecto

Instalar las librerías requeridas mediante pip:

```bash
pip install selenium pyautogui
```

**Selenium**: Framework de automatización web para el control programático del navegador  
**PyAutoGUI**: Librería para automatización de GUI y captura de screenshots durante la ejecución de pruebas

###  Configuración de WebDriver

#### Chrome (Recomendado)
Descargar ChromeDriver compatible con la versión instalada del navegador Chrome. El ejecutable debe ubicarse en el directorio del proyecto o agregarse al PATH del sistema.

👉 [Descargar ChromeDriver](https://sites.google.com/chromium.org/driver/)

#### Firefox (Alternativo)
Para entornos que requieran Firefox, descargar GeckoDriver y configurar las variables de entorno correspondientes.

👉 [Descargar GeckoDriver](https://github.com/mozilla/geckodriver/releases)

###  Validación de la Configuración

Ejecutar cualquier script de prueba para verificar la correcta configuración del entorno:

```bash
python test_multijugador.py
```

###  Estructura de Archivos de Prueba

Los scripts de testing se encuentran organizados por funcionalidad y siguen las convenciones de nomenclatura `test_*.py` para facilitar su identificación y ejecución.

[🔼 Volver al índice](#índice)

---

<h2>
  Estructura del Proyecto
  <img src="https://github.com/user-attachments/assets/5fb60d18-40d0-491c-8945-3113559ff4cf" width="108" style="vertical-align: middle;" />
</h2>

A continuación se presenta la estructura del repositorio publicado en GitHub, organizada para facilitar la comprensión de los diferentes componentes del proyecto:

```
📁 Evidencias 1
📁 Evidencias 2
📁 codigos_pruebas_automatizadas
📁 img
📄 app.js
📄 index.html
📄 style.css
```

###  Descripción de Directorios y Archivos

- **`Evidencias 1` y `Evidencias 2`**: Contienen capturas de pantalla tomadas durante la ejecución de las pruebas automáticas, documentando los resultados obtenidos en cada caso de prueba.

- **`codigos_pruebas_automatizadas`**: Carpeta que almacena los archivos `.py` con los scripts de prueba realizados con Selenium y PyAutoGUI para validar el funcionamiento del juego.

- **`img`**: Almacena las imágenes utilizadas en el juego, incluyendo recursos gráficos como las imágenes que aparecen al ganar o perder una partida.

- **`app.js`**: Archivo JavaScript que contiene toda la lógica del juego, incluyendo la generación de números aleatorios, validación de respuestas y manejo de eventos.

- **`index.html`**: Estructura HTML principal de la aplicación web que define la interfaz de usuario del juego *¡Adivínalo!*.

- **`style.css`**: Hoja de estilos CSS que define la apariencia visual y el diseño responsivo de la aplicación.

[🔼 Volver al índice](#-índice)

---

<h2>
  Ejecución de Scripts de Pruebas Automáticas
  <img src="https://github.com/user-attachments/assets/3a96506f-6b07-41c2-b1f7-58fa6e3f4c13" width="98" style="vertical-align: middle;" />
</h2>

Para ejecutar las pruebas automatizadas del juego *¡Adivínalo!*, se debe seguir el siguiente procedimiento:

### 📝 Procedimiento de Ejecución

1. **Verificar prerrequisitos**: Confirmar que se encuentren instaladas todas las herramientas necesarias descritas en el apartado [Instalación y Configuración del Entorno de Pruebas](#-instalación-y-configuración-del-entorno-de-pruebas).

2. **Navegar al directorio de pruebas**: Ubicarse dentro de la carpeta `codigos_pruebas_automatizadas` desde la terminal o línea de comandos.

3. **Ejecutar los scripts de prueba**: Utilizar el siguiente comando para ejecutar cualquiera de los archivos de prueba:
   ```bash
   python nombre_del_script.py
   ```

   **Ejemplo de ejecución:**
   ```bash
   python test_multijugador.py
   ```

###  Consideraciones Importantes

- **Navegador requerido**: Las pruebas están desarrolladas específicamente para ejecutarse sobre el navegador **Google Chrome**.

- **Configuración de ChromeDriver**: El archivo `chromedriver.exe` debe estar ubicado en la misma carpeta que los scripts de prueba, o correctamente configurado en la variable de entorno PATH del sistema.

- **Ejecución en primer plano**: Algunos scripts requieren interacción visual directa con la interfaz, por lo que no deben ejecutarse en segundo plano mientras se utiliza el equipo para otras actividades.

- **Generación de evidencias**: Las pruebas capturan screenshots automáticamente durante su ejecución. Estas imágenes se almacenan en las carpetas `Evidencias 1` y `Evidencias 2`, organizadas según el nombre y tipo de cada prueba realizada.

[🔼 Volver al índice](#-índice)

---

<h2>
  Manejo de Descargas
  <img src="https://github.com/user-attachments/assets/bc8034a5-37ee-4c1e-9a6f-9373f08af0fd" width="78" style="vertical-align: middle;" />
</h2>



Durante la ejecución de los scripts de pruebas automatizadas, se generan automáticamente capturas de pantalla como evidencia del comportamiento de la aplicación. Estas imágenes permiten verificar visualmente los resultados de cada prueba realizada.

Las capturas están organizadas en dos carpetas principales dentro del repositorio: **Evidencias 1** y **Evidencias 2**. Cada una de estas contiene subcarpetas que corresponden a los diferentes scripts de prueba utilizados.

- **Evidencias 1**: Contiene las pruebas iniciales del juego.
  - `abrir_juego/`
  - `test_adivinanza_correcta/`
  - `test_adivinanza_incorrecta/`
  - `test_elementos_inicio/`

- **Evidencias 2**: Agrupa pruebas más avanzadas o con mayor interacción.
  - `test_iniciar_juego/`
  - `test_multijugador/`
  - `test_registro_nombre/`
  - `test_titulo_juego/`

Dentro de cada subcarpeta se encuentran las imágenes (pantallazos) capturados durante la ejecución de las pruebas. Cada nombre de archivo refleja el momento exacto de la prueba, por ejemplo: `ronda1_dafne.png` o `resultado_juego.png`.

Estas carpetas están disponibles públicamente en el repositorio, por lo tanto, cualquier usuario puede acceder a ellas para consultar las evidencias y confirmar que las pruebas automatizadas se ejecutaron correctamente.

[🔼 Volver al índice](#-índice)

---

<h2>
  Casos de Prueba
  <img src="https://github.com/user-attachments/assets/a5c127be-b90a-4a99-81ee-9d085d92d037" width="78" style="vertical-align: middle;" />
</h2>




A continuación, se describen los casos de prueba implementados para verificar el correcto funcionamiento del juego en diferentes escenarios. Estas pruebas fueron automatizadas utilizando Selenium, y se desarrollaron con base en los comportamientos esperados del juego.

Cada script evalúa un aspecto específico de la funcionalidad, y sus resultados fueron respaldados con capturas de pantalla que se encuentran en las carpetas de evidencias.

| Nombre del Script                | Descripción                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **abrir_juego.py**               | Verifica que el juego cargue correctamente y que la página se abra sin errores. |
| **test_titulo_juego.py**        | Comprueba que el título del juego se muestre correctamente al cargar la página. |
| **test_elementos_inicio.py**    | Evalúa que todos los elementos iniciales (botón, input, título) estén visibles. |
| **test_iniciar_juego.py**       | Simula la interacción del usuario para iniciar el juego tras ingresar su nombre. |
| **test_registro_nombre.py**     | Verifica que se registre correctamente el nombre ingresado por el jugador. |
| **test_adivinanza_correcta.py** | Simula una adivinanza correcta y valida que se muestre el mensaje de acierto. |
| **test_adivinanza_incorrecta.py**| Simula una adivinanza incorrecta y valida que se muestre el mensaje de error. |
| **test_multijugador.py**        | Ejecuta una sesión de juego en modo multijugador, con múltiples rondas y validación de resultados. |

Cada uno de estos scripts fue estructurado para ejecutarse de forma autónoma y reproducible, asegurando así la confiabilidad de las pruebas en diferentes ejecuciones.

[🔼 Volver al índice](#-índice)

---

<h2>
  Recomendaciones
  <img src="https://github.com/user-attachments/assets/56c9fb71-68af-45d6-8e15-de3ca8e26266" width="98" style="vertical-align: middle;" />
</h2>


Antes de ejecutar los scripts de prueba automatizada, se sugieren las siguientes recomendaciones para evitar errores y asegurar una correcta ejecución del entorno:

-  **Verificar la compatibilidad del navegador y del driver**  
  Asegúrate de que la versión del navegador (Google Chrome o Firefox) coincida con la del driver correspondiente (ChromeDriver o GeckoDriver).

-  **Ejecutar cada script en una sesión limpia**  
  Para evitar interferencias entre pruebas, se recomienda cerrar el navegador completamente antes de ejecutar un nuevo script.

-  **Mantener una estructura organizada**  
  Las capturas de pantalla se guardan automáticamente en carpetas según el nombre de la prueba. Se sugiere no mover estas carpetas para mantener la organización.

-  **Supervisar los scripts al ejecutarse**  
  Como las pruebas no se ejecutan en modo headless, es útil observar el flujo en pantalla para detectar visualmente posibles errores o fallas en la automatización.

-  **Realizar pruebas en diferentes resoluciones**  
  Se recomienda probar en distintas resoluciones de pantalla para asegurar que los elementos del juego se muestren correctamente.

-  **Evitar interacciones durante la ejecución**  
  No mover el mouse ni interactuar con el teclado mientras se ejecutan las pruebas, ya que esto puede alterar los resultados, especialmente cuando se usan librerías como PyAutoGUI.

Estas sugerencias están basadas en la experiencia obtenida durante el desarrollo de este proyecto, y buscan facilitar su uso a futuros usuarios o desarrolladores.

[🔼 Volver al índice](#-índice)

---

<h2>
  Conclusiones
  <img src="https://github.com/user-attachments/assets/42e50dd0-3e79-40a5-980f-0eeee5e23a85" width="58" style="vertical-align: middle;" />
</h2>



El desarrollo y la implementación de pruebas automatizadas para el juego **Adivínalo** nos permitió afianzar conocimientos fundamentales sobre automatización, control de calidad y herramientas de desarrollo web.

Entre los principales aprendizajes y logros, destacamos los siguientes:

- ✔️ Aprendimos a utilizar **Selenium** para controlar navegadores y automatizar acciones como clics, entradas de texto y validación de elementos en pantalla.
- ✔️ Implementamos **PyAutoGUI** para la captura automática de evidencias, permitiendo documentar de manera visual los resultados de cada prueba.
- ✔️ Logramos ejecutar pruebas exitosas tanto en modo individual como en modo multijugador, simulando distintos escenarios del juego.
- ✔️ Estructuramos nuestro proyecto de forma clara, facilitando la navegación y comprensión del código fuente, las evidencias y la documentación.
- ✔️ Mejoramos nuestras habilidades de trabajo colaborativo, dividiendo tareas y documentando cada etapa del proyecto.

En general, este proyecto representó una experiencia enriquecedora que nos permitió aplicar conocimientos teóricos en un caso práctico y real, integrando programación web, automatización y documentación técnica.

[🔼 Volver al índice](#-índice)

---

## Desarrolladoras <img src="https://github.com/user-attachments/assets/66023c24-8f7e-4874-b2ba-d7eb7c1daf00" width="80" style="vertical-align: middle;" />



Este proyecto fue desarrollado por Dafne Julieth Cortés y Johana Jazmín Saavedra, estudiantes de tercer semestre en Técnica profesional en programación de aplicaciones de software de la Fundación Universitaria Compensar. Con una participación activa en la creación del juego, diseño de pruebas automatizadas, documentación y presentación del proyecto final.

<div align="center">
  <table>
    <tr>
      <td align="center" style="padding-right: 60px;">
        <img src="https://github.com/user-attachments/assets/9595bb09-c5cc-4ce8-8a1a-e6bfc3ffd378" width="120" style="border: none;"><br/>
        <strong>Dafne Julieth Cortés</strong>
      </td>
      <td align="center" style="padding-left: 60px;">
        <img src="https://github.com/user-attachments/assets/96a0990c-a533-42c2-9fa2-7224c4eca021" width="120" style="border: none;"><br/>
        <strong>Johana Jazmín Saavedra</strong>
      </td>
    </tr>
  </table>
</div>

[🔼 Volver al índice](#-índice)

---











