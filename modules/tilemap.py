import pygame as pg

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
        
