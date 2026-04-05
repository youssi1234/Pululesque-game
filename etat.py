import pygame


class Etat:

    def __init__(self):

        self.current_state = "menu"

    def switch_state(self, new_state):
        self.current_state = new_state



