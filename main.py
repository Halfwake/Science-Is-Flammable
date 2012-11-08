import pygame
from pygame.locals import *

import config
import content
import messenger
import camera

if __name__ == "__main__":
    display = pygame.display.set_mode(config.DISPLAY_SIZE)
    pygame.display.set_caption(config.GAME_TITLE)
    pygame.init()
    pygame.key.set_repeat(0, 1)
    clock = pygame.time.Clock()

    for key in content.IMAGE:
        content.IMAGE[key] = content.IMAGE[key].convert()
    
    while True:
        clock.tick(30)
        screen = messenger.Messenger.screen
        camera = messenger.Messenger.camera
        events = []

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
        
        messenger.Messenger.mode.on_draw(display, screen, camera)
        messenger.Messenger.mode.on_input(events)
        messenger.Messenger.mode.on_update()
