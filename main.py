import pygame
from menu import Menu


pygame.init()

size_screen = (600, 400)
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode(size_screen)

game_state = "menu"

fluidity = 60
clock = pygame.time.Clock()

running = True
while running:
    # 1. GESTION DES ÉVÉNEMENTS (Clavier/Souris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "menu":
        menu = Menu(game_state)
        menu.draw(screen)

    elif game_state == "game":
        game = Game(game_state)
        screen.fill((255, 172, 112))

    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
