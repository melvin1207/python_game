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

surface2 = pygame.Surface( (200, 200) )
surface2.fill(verde)

rect = surface2.get_rect()
rect.center = ( width // 2, height // 2)
my_color = (200, 20, 90)



rect2 = (100, 100, 80, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(my_color)
    surface.blit(surface2, rect)
    pygame.draw.rect(surface, red, (100, 50, 80, 40) )
    pygame.display.update()