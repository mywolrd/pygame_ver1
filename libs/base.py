from pygame.locals import *
import pygame as pg

# Tiles, stationary objects that do not have
# multiple sprites representing itself.
class BaseSprite(pg.sprite.DirtySprite):
    def __init__(self, sprite, topleft):
        super(BaseSprite, self).__init__(self)
        self.dirty = 1
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self):
        pass

# For character objects, which may have motions.

class BaseSpriteSheet(pg.sprite.DirtySprite):
    def __init__(self, spritesheet, sheetinfo):
        super(BaseSpriteSheet, self).__init__(self)
        self.dirty = 2
        self.sheet = spritesheet
        self.sheetinfo = sheetinfo
        self.currentmotion = None
        self.currentindex = 0

    def update(self):
        pass

class Tile(BaseSprite):
    def __init__(self, sprite):
        super(Tile, self).__init__(self, sprite)
        self.collidable = False

    def isCollidable(self):
        self.collidable = True

class Liveling(BaseSpriteSheet):
    def __init__(self, spritesheet, sheetinfo):
        super(BaseSpriteSheet, self).__init__(self, spritesheet, sheetinfo)

    def is_in_vision(self, char):
        pass

    def update(self):
        pass
