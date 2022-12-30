import pygame
import math
from sys import exit

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
FPS = 60
LONGITUD_COLA = 1500

# CONSTANTES

m1 = 20
m2 = 20
l1 = 125
l2 = 125

ang1 = 1.9
ang2 = 1.9
vel1 = 0
vel2 = 0
ace1 = 0.001
ace2 = -0.0015

# ESTRELLA
#ace1 = 0.0010
#ace2 = -0.0015

# POLIGONO N+1 LADOS
#ace1 = 0.1
#ace2 = -0.N

# LONGITUD_COLA = 400

CENTRO_X = WINDOW_WIDTH/2
CENTRO_Y = WINDOW_HEIGHT/2

x = 0
y = 0

# COLORES:
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Doble pendulo")
clock = pygame.time.Clock()

time = 0
puntos_trazo = [[0,0]]

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

    # Dibujar pendulo 1:
    pygame.draw.circle(WINDOW, ROJO, (CENTRO_X, CENTRO_Y), 5)
    pygame.draw.aaline(WINDOW, AZUL, (CENTRO_X, CENTRO_Y), (x1, y1))
    pygame.draw.circle(WINDOW, BLANCO, (x1, y1), 5)  # Punto

    # Dibujar pendulo 2:
    pygame.draw.aaline(WINDOW, AZUL, (x1, y1), (x2, y2))
    pygame.draw.circle(WINDOW, BLANCO, (x2, y2), 5)  # Punto

# DESPUES CORREGIR EL ORDEN DE DIBUJO PARA QUE NO SE SOLAPE


    ang1 += vel1
    ang2 += vel2

    vel1 += ace1
    vel2 += ace2

    # DIBUJAR TRAZO
    puntos_trazo.append([x2, y2])
    if len(puntos_trazo) > LONGITUD_COLA:
        puntos_trazo.pop(0)
    pygame.draw.aalines(WINDOW, ROJO, False, list(puntos_trazo[i] for i in range(len(puntos_trazo))))

    time += 0.05

    pygame.display.update()
    clock.tick(FPS)
