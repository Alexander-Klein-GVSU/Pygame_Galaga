import os
import pygame as pg

# Complete me! - TODO
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship3.png')).convert_alpha()

# Complete me! - FIXME
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # TODO

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        pass

    def down(self, delta):
        pass