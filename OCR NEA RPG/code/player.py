#player
import pygame
from settings import *
from sprites import *

class player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        #lists of images for each direction
        self.images = {
            'up': [pygame.transform.scale(pygame.image.load(f'../images/mizu/U{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'down': [pygame.transform.scale(pygame.image.load(f'../images/mizu/D{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'left': [pygame.transform.scale(pygame.image.load(f'../images/mizu/L{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
            'right': [pygame.transform.scale(pygame.image.load(f'../images/mizu/R{i}.png').convert_alpha(), (50, 80)) for i in range(3)],
        }
        self.image = pygame.transform.scale(pygame.image.load(f'../images/mizu/D0.png').convert_alpha(), (50, 80))
        #self.image = self.images[self.direction_facing][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect.inflate(-5, -10)
        #movement
        self.direction = pygame.Vector2()
        self.speed = 300
        self.collision_sprites = collision_sprites

    #def load_images(self):
        #self.frames = {'left': [],'right': [],'up': [],'down': [],}
        #self.direction_facing = 'down'
        #self.frame_index = 0

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
   
    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                #print('overlap', random.randint(0,100))
                if direction=='horizontal':
                    if self.direction.x>0: self.hitbox_rect.right=sprite.rect.left
                    if self.direction.x<0: self.hitbox_rect.left=sprite.rect.right
                    #player moving left & right
                else:
                    if self.direction.y>0: self.hitbox_rect.bottom=sprite.rect.top
                    if self.direction.y<0: self.hitbox_rect.top=sprite.rect.bottom
                    #player moving up and down

    def update(self, dt):
        self.input()
        self.move(dt)