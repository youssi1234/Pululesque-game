import pygame
from RikiLabs.entity.icon import icon
from RikiLabs.map.map import map
from RikiLabs.game import game

pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

# Element à mettre dans la fenetre
TheGame = game(screen)

running = True
while running:

    # mettre les éléments dans screen
    screen.blit(TheGame.mapEx.image, TheGame.mapEx.rect)
    screen.blit(TheGame.icon_player.image, TheGame.icon_player.rect)
    pygame.display.flip()

    # interaction avec les elements
    TheGame.icon_player.move(screen, TheGame.mapEx)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            TheGame.icon_player.key_Held[event.key] = True
        elif event.type == pygame.KEYUP:
            TheGame.icon_player.key_Held[event.key] = False
    screen.fill((0, 0, 0))  # fond noir

pygame.quit()