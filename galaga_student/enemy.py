import os
import pygame as pg

# Complete me! - TODO
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship3.png')).convert_alpha()