import json
import pygame as pg

class TileEditor:
    def __init__(self,width,height, tile_size):

        self.height = height
        self.width = width
        self.tile_size = tile_size
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]

        self.current_tile = 1

        self.offset_x = 150
        self.offset_y = 60

        self.tile_colors = {
            0: (50, 50, 50),
            1: (139, 69, 19),
            2: (0, 200, 0),
            3: (100, 100, 100),
            4: (255, 100, 0)
            }
        
    def handle_click(self, mouse_x, mouse_y,button):
        
        adjusted_x = mouse_x - self.offset_x
        adjusted_y = mouse_y - self.offset_y

        col = adjusted_x // self.tile_size
        row = adjusted_y // self.tile_size

        if 0 <= col < self.width and 0 <= row < self.height:
            if button == 1:
                self.map_data[row][col] = self.current_tile
            elif button == 3:
                self.map_data[row][col] = 0

    def set_current_tile(self, tile_id):

        if tile_id in self.tile_colors:
            self.current_tile = tile_id

    def safe_to_file(self, filename):
        data = {
            "width": self.width,
            "height": self.height,
            "tile_size": self.tile_size,
            "map": self.map_data
        }

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

        print(f"Карта сохранения в {filename}")

    def load_from_file(self, filename): 
        try:
            with open(filename, 'r', encoding = 'utf-8') as f:
                          data = json.load(f)
                
            self.width = data ['width']
            self.height = data['height']
            self.tile_size = data['tile_size']
            self.map_data = data['map']

            print(f"Карта загружена из {filename}")
            return True
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
            return False

    def draw(self,screen):
        for row in range(self.height):
            for col in range(self.width):
                 tile_id = self.map_data[row][col]
                 x = col * self.tile_size
                 y = row * self.tile_size

                 color = self.tile_colors.get(tile_id, (255, 0, 255))
                 pg.draw.rect(screen, color, (x, y, self.tile_size, self.tile_size))
                 pg.draw.rect(screen, (100, 100, 100), (x, y, self.tile_size, self.tile_size), 2)

    def draw_ui(self, screen):
        font = pg.font.Font(None, 28)

        title = font.render("Tilemap Editor", True, (255, 255, 255))
        screen.blit(title, (10,10))

        current_text = font.render(f"Тайл: {self.current_tile}", True, (255,255,255))
        screen.blit(current_text, (10, 40))

        palette_y = 70
        for tile_id in range(1,5):
             x = 10
             y = palette_y + (tile_id - 1) * 35

             color = self.tile_colors[tile_id]
             pg.draw.rect(screen, color, (x, y, 30, 30))

             border_color = (255, 255, 0) if tile_id == self.current_tile else (255,255,255)
             pg.draw.rect(screen, border_color, (x, y, 30, 30), 2)

             num_text = font.render(str(tile_id), True, (255, 255, 255))
             screen.blit(num_text, (x + 35, y + 5))

             hints = [
                  "1-4: Выбор тайла",
                  "ЛКМ: Рисовать",
                  "ПКМ: Стирать",
                  "S: Сохранить",
                  "L: Загрузить"
             ]

             hint_y = 250
             for hint in hints:
                text = pg.font.Font(None, 22).render(hint, True, (200, 200, 200))
                screen.blit(text, (10, hint_y))
                hint_y += 25
















