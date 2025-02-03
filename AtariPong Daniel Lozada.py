import pygame
import sys

# Para inicializar pygame
pygame.init()

# Configurar pantalla
screen_width = 800
screen_height = 600
screen=pygame.display.set_mode((screen_width, screen_height))

# Colores
white = (252, 255, 255)
black = (0, 0, 0)

# Pelota
ball_size = 20
ball_speed =[5,5]
ball = pygame.rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)

#Barras
paddle_width = 10
paddle_height = 100
paddle_speed = 5
