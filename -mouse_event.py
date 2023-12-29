import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('Colors')

#RGB
red = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

surface2 = pygame.Surface( (200, 200) )
surface2.fill(verde)

my_color = (200, 20, 90)

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('Click izquierda')
            if event.button == 2:
                print('Click centro')
            if event.button == 3:
                print('Click derecha')
            if event.button == 4:
                print('Scroll hacia arriba')
            if event.button == 5:
                print('Scroll hacia abajo')

        if event.type == pygame.MOUSEBUTTONUP:
            pass

    surface.fill(white)
    pygame.display.update()