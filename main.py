import pygame
from menu import Menu
from game import Game
from etat import Etat
from loadingAnim import LoadingAnim

pygame.init()

screen_width = 800
screen_height = 620
size_screen = (screen_width, screen_height)

pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode(size_screen)


game_state = Etat()
menu = Menu(game_state , screen_width, screen_height)
game = Game(game_state , screen_width , screen_height , screen)
loadingAnim = LoadingAnim()


fluidity = 60
clock = pygame.time.Clock()

running = True
while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    game_state.update_loading()

    if game_state.current_state == "menu":
        menu.draw(screen)

    elif game_state.current_state == "loading":
        menu.draw(screen)
        loadingAnim.draw(screen)

    elif game_state.current_state == "game":
        game.handle_events(events)
        game.draw(screen)
        game.icon_player.move(screen)


    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
