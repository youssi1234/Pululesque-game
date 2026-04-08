import pygame
import pytmx
import pyscroll
from RikiLabs.entity.icon import icon
from RikiLabs.assets.lot2.map import map

class game(pygame.sprite.Sprite):
    def __init__(self, screen):

        # map 
        self.mapI = map(screen)

        # player
        player_position = self.mapI.tmx_data.get_object_by_name("player")
        self.icon_player = icon(player_position.x, player_position.y)

        # groupe-na anaty mapI ilay joueur
        self.mapI.groupLayer_Map.add(self.icon_player)