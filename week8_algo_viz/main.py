import pygame #type: ignore
import math
import random
import sys

from pygame.locals import * # type: ignore

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 1. THE VISUALIZER CONFIGURATION
# Handles the math for bar sizes and drawing
class DrawInformation:
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        # Grab the active window
        self.window = pygame.display.get_surface()
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # Calculate dynamic width based on number of items
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        
        # Calculate dynamic height unit
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

    # Added this method to actually render the bars
    def draw(self, bg_color, color_positions={}):
        self.window.fill(bg_color)
        
        for i, val in enumerate(self.lst):
            # Math to place bars correctly
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height
            
            color = WHITE
            if i in color_positions:
                color = color_positions[i]
            # Draw Rectangle: (Surface, Color, (x, y, width, height))
            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height))
        pygame.display.update()


def bubble_sort(draw_info):
    lst = draw_info.lst
    
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            
            if num1 > num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
                draw_info.draw(BLACK, {j: GREEN, j+1: RED})
                
                yield True
    return lst

# 2. THE MAIN APPLICATION
# Handles the Game Loop and State
class Main:
    pygame.init()
    
    # Constants
    BACKGROUND_COLOR = BLACK
    
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    
    # Initialize Screen immediately
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    
    def __init__(self):
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.lst = self.generate_starting_list()
        # Initialize the DrawInfo helper
        self.draw_info = DrawInformation(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT, self.lst)
        
    def generate_starting_list(self):
        # Generate 50 random numbers between 0 and 100
        return [random.randint(0, 100) for _ in range(50)]

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            
            # A. Event Handling
            for event in pygame.event.get():
                if event.type == QUIT: #type: ignore
                    pygame.quit()
                    sys.exit()
                
                # Press 'R' to generate a new random list
                if event.type == KEYDOWN: #type: ignore
                    if event.key == K_r: #type: ignore
                        self.lst = self.generate_starting_list()
                        self.draw_info.set_list(self.lst)

            # B. Draw Routine
            self.draw_info.draw(self.BACKGROUND_COLOR)
            pygame.display.update()

if __name__ == "__main__":
    app = Main()
    app.run()