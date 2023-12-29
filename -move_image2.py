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


image = pygame.image.load('images/medium_circle.png')
rect = image.get_rect()
rect.center = (width // 2, height // 2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos()
    surface.fill(white)
    surface.blit(image, rect)
    pygame.display.update()