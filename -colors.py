import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('Colors')

#RGB
red = pygame.Color(255, 0, 0)
verde = pygame.Color(0, 255, 0)
azul = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

my_color = (200, 20, 90)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(red)
    pygame.display.update()