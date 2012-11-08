import pygame

import config
import messenger

class View(object):
    "A class for objects that can be viewed by the camera and moved."
    def in_camera(self, delta = (0, 0)):
        "Returns a tuple telling which coordinates the object is inside the camera"
        cord1, cord2 = False, False
        delta_x, delta_y = delta[0], delta[1]
        camera = messenger.Messenger.camera
        
        if (0 <= (self.rect.left + camera.rect.left) <= config.SCREEN_WIDTH) and (0 <= (self.rect.right + camera.rect.left) <= config.SCREEN_WIDTH):
            cord1 = True
        if (0 <= (self.rect.top + camera.rect.top) <= config.SCREEN_HEIGHT) and (0 <= (self.rect.bottom + camera.rect.top) <= config.SCREEN_HEIGHT):
            cord2 = True
        return (cord1, cord2)
    def in_walk(self, delta = (0, 0)):
        cord1, cord2 = True, True
        delta_x, delta_y = delta[0], delta[1]
        a_map = messenger.Messenger.modes["GameMode"].map
        tile_map_x, tile_map_y = (self.rect.left + delta_x - 1) / config.TILE_WIDTH, (self.rect.top + delta_y - 1) / config.TILE_HEIGHT
        tile_x, tile_y = tile_map_x * config.TILE_WIDTH, tile_map_y * config.TILE_HEIGHT
        if not a_map.map[tile_map_x][tile_map_y].walk:
            if (tile_x <= self.rect.left <= (tile_x + config.TILE_WIDTH)) or (tile_x <= self.rect.right <= (tile_x + config.TILE_WIDTH)):
                cord1 = False
            if (tile_y <= self.rect.top <= (tile_y + config.TILE_HEIGHT)) or (tile_y <= self.rect.bottom <= (tile_y + config.TILE_HEIGHT)):
                cord2 = False
        return (cord1, cord2)
                
    def move_ip(self, delta_x, delta_y):
        self.rect.move_ip(delta_x, delta_y)
    
class Camera(object):
    "A simple object meant to give limits to draw calls."
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos, config.CAMERA_SIZE)
    
    def move_ip(self, delta_x, delta_y):
        self.rect.move_ip(delta_x, delta_y)

    def save_data(self):
        return {"POS" : self.pos, "SIZE" : self.size}
    def load_data(self, json_info):
        self.rect.left, self.rect.top = json_info["CAMERA"]["POS"]
        self.size = json_info["CAMERA"]["SIZE"]    
