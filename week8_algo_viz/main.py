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
    
    # added new shades of grays
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        # Grab the active window
        self.window = pygame.display.get_surface()
        self.set_list(lst)
        
        # font setup
        self.font = pygame.font.SysFont('Ariel', 30)
        self.large_font = pygame.font.SysFont('Ariel', 40)

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
    def draw(self, bg_color, algo_name, ascending, color_positions={}):
        self.window.fill(bg_color)
        
        # added selection sort to the HUD
        direction = "Ascending" if ascending else "Descending"
        title_text = f"{algo_name} - {direction}"
        controls_1 = "R: Reset | SPACE: Start | A: Ascending | D: Descending"
        controls_2 = "I: Insertion | B: Bubble | S: Selection | H: Heap"
        
        title_surface = self.large_font.render(title_text, 1, BLUE)
        controls_1_surface = self.font.render(controls_1, 1, WHITE)
        controls_2_surface = self.font.render(controls_2, 1, WHITE)
        
        self.window.blit(title_surface, (self.width/2 - title_surface.get_width()/2, 5))
        self.window.blit(controls_1_surface, (self.width/2 - controls_1_surface.get_width()/2, 45))
        self.window.blit(controls_2_surface, (self.width/2 - controls_2_surface.get_width()/2, 75))
        
        for i, val in enumerate(self.lst):
            # Math to place bars correctly
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height
            
            color = self.GRADIENTS[i % 3] #type: ignore
            
            if i in color_positions:
                color = color_positions[i]
            # Draw Rectangle: (Surface, Color, (x, y, width, height))
            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height))
        pygame.display.update()

# Bubble sort
def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    
    # standard bubble sort loop
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            
            # compare adjacent numbers
            if (ascending and num1 > num2) or (not ascending and num1 < num2):
                
                # swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
                # visualizing: the draw on swap immediently
                # coloring the two bars being swapped red and green
                draw_info.draw(BLACK, "Bubble Sort", ascending, {j: GREEN, j+1: RED})
                
                # pause: yield control back to the main loop
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    for i in range(1, len(lst)):
        current = lst[i]
    
        while True:
            if i == 0:
                break
            
            if ascending and lst[i - 1] > lst[i]:
                swap = True
            elif not ascending and lst[i - 1] < lst[i]:
                swap = True
            else:
                swap = False
                
            if not swap:
                break
            
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            draw_info.draw(BLACK, "Insertion Sort", ascending, {i - 1: GREEN, i: RED})
            yield True
            i -= 1
            
    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        target_idx = i
        for j in range(i + 1, len(lst)):
            
            # The Magic Flip
            if (ascending and lst[j] < lst[target_idx]) or (not ascending and lst[j] > lst[target_idx]):
                target_idx = j
                
        if target_idx != i:
            lst[i], lst[target_idx] = lst[target_idx], lst[i]
            draw_info.draw(BLACK, "Selection Sort", ascending, {i: GREEN, target_idx: RED})
            yield True
            
    return lst

def heapify(draw_info, n, i, ascending):
    lst = draw_info.lst
    target = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if ascending:
        if left < n and lst[left] > lst[target]:
            target = left
        if right < n and lst[right] > lst[target]:
            target = right
        
    else:
        if left < n and lst[left] < lst[target]:
            target = left
        if right < n and lst[right] < lst[target]:
            target = right
            
    if target != i:
        lst[i], lst[target] = lst[target], lst[i]
        draw_info.draw(BLACK, "Heap Sort", ascending, {i: GREEN, target: RED})
        yield True
        
        yield from heapify(draw_info, n, target, ascending)
    

def heap_sort(draw_info, ascending = True):
    lst = draw_info.lst
    n = len(lst)
    
    for i in range(n // 2 - 1, -1, -1): 
        yield from heapify(draw_info, n,i,ascending)
        
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_info.draw(BLACK, "Heap Sort", ascending, {i: GREEN, 0: RED})
        yield True
        
        yield from heapify(draw_info, i, 0, ascending)
        
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
        self.ascending = True 
        self.sorting_algorithm = bubble_sort
        self.sorting_algo_name = "Bubble Sort"
        self.sorting_algorithm_generator = None
        
    def generate_starting_list(self):
        # Generate 50 random numbers between 0 and 100
        return [random.randint(0, 200) for _ in range(100)]

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
                self.draw_info.draw(BLACK, self.sorting_algo_name, self.ascending)
            
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
                        self.sorting = False
                        
                    if event.key == K_SPACE and not self.sorting: #type: ignore
                        self.sorting = True
                        self.sorting_algorithm_generator = self.sorting_algorithm(self.draw_info, self.ascending)
                        
                    # NEW: A = Ascending
                    elif event.key == K_a and not self.sorting: #type: ignore
                        self.ascending = True
                        
                    # NEW: D = Descending
                    elif event.key == K_d and not self.sorting: #type: ignore
                        self.ascending = False
                        
                    # I = Switch to Insertion Sort
                    elif event.key == K_i and not self.sorting: #type: ignore
                        self.sorting_algorithm = insertion_sort
                        self.sorting_algo_name = "Insertion Sort"
                    
                    # B = Switch to Bubble Sort
                    elif event.key == K_b and not self.sorting: #type: ignore
                        self.sorting_algorithm = bubble_sort
                        self.sorting_algo_name = "Bubble Sort"
                        
                    elif event.key == K_s and not self.sorting: #type: ignore
                        self.sorting_algorithm = selection_sort
                        self.sorting_algo_name = "Selection Sort"
                        
                    elif event.key == K_h and not self.sorting: #type: ignore
                        self.sorting_algorithm = heap_sort
                        self.sorting_algo_name = "Heap Sort"

if __name__ == "__main__":
    app = Main()
    app.run()