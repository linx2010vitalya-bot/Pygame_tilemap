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

    def update(self, dt, keys, tilemap):
        if not self.alive:
            return
        

        self.velocity_x = 0
        if keys[pg.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pg.K_RIGHT]:
            self.velocity_x = self.speed


        self.x += self.velocity_x * dt


        corners_x = [
            (self.x, self.y + 5),
            (self.x + self.width, self.y + 5),
            (self.x, self.y + self.height - 5),
            (self.x + self.width, self.y + self.height - 5),    
        ]

        for px, py in corners_x:
            if tilemap.is_solid(px, py):
                if self.velocity_x > 0:
                    self.x = int(px / tilemap.tile_size) * tilemap.tile_size - self.width - 1
                elif self.velocity_x < 0:
                    self.x = int (px / tilemap.tile_size) * tilemap.tile_size + tilemap.tile_size + 1
                break

        
        self.velocity_y += 1000 * dt
        self.y += self.velocity_y * dt


        self.on_ground = False
        corners_y = [
            (self.x + 5, self.y),
            (self.x + self.width - 5, self.y),
            (self.x + 5, self.y + self.height),
            (self.x + self.width - 5, self.y + self.height),
        ]

        for px, py in corners_y:
            if tilemap.is_solid(px, py):
                if self.velocity_y > 0:
                    self.y = int(py / tilemap.tile_size) * tilemap.tile_size - self.height - 1
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.y = int(py / tilemap.tile_size) * tilemap.tile_size + tilemap.tile_size + 1
                    self.velocity_y = 0
                break


            if keys[pg.K_SPACE] and self.on_ground:
                self.velocity_y = -self.jump_power


            for px, py in corners_y:
                if tilemap.is_danger(px, py):
                    self.alive = False
                    break