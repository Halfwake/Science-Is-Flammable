import json
import pygame

import game
import tile
import agent
import config

def save_map(a_map):
    "Takes a map and returns JSON text representing it."
    a_file = open(a_map.file_name, "w")
    json_info = a_map.save_data()
    a_file.write(json_info)
    a_file.close()

def load_map(file_name):
    "Takes a file_name and creates a map out of it."
    a_file = open(file_name)
    json_info = json.loads(a_file.read())
    a_file.close()
    group = pygame.sprite.Group()
    thing_group = pygame.sprite.Group()
    a_map = game.Map(json_info["NAME"], file_name, group, thing_group, (len(json_info["MAP"][0]), len(json_info["MAP"])))
    agents = [age for age in json_info["AGENTS"]]
    for a_agent in agents: a_map.start_agents.append(agent.AGENT[a_agent["NAME"]](thing_group, a_agent["POS"], config.TILE_SIZE))
    objects = [a_object for a_object in json_info["OBJECTS"]]
    for y, row in enumerate(json_info["MAP"]):
        for x, item in enumerate(row):
            a_map.map[x][y] = tile.TILE[item](group, (x * config.TILE_WIDTH, y * config.TILE_HEIGHT), config.TILE_SIZE)
    return a_map
            
