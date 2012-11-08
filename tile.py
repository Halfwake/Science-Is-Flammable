import pygame
import json

import content
import camera

TILE = {}

class Tile(pygame.sprite.Sprite, camera.View):
    def __init__(self, group, pos, size, name, image, walk):
        super(Tile, self).__init__(group)
        self.name = name
        self.image = image #The image the tile has
        self.rect =  pygame.Rect(pos, size)
        self.walk = walk #Whether or not the tile can be traversed
    def on_touch(self, other):
        "What happens to something upon walking over this tile."
        pass
    def save_data(self):
        "Returns a JSON dictionary describing this tile."
        return json.dumps({"TILE" : self.name,
                           "POS" : self.rect.topleft,
                           "SIZE" : self.rect.size})

#Each possible tile is a constructor that takes a group for the tile to belong to
#Tiles without special 'on_touch' functions are created with lambdas    
TILE["GRASS_1"] = lambda group, pos, size : Tile(group, pos, size, "GRASS_1", content.IMAGE["GRASS_1"], True)
TILE["CRUMPLE_PAPER_1"] = lambda group, pos, size : Tile(group, pos, size, "CRUMPLE_PAPER_1", content.IMAGE["CRUMPLE_PAPER_1"], True)
TILE["HOLE_IN_PAPER_1"] = lambda group, pos, size : Tile(group, pos, size, "HOLE_IN_PAPER_1", content.IMAGE["HOLE_IN_PAPER_1"], False)
