import pygame as pg
import json

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        self.width = 0
        self.height = 0


        self.tile_colors = {
            0: (50, 50 ,50),
            1: (139, 69, 19),
            2: (0, 200, 0),
            3: (100, 100, 100),
            4: (255, 0, 0)
        }


        self.solid_tiles = {1, 3}
        self.danger_tiles = {4}

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.map_data = data['map']
        self.width = data['width']
        self.height = data['height']    
        
