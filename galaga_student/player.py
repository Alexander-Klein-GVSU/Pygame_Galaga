import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Instantiates player.
        self.image = pg.image.load(os.path.join('galaga_student/assets', 'Ship6.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 65
        self.rect.centery = 384
        
    # Draws Player
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Moves Player up.
    def up(self, delta):
        if (self.rect.centery > 0):
            if (self.rect.centery >= 5):
                self.rect.centery -= 5
            else:
                self.rect.centery = 0

    # Moves Player down.
    def down(self, delta):
        if (self.rect.centery < 768):
            if (self.rect.centery <= 763):
                self.rect.centery += 5
            else:
                self.rect.centery = 768
