let jugadores = [];
let puntuaciones = [];
let jugadorActual = 0;
let numeroSecreto;
let intentos = 3;
let intentosMaximos = 3;
let rondaActual = 1;
let rondaTotal = 3;

const pantallaInicio = document.getElementById("pantallaInicio");
const pantallaJuego = document.querySelector(".container");
const pantallaResultados = document.getElementById("pantallaResultados");
const cantidadUsuarios = document.getElementById("cantidadUsuarios");
const botonRegistrar = document.getElementById("botonRegistrar");
const botonIniciar = document.getElementById("botonIniciar");

const valorUsuario = document.getElementById("valorUsuario");
const verificar = document.getElementById("verificar");
const reiniciar = document.getElementById("reiniciar");
const finalizarJuego = document.getElementById("finalizarJuego");
const volverAJugar = document.getElementById("volverAJugar");

const mensajeJuego = document.getElementById("mensajeJuego");
const textoIntentos = document.getElementById("textoIntentos");
const nombreJugador = document.getElementById("nombreJugador");
const imagenJuego = document.getElementById("imagenJuego");
const numeroRonda = document.getElementById("numeroRonda");

botonRegistrar.addEventListener("click", () => {
    const cantidad = parseInt(cantidadUsuarios.value);
    if (isNaN(cantidad) || cantidad < 1 || cantidad > 10) {
        alert("Por favor, ingresa un número válido entre 1 y 10");
        return;
    }
    
    jugadores = [];
    puntuaciones = [];

    for (let i = 0; i < cantidad; i++) {
        const nombre = prompt(`Nombre del Jugador ${i + 1}:`);
        if (nombre && nombre.trim() !== "") {
            jugadores.push(nombre.trim());
        } else {
            jugadores.push(`Jugador ${i + 1}`);
        }
        // Inicializamos con arrays para cada jugador
        puntuaciones.push(new Array(rondaTotal).fill(null));
    }

    if (jugadores.length > 0) {
        botonIniciar.disabled = false;        
    }
});

botonIniciar.addEventListener("click", () => {
    pantallaInicio.style.display = "none";
    pantallaJuego.style.display = "flex";
    rondaActual = 1;
    jugadorActual = 0;
    iniciarJuego();
});

function iniciarJuego() {
    numeroSecreto = Math.floor(Math.random() * 10) + 1;
    intentos = intentosMaximos;
    imagenJuego.src = './img/ia.png';
    mensajeJuego.textContent = "Indica un número del 1 al 10";
    textoIntentos.textContent = `(Tienes ${intentos} intentos)`;
    nombreJugador.textContent = `Turno de: ${jugadores[jugadorActual]}`;
    numeroRonda.textContent = `Ronda ${rondaActual} de ${rondaTotal}`;
    reiniciar.disabled = true;
    verificar.disabled = false;
    limpiarCaja();
    console.log("Número Secreto:", numeroSecreto); 
}

function limpiarCaja() {
    valorUsuario.value = '';
    valorUsuario.focus();
}

verificar.addEventListener("click", () => {
    const valor = parseInt(valorUsuario.value);

    if (isNaN(valor) || valor < 1 || valor > 10) {
        mensajeJuego.textContent = "Por favor, introduce un número entre 1 y 10";
        imagenJuego.src = './img/ia.png';
        limpiarCaja();
        return;
    }

    if (valor === numeroSecreto) {
        // Si acierta, gana puntos según los intentos restantes
        puntuaciones[jugadorActual][rondaActual - 1] = intentos;
        mensajeJuego.innerHTML = `¡Correcto, ${jugadores[jugadorActual]}!<br>
        Adivinaste en ${intentosMaximos - intentos + 1} intento(s).<br>
        +${intentos} punto(s)`;
        textoIntentos.textContent = "";
        imagenJuego.src = './img/ia3.png';
        verificar.disabled = true;
        reiniciar.disabled = false;
    } else {
        intentos--;
        if (intentos > 0) {
            mensajeJuego.textContent = valor > numeroSecreto ? "El número es menor." : "El número es mayor.";
            textoIntentos.textContent = `(Te quedan ${intentos} intento${intentos > 1 ? 's' : ''})`;
            imagenJuego.src = valor > numeroSecreto ? './img/ia5.png' : './img/ia4.png';
        } else {
            mensajeJuego.textContent = `¡Sin intentos! El número era ${numeroSecreto}.`;
            textoIntentos.textContent = "";
            imagenJuego.src = './img/ia2.png';
            verificar.disabled = true;
            reiniciar.disabled = false;

            // Si se queda sin intentos, obtiene 0 puntos
            puntuaciones[jugadorActual][rondaActual - 1] = 0;
        }
    }

    limpiarCaja();
});

reiniciar.addEventListener("click", () => {
    jugadorActual = (jugadorActual + 1) % jugadores.length;
    if (jugadorActual === 0) {
        rondaActual++;
        if (rondaActual > rondaTotal) {
            // Si terminaron todas las rondas, mostramos los resultados
            mostrarResultados();
            return;
        }
    }
    iniciarJuego();
});

finalizarJuego.addEventListener("click", () => {
    // Preguntar si está seguro de finalizar antes de todas las rondas
    if (rondaActual < rondaTotal || puntuaciones[jugadorActual][rondaActual - 1] === null) {
        const confirmar = confirm("¿Estás seguro de finalizar el juego? Los puntajes actuales serán los definitivos.");
        if (!confirmar) return;
        
        // Rellenar puntuaciones faltantes con 0
        for (let i = 0; i < jugadores.length; i++) {
            for (let j = 0; j < rondaTotal; j++) {
                if (puntuaciones[i][j] === null) {
                    puntuaciones[i][j] = 0;
                }
            }
        }
    }
    
    mostrarResultados();
});

function mostrarResultados() {
    pantallaJuego.style.display = "none";
    pantallaResultados.style.display = "flex";
    
    const listaResultados = document.getElementById("listaResultados");
    listaResultados.innerHTML = '';
    
    // Procesamos los resultados
    const resultadosFinales = jugadores.map((nombre, i) => {
        const puntosRondas = puntuaciones[i];
        const total = puntosRondas.reduce((acc, val) => acc + (val || 0), 0);
        return { 
            nombre, 
            puntosRondas, 
            total 
        };
    });
    
    // Ordenamos por puntuación total (de mayor a menor)
    resultadosFinales.sort((a, b) => b.total - a.total);
    
    // Creamos las filas de la tabla
    resultadosFinales.forEach((jugador, index) => {
        const fila = document.createElement("tr");
        
        // Posición
        const posicion = document.createElement("td");
        posicion.textContent = `${index + 1}`;
        
        // Nombre del jugador
        const nombre = document.createElement("td");
        nombre.textContent = jugador.nombre;
        
        // Puntos de cada ronda
        const puntos1 = document.createElement("td");
        puntos1.textContent = jugador.puntosRondas[0] !== null ? jugador.puntosRondas[0] : '-';
        
        const puntos2 = document.createElement("td");
        puntos2.textContent = jugador.puntosRondas[1] !== null ? jugador.puntosRondas[1] : '-';
        
        const puntos3 = document.createElement("td");
        puntos3.textContent = jugador.puntosRondas[2] !== null ? jugador.puntosRondas[2] : '-';
        
        // Total
        const total = document.createElement("td");
        total.textContent = jugador.total;
        total.style.fontWeight = "bold";
        
        // Si es el ganador (primer lugar), resaltamos la fila
        if (index === 0) {
            fila.classList.add("ganador");
            // También actualizamos el título del ganador
            document.getElementById("nombreGanador").textContent = `${jugador.nombre} - ${jugador.total} puntos`;
        }
        
        fila.appendChild(posicion);
        fila.appendChild(nombre);
        fila.appendChild(puntos1);
        fila.appendChild(puntos2);
        fila.appendChild(puntos3);
        fila.appendChild(total);
        
        listaResultados.appendChild(fila);
    });
}

// Botón para volver a jugar
volverAJugar.addEventListener("click", () => {
    // Reiniciar todo el juego
    pantallaResultados.style.display = "none";
    pantallaInicio.style.display = "flex";
    
    // Limpiar datos anteriores
    jugadores = [];
    puntuaciones = [];
    jugadorActual = 0;
    rondaActual = 1;
    
    // Reiniciar botones
    botonIniciar.disabled = true;
    cantidadUsuarios.value = "1";
});

// Al cargar la página, asegurarse de que se muestre la pantalla de inicio
window.onload = function() {
    pantallaInicio.style.display = "flex";
    pantallaJuego.style.display = "none";
    pantallaResultados.style.display = "none";
};



