from pygame.locals import *
import pygame as pg

# Tiles, stationary objects that do not have
# multiple sprites representing itself.
#
# sprite is an image object from ResourceManager
# topleft is the topleft coordinate of this object on the display
class BaseSprite(pg.sprite.DirtySprite):
    def __init__(self, sprite, topleft):
        super(BaseSprite, self).__init__()
        self.dirty = 1
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

    def update(self):
        pass

class Tile(BaseSprite):
    def __init__(self, sprite):
        super(Tile, self).__init__(self, sprite)
        self.collidable = False

    def isCollidable(self):
        self.collidable = True

# For character objects, which may have motions.
# 
# spritesheet is an image object/file containing bunch of sprites
# sheetinfo is a dictionary - 
class BaseSpriteSheet(pg.sprite.DirtySprite):
    def __init__(self, spritesheet):
        super(BaseSpriteSheet, self).__init__()
        self.dirty = 2

        self.spritesheet = spritesheet
        
        self.animindex = 0

    def update(self, ev):
        pass
