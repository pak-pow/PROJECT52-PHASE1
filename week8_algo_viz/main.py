import pygame #type: ignore
import math
import random
import sys

from pygame.locals import *  # type: ignore

class DrawInformation:
    SIDE_PAD = 100  
    TOP_PAD = 150   

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = Main.DISPLAY
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        
class Main:
    
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BACKGROUND_COLOR = BLACK
    
    CLOCK = pygame.time.Clock()
    FPS = 60
    
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
    
    def  __init__(self):
        pygame.display.set_caption("Sorting Algorithm Visualizer")

    def run(self):
        
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT: #type: ignore
                    pygame.quit()
                    sys.exit()
                    
            self.DISPLAY.fill(self.BACKGROUND_COLOR)
            pygame.display.update()
    
if __name__ == "__main__":
    app = Main()
    app.run()