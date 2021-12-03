import os
import pygame as pg

# Complete me! - FIXME
class Enemy(pg.sprite.Sprite):
    def __init__(self, location):
        super(Enemy, self).__init__()
        # TODO
        self.image = pg.image.load(os.path.join('galaga_student/assets', 'Ship3.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = location[0]
        self.rect.centery = location[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        pass

    def down(self, delta):
        pass