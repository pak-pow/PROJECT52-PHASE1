import pygame #type: ignore
import math
import random
import sys

from pygame.locals import * # type: ignore

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
        
        # font setup
        self.font = pygame.font.SysFont('comicsans', 30)
        self.large_font = pygame.font.SysFont('comicsans', 40)

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
    def draw(self, bg_color, algo_name, color_positions={}):
        self.window.fill(bg_color)
        
        controls = "R - Reset | SPACE - Start Sorting"
        sorting_text = f"{algo_name} | 'I' - Insertion | 'B' - Bubble"
        
        controls_surface = self.font.render(controls, 1, WHITE)
        sorting_surface = self.large_font.render(sorting_text, 1, BLUE)
        
        self.window.blit(controls_surface, (self.width/2 - controls_surface.get_width()/2, 45))
        self.window.blit(sorting_surface, (self.width/2 - sorting_surface.get_width()/2, 5)) 
        
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

# Bubble sort
def bubble_sort(draw_info):
    lst = draw_info.lst
    
    # standard bubble sort loop
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            
            # compare adjacent numbers
            if num1 > num2:
                
                # swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
                # visualizing: the draw on swap immediently
                # coloring the two bars being swapped red and green
                draw_info.draw(BLACK, {j: GREEN, j+1: RED})
                
                # pause: yield control back to the main loop
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
        
        # sorting state variables
        self.sorting = False
        self.sorting_algorithm_generator = None
        
    def generate_starting_list(self):
        # Generate 50 random numbers between 0 and 100
        return [random.randint(0, 100) for _ in range(50)]

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            
            if self.sorting:
                
                try:
                    next(self.sorting_algorithm_generator) # type: ignore
                except StopIteration:
                    self.sorting = False
                    
            else:
                self.draw_info.draw(BLACK)
            
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
                        
                    if event.key == K_SPACE and not self.sorting: #type: ignore
                        self.sorting = True
                        self.sorting_algorithm_generator = bubble_sort(self.draw_info)

            # B. Draw Routine
            self.draw_info.draw(self.BACKGROUND_COLOR)
            pygame.display.update()

if __name__ == "__main__":
    app = Main()
    app.run()