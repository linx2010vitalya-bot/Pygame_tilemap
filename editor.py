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


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                editor.set_current_tile(1)
            elif event.key == pg.K_2:
                editor.set_current_tile(2)
            elif event.key == pg.K_3:
                editor.set_current_tile(3)
            elif event.key == pg.K_4:
                editor.set_current_tile(4)
            elif event.key == pg.K_s:
                editor.safe_to_file("tilemap.json")
            elif event.key == pg.K_l:
                editor.load_from_file("filemap.json")


    if event.type == pg.MOUSEBUTTONDOWN:
        mouse_pressed = True
        editor.handle_click(*event.pos, event.button)

    if event.type == pg.MOUSEBUTTONUP:
        mouse_pressed = False 


    if mouse_pressed:
        mouse_buttons = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()

        if mouse_buttons[0]:
            editor.handle_click(*mouse_pos, 1)
        elif mouse_buttons[2]:
            editor.handle_click(*mouse_pos, 3)


    screen.fill((30, 30, 40))


    pg.draw.rect(screen, (20, 20, 30), (0, 0, 150, 600))


    map_surface = pg.Surface((640, 480))
    editor.draw(map_surface)
    screen.blit(map_surface, (editor.offset_x, editor.offset_y))


    editor.draw_ui(screen)

    pg.display.flip()

pg.quit()
