#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from pygame.locals import *
from pygame import mixer
from pygame.sprite import Group
import random


def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    # Create a player
    players = pg.sprite.Group()
    player = Player()
    players.add(player)

    # Create enemy and projectile Groups
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()

    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i, j))
            enemies.add(enemy)

    # Start sound - Load background music and start it
    # playing on a loop
    mixer.init()
    mixer.music.load(os.path.join('galaga_student/assets', 'cpu-talk.wav'))
    mixer.music.play(-1)

    # Load background image.
    background = pg.image.load(os.path.join('galaga_student/assets', 'space.png'))

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    # Make a tuple for FONTCOLOR
    FONTCOLOR = (56, 69, 159)
    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 250
    # Make sure enemy can't fire more than once every second.
    eShotDelta = 1000
    # Sprite hit
    hit = -1
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()


    clock.tick(fps)
    # Setup score variable
    score = 0
    while running:

        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100

        keys = pg.key.get_pressed()

        if keys[K_s]:
            player.down(delta)
        if keys[K_w]:
            player.up(delta)
        if keys[K_SPACE]:
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies)
                projectiles.add(projectile)
                shotDelta = 0

        # Ok, events are handled, let's update objects!
        player.update(delta)
        bounce = 0
        shooter = -1
        iter = 0
        if (eShotDelta) >= 1.0:
            shooter = random.randint(0, len(enemies))
            eShotDelta = 0.0
        for enemy in enemies:
            bounce = enemy.update(delta)
            # Check for bounce so all enemy ships change direction at the same time.
            if (bounce > 0):
                for en in enemies:
                    if (bounce == 1):
                        en.setDirection(1)
                    else:
                        en.setDirection(0)
                break
            if (shooter == iter):
                projectile = Projectile(enemy.rect, players)
                projectiles.add(projectile)
            iter += 1

        for projectile in projectiles:
            hit, collision = projectile.update(delta)
            if (hit == 1):
                enemies.remove(collision)
            elif (hit == 0):
                break
        
        if (hit == 0 or (len(enemies) == 0)):
            break

        # Objects are updated, now let's draw!
        screen.blit(background, (0, 0))
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # How much time has passed this loop?
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta
        eShotDelta += delta

    # Game Over Screens
    screen.fill((0, 0, 0))
    if (hit == 0):
        font.render_to(screen, (190, 400), "ur bad lmao", (255, 0, 0), None, size=100)
        mixer.music.load(os.path.join('galaga_student/assets', 'lose.wav'))
        mixer.music.play()
    else:
        font.render_to(screen, (100, 400), "conglat your'e winer", (255, 215, 0), None, size=80)
        score += 100
        mixer.music.load(os.path.join('galaga_student/assets', 'poggers.wav'))
        mixer.music.play()
    font.render_to(screen, (350, 200), "Score: " + str(score), FONTCOLOR, None, size=64)
    pg.display.flip()
    pg.time.wait(10000)

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
