import os
import pygame as pg

# Complete me! - FIXME
class Enemy(pg.sprite.Sprite):
    direction = 0
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
        if (self.direction == 0):
            if (self.rect.centery > 0):
                self.rect.centery -= 1
            else:
                self.direction = 1
        else:
            if (self.rect.centery < 768):
                self.rect.centery += 1
            else:
                self.direction = 0