import pygame
from screen.menu import Menu
from screen.game import Game
from etat import Etat
from composant.loadingAnim import LoadingAnim


pygame.init()

screen_width = 960
screen_height = 540
size_screen = (screen_width, screen_height)

pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode(size_screen)


game_state = Etat()
menu = Menu(game_state , screen_width, screen_height)
game = Game(game_state , screen)
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
    pygame.display.update()


    if game_state.current_state == "menu":
        menu.draw(screen)

    elif game_state.current_state == "loading":
        menu.draw(screen)
        loadingAnim.draw(screen)

    elif game_state.current_state == "game":

        game.update()
        game.handle_events(events)
        game.draw(screen)


    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
