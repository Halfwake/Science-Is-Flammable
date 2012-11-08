"Includes all art content files."

import pygame
from os.path import sep

def load_image(file_name):
    IMAGE_DIR = "content" + sep + "image" + sep
    image = pygame.image.load(IMAGE_DIR + file_name)
    #image.convert()
    return image

IMAGE = {}
IMAGE["GRASS_1"] = load_image("GRASS_1.png")
IMAGE["MAINMENU_BACKGROUND_1"] = load_image("MAINMENU_BACKGROUND_1.png")
IMAGE["QUIT_BUTTON_1"] = load_image("QUIT_BUTTON_1.png")
IMAGE["START_BUTTON_1"] = load_image("START_BUTTON_1.png")
IMAGE["PLAYER_1"] = load_image("PLAYER_1.png")
IMAGE["CRUMPLE_PAPER_1"] = load_image("CRUMPLE_PAPER_1.png")
IMAGE["HOLE_IN_PAPER_1"] = load_image("HOLE_IN_PAPER_1.png")
IMAGE["SPOOKY_INTERN_JOE"] = load_image("SPOOKY_INTERN_JOE.png")

SOUND_DIR = "content" + sep + "sound" + sep
SOUND = {}

MUSIC_DIR = "content" + sep + "music" + sep
MUSIC = {}
