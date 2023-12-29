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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = 'Izquierda'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = 'Derecha'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = 'Abajo'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = 'Arriba'

        if event.type == pygame.KEYUP:
            pass

    surface.fill(white)
    
    pygame.display.update()