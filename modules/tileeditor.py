class TileEditor:
    def __init__(self,width,height, tile_size):

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



















