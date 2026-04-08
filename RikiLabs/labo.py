import pygame
import pytmx
import pyscroll
from RikiLabs.game import game

pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((800, 620))
pygame.display.set_caption("Mon premier jeu")

# Element à mettre dans la fenetre
TheGame = game(screen)

clock = pygame.time.Clock()

running = True
while running:

    # mettre les éléments dans screen
    TheGame.mapI.groupLayer_Map.draw(screen)
    pygame.display.flip()

    # interaction avec les elements
    TheGame.icon_player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            TheGame.icon_player.key_Held[event.key] = True
        elif event.type == pygame.KEYUP:
            TheGame.icon_player.key_Held[event.key] = False
    screen.fill((0, 0, 0))  # fond noir
    clock.tick(60)

pygame.quit()