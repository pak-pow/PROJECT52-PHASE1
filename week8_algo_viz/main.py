import pygame #type: ignore
import math
import random
import sys

from pygame.locals import *  # type: ignore

class Main:
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BACKGROUND_COLOR = BLACK
    
    CLOCK = pygame.time.Clock()
    FPS = 60

    def  __init__(self):
        pygame.init()
        
        self.DISPLAY_WIDTH = 800
        self.DISPLAY_HEIGHT = 600
        self.DISPLAY = pygame.display.set_mode((self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT))
        
        pygame.display.set_caption("Sorting Algorithm Visualizer")
    
    def run(self):
        
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT: #type: ignore
                    pygame.quit()
                    sys.exit()
    
if __name__ == "__main__":
    app = Main()
    app.run()