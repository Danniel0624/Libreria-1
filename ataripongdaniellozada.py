import pygame 

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de las paletas y la bola 
paleta_ancho, paleta_alto = 10, 100
bola_radio = 10

# Posiciones iniciales
paleta1_x, paleta1_y = 30, (ALTO // 2) - (paleta_alto // 2)
paleta2_x, paleta2_y = ANCHO - 40, (ALTO // 2) - (paleta_alto // 2)
bola_x, bola_y = ANCHO // 2, ALTO // 2

# Velocidades
velocidad_paleta = 5
bola_dx, bola_dy = 4, 4

# Puntuaciones
puntaje1, puntaje2 = 0, 0

# Fuente de texto
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    pantalla.fill(NEGRO)

    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Controles de las paletas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1_y > 0:
        paleta1_y -= velocidad_paleta
    if teclas[pygame.K_s] and paleta1_y < ALTO - paleta_alto:
        paleta1_y += velocidad_paleta
    if teclas[pygame.K_UP] and paleta2_y > 0:
        paleta2_y -= velocidad_paleta
    if teclas[pygame.K_DOWN] and paleta2_y < ALTO - paleta_alto:
        paleta2_y += velocidad_paleta

  