import os
import pygame as pg

from player import Player

class Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemies):
        super(Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('galaga_student/assets', 'shot.png')).convert_alpha()
        for e in enemies:
            if (isinstance(e, Player)):
                self.image = pg.transform.flip(self.image, True, True)
            break
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 100
        self.rect.centery = shipLocation.y + 37
        self.enemies = enemies
        self.event = pg.USEREVENT + 1
        self.fireSound = pg.mixer.Sound(os.path.join('galaga_student/assets', 'fire.wav'))
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound(os.path.join('galaga_student/assets', 'explosion.wav'))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        for e in self.enemies:
            if (isinstance(e, Player)):
                self.rect.x -= 1000 * delta
                if self.rect.x < 0:
                    self.kill()
            else:
                self.rect.x += 1000 * delta
                if self.rect.x > 1024:
                    self.kill()
            break
        collision = pg.sprite.spritecollideany(self, self.enemies)
        if collision:
            collision.kill()
            pg.event.post(pg.event.Event(self.event))
            self.explosionSound.play()
            self.kill()
            if (isinstance(collision, Player)):
                return 0, 0
            else:
                return 1, collision
        return -1, 0

