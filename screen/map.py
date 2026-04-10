import pygame
import pytmx 
import pyscroll

class Map:
    def __init__(self, screen , player):
        self.screen = screen
        self.player = player
        self.tmx_data = None
        self.map_layer = None
        self.map_data = None
        self.group = None

        self.switch_map("sans titre")


    def switch_map(self, map: str):
        self.tmx_data = pytmx.load_pygame(f"assets/map/{map}.tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=14)

        self.group.add(self.player)
        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)

    

    def draw(self):
        self.group.draw(self.screen)