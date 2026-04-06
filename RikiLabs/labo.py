import pygame
from icon import icon
pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

# Element à mettre dans la fenetre
icon_player = icon()


running = True

while running:


    screen.blit(icon_player.image, icon_player.rect)
    pygame.display.flip()
    icon_player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            icon_player.key_Held[event.key] = True
        elif event.type == pygame.KEYUP:
            icon_player.key_Held[event.key] = False
    screen.fill((0, 0, 0))  # fond noir

pygame.quit()