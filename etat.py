import pygame


class Etat:

    def __init__(self, menu, game):
        self.menu = menu
        self.game = game
        self.current_state = "menu"

    def switch_state(self, new_state):
        self.current_state = new_state

    def draw(self, screen):
        if self.current_state == "menu":
            self.menu.draw(screen)
        elif self.current_state == "game":
            self.game.draw(screen)

    def handle_events(self, events):
        if self.current_state == "menu":
            self.menu.handle_events(events)
        elif self.current_state == "game":
            self.game.handle_events(events)


