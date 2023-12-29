import sys
import pygame

pygame.init()

width = 1000
height = 500

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('MY GAME')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()