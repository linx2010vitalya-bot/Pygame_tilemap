import pygame as pg

class Player: 
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.width = 28
        self.height = 44 
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 200
        self.jump_power = 400
        
        self.on_ground = False
        self.alive = True