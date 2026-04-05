import pygame as pg
from modules.tileeditor import TileEditor

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Editor")
clock = pg.time.Clock()


editor = TileEditor(width = 20, height = 15, tile_size = 32)


editor.load_from_file("tilemap.json")


mouse_pressed = False

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False