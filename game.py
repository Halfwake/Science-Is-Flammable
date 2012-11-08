import pygame
from pygame.locals import *

import mode
import map_file
import camera
import config
import content
import messenger
import agent

class BattleMode(mode.Mode): pass

class Map(object):
    def __init__(self, name, file_name, group, thing_group, size):
        self.name = name
        self.file_name = file_name
        self.group = group
        self.size = size
        self.thing_group = thing_group#for objects and entities
        self.start_agents = []
        self.start_objects = []
        self.map = [[None for y in xrange(size[1])] for x in xrange(size[0])]
        
    @property
    def width(self): return size[0]
    @property
    def height(Self): return size[1]
    
    def save_data(self):
        json_info = {}
        json_info["NAME"] = self.name
        json_info["MAP"] = [[None for y in xrange(size[1])] for x in xrange(size[0])]
        for x, row in enumerate(self.map):
            for y, item in enumerate(row):
                json_info["MAP"][x][y] = self.map[x][y]
        return json_info

class GameMode(mode.Mode):
    "A class for the mode that involves traversing the over world."
    def __init__(self):
        self.new_game()
    def new_game(self):
        "Basic setup for a new game."
        self.player = Player(config.PLAYER_START)
        self.map = map_file.load_map(config.START_MAP)
        self.agents = self.map.start_agents
        self.objects = self.map.start_objects
        #self.agent_object_group = self.map.group #Copies the map group (sprite batch) that draws objects and agents
        #self.cam_buffer_screen = pygame.Surface() #a buffer surface used to position objects and agents relative to the camera
    def save_data(self):
        json_info = {}
        json_info["PLAYER"] = self.player.save_data()
        json_info["MAP"] = self.map.save_data()
        json_info["AGENTS"] = [agent.save_data() for agent in self.agents]
        json_info["OBJECTS"] = [a_object.save_data() for a_object in self.objects]
        return json_info
    def on_draw(self, display, screen, camera):
        screen.fill(config.VOID_COLOR)
        display.blit(screen, (0, 0))
        self.map.group.draw(screen)
        self.map.thing_group.draw(screen)
        self.player.draw(screen)
        camera = messenger.Messenger.camera
        display.blit(screen, (camera.rect.left , camera.rect.top))
        pygame.display.flip()
    def on_update(self):
        self.player.update()
        for a_object in self.objects:
            if a_object.in_camera(): a_object.update()
        for agent in self.agents:
            if agent.in_camera():
                agent.update()
    def on_input(self, a_input):
        for event in a_input:
            if event.type == KEYDOWN:
                camera = messenger.Messenger.camera
                if event.key == K_w:
                    camera.move_ip(0, 32)
                elif event.key == K_s:
                    camera.move_ip(0, -32)
                if event.key == K_a:
                    camera.move_ip(32, 0)
                elif event.key == K_d:
                    camera.move_ip(-32, 0)
                    
                if event.key == K_UP:
                    self.player.move(0, -1 * self.player.speed)
                elif event.key == K_DOWN:
                    self.player.move(0, self.player.speed)
                if event.key == K_RIGHT:
                    self.player.move(self.player.speed, 0)
                elif event.key == K_LEFT:
                    self.player.move(-1 * self.player.speed, 0)



class Object(pygame.sprite.Sprite, camera.View):
    "A class for all objects."
    def __init__(self, group, pos, size, image):
        super(Object, self).__init__(group)
        self.image = image
        self.rect = pygame.rect(pos, size)
    def save_data(self):
        return None
    def update():
        pass

class Player(agent.Mover):
    "The class representing the player character."
    def __init__(self, pos):
        self.group = pygame.sprite.Group()
        super(Player, self).__init__(self.group, pos, config.PLAYER_SIZE, content.IMAGE["PLAYER_1"])
        self.speed = 64
        self.actions = []
    def save_data(self):
        return None
    def update(self):
        if self.actions: self.actions.pop()()
    def draw(self, screen):
        self.group.draw(screen)
        
        
