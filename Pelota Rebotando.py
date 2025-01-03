#nstalar pygame ejecutando (pip install pygame)

import pygame
import sys
import random

# Inicialización de pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pelota Rebotando")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configuración de la pelota
ball_radius = 35  # Radio aumentado
ball_pos = [WIDTH // 2, HEIGHT // 2]  # Posición inicial
ball_vel = [5, 3]  # Velocidad inicial (en píxeles por frame)
ball_text = "ZTZ" # Texto dentro de la pelota
ball_color = RED  # Color inicial de la pelota

# Fuente para el texto
font = pygame.font.Font(None, 36)  # Tamaño de fuente

# Reloj para controlar los FPS
clock = pygame.time.Clock()
FPS = 60

# Función para generar un color aleatorio
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar posición de la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Detección de colisiones con los bordes
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_vel[0] = -ball_vel[0]  # Cambiar dirección horizontal
        ball_color = random_color()  # Cambiar color

    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_vel[1] = -ball_vel[1]  # Cambiar dirección vertical
        ball_color = random_color()  # Cambiar color

    # Dibujar en la pantalla
    screen.fill(BLACK)  # Limpiar la pantalla
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)  # Dibujar la pelota

    # Dibujar el texto dentro de la pelota
    text_surface = font.render(ball_text, True, WHITE)
    text_rect = text_surface.get_rect(center=(ball_pos[0], ball_pos[1]))
    screen.blit(text_surface, text_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(FPS)

# Cerrar pygame
pygame.quit()
sys.exit()
