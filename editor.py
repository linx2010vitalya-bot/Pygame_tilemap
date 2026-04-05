import pygame as pg
from modules.tileeditor import TileEditor

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Editor")
clock = pg.time.Clock()
