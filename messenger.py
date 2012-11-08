import pygame

import game_file
import camera
import config
import menu
import game
import character
import map_file

class Messenger(object):
    "A class that allows cross mode tasks to be performed."
    #A hash containing all modes
    modes = {"MainMenuMode" : menu.MainMenuMode(),
             "MenuMode" : menu.MenuMode(),
             "SaveMenuMode" : menu.SaveMenu(),
             "GameMode" : game.GameMode(),
             "BattleMode" : game.BattleMode(),
             "InventoryMode" : character.InventoryMode(),
             "StatsMode" : character.StatsMode()}
    mode = modes["MainMenuMode"]
    camera = camera.Camera(config.CAMERA_START, config.CAMERA_SIZE)
    screen = pygame.Surface(config.SCREEN_SIZE)
    @staticmethod
    def switch_mode(new_mode):
        Messenger.mode = Messenger.modes[new_mode]
    @staticmethod
    def save_game(file_name):
        "Saves the game."
        json_info = {}
        for mode_key in modes:
            mode = modes[mode_key]
            if not mode == "CAMERA":
                json_info[mode_key] = modes.save_data()
        json_info["CAMERA"] = Messenger.camera.save_data()
        game_file.save_game(file_name, json_info)
    @staticmethod
    def load_game(file_name):
        "Loads a game."
        json_info = game_file.load_game(file_name)
        for mode_key in  json_info:
            mode = json_info[mode_key]
            if mode_key == "CAMERA":
                Messenger.camera.load_data(mode)
            else:
                modes[mode_key].load_data(mode)
        
        
