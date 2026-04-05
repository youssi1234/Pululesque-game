import pygame

class Etat:
    def __init__(self):
        self.current_state = "menu"
        self.loading_start_time = 0
        self.loading_duration = 2000  # 2 secondes de chargement (en millisecondes)

    def switch_state(self, new_state):
        if new_state == "loading":
            self.loading_start_time = pygame.time.get_ticks() # On retient l'heure du clic
        self.current_state = new_state

    def update_loading(self):
        # Si on est en chargement, on regarde si le temps est écoulé
        if self.current_state == "loading":
            if pygame.time.get_ticks() - self.loading_start_time > self.loading_duration:
                self.current_state = "game"
