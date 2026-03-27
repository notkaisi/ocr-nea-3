from settings import *
import pygame

class Battle:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('Battle')
        self.clock = pygame.time.Clock()
        self.running = True