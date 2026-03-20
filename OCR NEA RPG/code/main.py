import pygame
from settings import *
from player import player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint

class game:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption('RPG')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        #sprites
        self.player = player((400, 300), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x, y = randint(0, window_width), randint(0, window_height)
            w, h = randint(60, 100), randint(50, 100)
            CollisionSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))

    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        print(map)

    def run(self):
        while self.running:
            #dt
            dt = self.clock.tick() / 1000 #60 fps cap

            #event loop 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #update
            self.all_sprites.update(dt)

            #draw
            self.screen.fill(pink)
            self.all_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()

        
if __name__ == '__main__':
    game = game()
    game.run()


#plain surface
surf = pygame.Surface((100,200))
surf.fill(white)
x=100
y=150

