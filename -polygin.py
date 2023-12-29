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

rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, height // 2)

rect2 = (100, 100, 80, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(my_color)
    pygame.draw.rect(surface, red, rect)
    pygame.draw.circle(surface, verde, (200, 300), 100)
    pygame.draw.line(surface, azul, (100, 100), (200, 300), 2)
    pygame.draw.polygon(surface, azul, ((0, 400), (100, 300), (200, 400)))
    pygame.draw.polygon(surface, azul, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    pygame.display.update()