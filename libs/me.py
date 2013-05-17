from base import BaseSpriteSheet
from pygame.locals import *
import pygame as pg

WALK = 5
RUN = 10
INDEXMAX = 2

class Me(BaseSpriteSheet):
    def __init__(self, spritesheet, sheetinfo):
        super(Me, self).__init__(spritesheet, sheetinfo)
        self.speed  = WALK
        self.animation = LEFT
        self.posx = None
        self.posy = None

    def update(self, ev):

        # if any of four moves(up, down, right, left) is entered
        # update self.position. self.position is top-left coordinate
        # of this sprite.

        if ev == UP:
            self.posy += self.speed
        elif ev == DOWN:
            self.posy -= self.speed
        elif ev == LEFT:
            self.posx -= self.speed
        elif ev == RIGHT:
            self.posx += self.speed
        elif ev == DEAD:
            pass
        elif ev == RUN:
            # change speed when RUN event has occurred.
            if self.speed == RUN:
                self.speed = WALK
            else:
                self.speed = RUN
        
        if self.animation != ev:
            self.animation = ev
        
        self.image = (self.spritesheet[animation])[animindex]
        self.rect = image.get_rect()
        self.rect.topleft = (self.posx, self.posy)

        # change self.image to the next motion in spritesheet
        if animindex == INDEXMAX:
            animindex = 0
        else:
            animindex += 1
        


    
