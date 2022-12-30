import pygame
import math
from sys import exit

# COLORES:
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO_SUAVE = (200, 200, 200)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
LONGITUD_COLA = 300  # Cantidad de puntos de trayectoria se almacenan

# Variables

l1 = 125
l2 = 125
ang1 = 1.9
ang2 = 1.9
vel1 = 0.1
vel2 = -0.2
ace1 = 0
ace2 = 0

# ESTRELLA lenta, relación (-1/15)
# ace1 = 0.00040
# ace2 = -0.00060

# ESTRELLA rápida, relación (-1/15)
# ace1 = 0.010
# ace2 = -0.015

# POLÍGONO N+1 LADOS
# ace1 = 0.1
# ace2 = -0.N

CENTRO_X = WINDOW_WIDTH/2
CENTRO_Y = WINDOW_HEIGHT/2

x = 0
y = 0

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Graficador de epitrocoides e hipotrocoides")
clock = pygame.time.Clock()

puntos_trazo = [[CENTRO_X + l1 * math.sin(ang1) + l2 * math.sin(ang2), CENTRO_Y + l1 * math.cos(ang1) + l2 * math.cos(ang2)]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    WINDOW.fill(NEGRO)

    x1 = CENTRO_X + l1 * math.sin(ang1)
    y1 = CENTRO_Y + l1 * math.cos(ang1)

    x2 = x1 + l2 * math.sin(ang2)
    y2 = y1 + l2 * math.cos(ang2)

    # Dibujar pendulos:
    pygame.draw.aaline(WINDOW, AZUL, (CENTRO_X, CENTRO_Y), (x1, y1))  # Línea azul 1
    pygame.draw.aaline(WINDOW, AZUL, (x1, y1), (x2, y2))  # Línea azul 2
    pygame.draw.circle(WINDOW, ROJO, (CENTRO_X, CENTRO_Y), 5)  # Punto centro
    pygame.draw.circle(WINDOW, BLANCO, (x1, y1), 5)  # Punta 1
    pygame.draw.circle(WINDOW, BLANCO, (x2, y2), 5)  # Punta 2

    # Actualizar variables
    ang1 += vel1
    ang2 += vel2
    vel1 += ace1
    vel2 += ace2

    # Dibujar trazo
    puntos_trazo.append([x2, y2])
    if len(puntos_trazo) > LONGITUD_COLA:
        puntos_trazo.pop(0)

    # TRAZO CON LINEAS CONECTADAS
    pygame.draw.aalines(WINDOW, ROJO, False, list(puntos_trazo[i] for i in range(len(puntos_trazo))))

    # TRAZO CON PUNTOS
    for i in range(len(puntos_trazo)):
        pygame.draw.circle(WINDOW, ROJO, puntos_trazo[i], 2)

    # Dibujar circunferencias
    pygame.draw.circle(WINDOW, BLANCO_SUAVE, (CENTRO_X, CENTRO_Y), l1+l2+1, 1) # Circunferencia general
    # pygame.draw.circle(WINDOW, BLANCO_SUAVE, (CENTRO_X, CENTRO_Y), l1, 1)  # Circunferencia 1
    pygame.draw.circle(WINDOW, BLANCO_SUAVE, (x1, y1), l2, 1) # Circunferencia 2

    pygame.display.update()
    clock.tick(FPS)
