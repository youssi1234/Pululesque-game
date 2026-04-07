import pygame
from RikiLabs.entity.icon import icon
from RikiLabs.map.map import map

pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

# Element à mettre dans la fenetre
icon_player = icon(screen)
mapEx = map(screen)

running = True
while running:

    # mettre les éléments dans screen
    screen.blit(mapEx.image, mapEx.rect)
    screen.blit(icon_player.image, icon_player.rect)
    pygame.display.flip()

    # interaction avec les elements
    icon_player.move(screen, mapEx)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            icon_player.key_Held[event.key] = True
        elif event.type == pygame.KEYUP:
            icon_player.key_Held[event.key] = False
    screen.fill((0, 0, 0))  # fond noir

pygame.quit()