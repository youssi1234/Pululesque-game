import pygame
import pytmx 
import pyscroll

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.map_data = None
        self.group = None

        self.switch_map("fond")

    def switch_map(self, map: str):
        self.tmx_data = pytmx.load_pygame(f"assets/map/{map}.tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

    def draw(self):
        self.group.draw(self.screen)