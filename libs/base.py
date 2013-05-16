from pygame.locals import *
import pygame as pg

# Tiles, stationary objects that do not have
# multiple sprites representing itself.
class BaseSprite(pg.sprite.DirtySprite):
    def __init__(self, sprite):
        super(BaseSprite, self).__init__(self)
        self.dirty = 1
        self.image = sprite
        self.rect = self.image.get_rect()
        
    def update(self):
        pass

# For character objects, which may have motions.

class BaseSpriteSheet(pg.sprite.DirtySprite):
    def __init__(self, spritesheet):
        super(BaseSpriteSheet, self).__init__(self)
        self.dirty = 2
        self.sheet = spritesheet

    def update(self):
        pass

class Tile(BaseSprite):
    def __init__(self, sprite):
        super(Tile, self).__init__(self, sprite)


class Liveling(BaseSpriteSheet):
    def __init__(self, spritesheet):
        super(BaseSpriteSheet, self).__init__(self, spritesheet)

    def is_in_vision(self, char):
        pass
