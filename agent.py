import pygame

import camera
import content
import config
import messenger

class Agent(pygame.sprite.Sprite, camera.View):
    "A class representing all entities with AI."
    def __init__(self, group, pos, size, image):
        super(Agent, self).__init__(group)
        self.image = image
        self.rect = pygame.Rect(pos, size)
    def save_data(self):
        return None


class Mover(Agent):
    def __init__(self, group, pos, size, image):
        super(Mover, self).__init__(group, pos, size, image)
        self.actions = []
    def move(self, delta_x, delta_y):
        "Handles tweened movement."
        frame_move = config.FRAME_MOVE

        if delta_x < 0: xdirection = -1
        else: xdirection = 1
        delta_x = abs(delta_x)
        xmoves = delta_x / frame_move

        if delta_y < 0: ydirection = -1
        else: ydirection = 1
        delta_y = abs(delta_y)
        ymoves = delta_y / frame_move
        
        for move in xrange(xmoves): self.actions.append(lambda : self.move_ip(frame_move * xdirection, 0))
        for move in xrange(ymoves): self.actions.append(lambda : self.move_ip(0, frame_move * ydirection))

    def move_ip(self, delta_x, delta_y):
        "Handles instant movement and the collison related to it."
        camera = messenger.Messenger.camera
        
        super(Mover, self).move_ip(delta_x, 0)
        in_cam = self.in_camera()
        in_walk = self.in_walk()
        while (not in_cam[0]) or (not in_walk[0]):
            if delta_x < 0: super(Mover, self).move_ip(1, 0)
            elif delta_x > 0: super(Mover, self).move_ip(-1, 0)
            in_cam = self.in_camera()
            in_walk = self.in_walk()
            
        super(Mover, self).move_ip(0, delta_y)
        in_cam = self.in_camera()
        in_walk = self.in_walk()
        while (not in_cam[1]) or (not in_walk[1]):
            if delta_y < 0: super(Mover, self).move_ip(0, 1)
            elif delta_y > 0: super(Mover, self).move_ip(0, -1)
            in_cam = self.in_camera()
            in_walk = self.in_walk()

class Fighter(Mover):
    def __init__(self, group, pos, size, image, name, game_name, description, attack, strength, defense, science, max_research, speed):
        super(Fighter, self).__init__(group, pos, size, image)
        self.name = name
        self.game_name = game_name
        self.description = description
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.science = science
        self.max_research = max_research
        self.research = max_research
        self.speed = speed
    def save_data(self):
        json_info = {}
        json_info["NAME"] = self.name
        json_info["POS"] = self.pos
        json_info.research["RESEARCH"] = self.research
        return json_info

def home_player(self):
    player = messenger.Messenger.modes["GameMode"].player
    if self.rect.bottom < player.rect.top:
        self.move(0, self.speed)
    elif self.rect.top > player.rect.bottom:
        self.move(0,  -1 * self.speed)
    if self.rect.left > player.rect.right:
        self.move(-1 * self.speed, 0)
    elif self.rect.right < player.rect.left:
        self.move(self.speed, 0)
    

AGENT = {}
class Anon(Fighter):
    def __init__(self, group, pos, size):
        super(Anon, self).__init__(group,
                                   pos,
                                   size,
                                   content.IMAGE["SPOOKY_INTERN_JOE"],
                                   "SPOOKY_INTERN_JOE",
                                   "Spooky Intern Joe",
                                   "This description is too spooky to be viewed.",
                                   0,
                                   0,
                                   999999,
                                   999999,
                                   999999,
                                   64)
    def update(self):
        home_player(self)
        if self.actions: self.actions.pop()()
AGENT["SPOOKY_INTERN_JOE"] = Anon        
