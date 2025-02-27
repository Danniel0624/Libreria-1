Pong en Python

Este es un clon del clásico juego Pong desarrollado en Python utilizando la biblioteca Pygame.

🎯 Objetivo del Programa

El objetivo de este proyecto es recrear el clásico juego Pong utilizando Python y Pygame, permitiendo a dos jugadores competir en una partida simple pero entretenida. Este desarrollo sirve como una introducción a la programación de videojuegos con Pygame y el manejo de gráficos en 2D.

🏢 Datos del estudiante

Nombre: Daniel Lozada 

Correo de contacto: julozadabo@uide.edu.ec

Institución: UIDE

Fecha de desarrollo: 18-01-2025/24-02-2025

🎮 Características

Simulación de un juego clásico de Pong.

Control de las paletas mediante el teclado.

Rebote de la pelota en los bordes y en las paletas.

Reinicio automático cuando la pelota sale de la pantalla.

Interfaz gráfica sencilla y funcional.

📋 Requisitos

Antes de ejecutar el juego, se debe de tener instalado Python 3.x y la biblioteca Pygame.

Instalar Pygame con el siguiente comando:

pip install pygame

🚀 Ejecución

Para ejecutar el juego, se debe abrir una terminal en el directorio donde se encuentra el archivo y escribir:

python pong.py

🕹️ Controles

Jugador 1 (Izquierda):

W → Mover hacia arriba

S → Mover hacia abajo

Jugador 2 (Derecha):

⬆️ (Flecha arriba) → Mover hacia arriba

⬇️ (Flecha abajo) → Mover hacia abajo

🔍 Explicación de las Funcionalidades del Código

Inicialización: Se importa la librería pygame, se configura la ventana de juego y se definen los colores, dimensiones y velocidad de los objetos.

Dibujar los elementos: Se crean funciones para dibujar la pelota y las paletas en la pantalla.

Movimiento de la pelota: Se actualiza la posición de la pelota en cada iteración del bucle de juego.

Colisión con los bordes: Si la pelota toca la parte superior o inferior, cambia su dirección en el eje Y.

Colisión con las paletas: Se detecta el choque de la pelota con las paletas para rebotar correctamente.

Puntuación: Si la pelota sale por la izquierda o la derecha, se reinicia la posición y se actualiza el marcador.

Control del juego: Se capturan eventos del teclado para mover las paletas.

📌 Estructura del Código

pong.py: Código principal del juego.

