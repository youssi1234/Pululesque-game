import pygame
from menu import Menu
from game import Game
from etat import Etat

pygame.init()

size_screen = (600, 400)
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode(size_screen)


game_state = Etat()
menu = Menu(game_state)

fluidity = 60
clock = pygame.time.Clock()

running = True
while running:
    # 1. GESTION DES ÉVÉNEMENTS (Clavier/Souris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state.current_state == "menu":
        menu.draw(screen)

    elif game_state.current_state == "game":
        game = Game(game_state)
        game.draw(screen)
        

    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
