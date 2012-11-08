import pygame
from pygame.locals import *

import mode
import config
import content
import gui
import messenger

class MainMenuMode(mode.Mode):
    def __init__(self):
        self.make_background()
        self.make_buttons()
    def make_background(self):
        "Creates a group containing the background."
        self.background = pygame.sprite.Group()
        background_sprite = pygame.sprite.Sprite(self.background)
        background_sprite.image = content.IMAGE["MAINMENU_BACKGROUND_1"]
        background_sprite.rect = pygame.Rect((0, 0), config.CAMERA_SIZE)
    def make_buttons(self):
        "Creates a group for all main menu buttons."
        self.buttons = pygame.sprite.Group()
        self.button_refs = [] #Stores a ref to each button
        
        exit_sprite = gui.Button(self.buttons,
                                 content.IMAGE["QUIT_BUTTON_1"],
                                 (config.CAMERA_WIDTH / 2 - 128, config.CAMERA_HEIGHT / 4 * 3 - 32),
                                 (256, 64))
        exit_sprite.on_click = lambda : (pygame.quit(), quit())
        self.button_refs.append(exit_sprite)
        
        start_sprite = gui.Button(self.buttons,
                                  content.IMAGE["START_BUTTON_1"],
                                  (config.CAMERA_WIDTH / 2 - 128, config.CAMERA_HEIGHT / 2 - 32),
                                  (256, 64))
        start_sprite.on_click = lambda : messenger.Messenger.switch_mode("GameMode")
        self.button_refs.append(start_sprite)
        
    def on_draw(self, display, screen, camera):
        self.background.draw(screen)
        self.buttons.draw(screen)
        display.blit(screen, (0, 0))
        pygame.display.flip()
    def on_input(self, a_input):
        for event in a_input:
            if event.type == MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.is_hover(event):
                        button.on_hover()
                    if button.is_click(event):
                        button.on_click()
        
class MenuMode(mode.Mode): pass

class SaveMenu(mode.Mode): pass
