import pygame
import pytmx
import pyscroll

class map(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.tmx_data = pytmx.util_pygame.load_pygame('RikiLabs/assets/lot2/map.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)    
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
        map_layer.zoom = 1
        self.groupLayer_Map = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)

        # on va prendre les zones de collisions 
        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                # Si c'est un polygone, il possède l'attribut 'points'
                if hasattr(obj, 'points'):
                    # On convertit les points relatifs en points absolus sur la map
                    points = [(obj.x + p.x, obj.y + p.y) for p in obj.points]
                    self.walls.append(points)
                else:
                    # Au cas où tu as quand même quelques rectangles
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))