from base import BaseSpriteSheet
from pygame.locals import *
import copy
import pygame as pg

WALK = 5
RUN = 10
INDEXMAX = 2

class Me(BaseSpriteSheet):
    def __init__(self, spritesheet, startpos):
        super(Me, self).__init__(spritesheet)
        self.speed  = WALK
        self.animation = K_LEFT

        self.image = (self.spritesheet[animation])[animindex]
        self.rect = image.get_rect()

        self.rect.topleft = startpos
        
    def update(self, ev, collidables=None):

        dx, dy = 0, 0

        # if any of four moves(up, down, right, left) is entered
        # update self.posx, self.posy. self.posx, self.posy is top-left
        # coordinate of this image on the screen.
        if ev == K_UP:
            dy = self.speed
        elif ev == K_DOWN:
            dy = -self.speed
        elif ev == K_LEFT:
            dx = -self.speed
        elif ev == K_RIGHT:
            dx = self.speed
        elif ev == DEAD:
            # update is called when a keyboard event occurs.
            # so for DEAD to work player has to continue hold or hit DEAD key.
            # This is not desirable. Fix this. Or it may work just fine.
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
        
        copy_me = copy.deepcopy(self)
        copy_me.rect.mode_ip(dx, dy)
                                         
        # check for collision. If there is, don't update.
        # Boundary checks neccessary ? Not sure if PyGame takes care of it....
        # C source code does not seem to check boundaries.
        if collidables:
            if not pg.sprite.spritecollideany(copy_me, collidables):
                self.rect.move_ip(dx, dy)
            
        # change self.image to the next motion in spritesheet
        if animindex == INDEXMAX:
            animindex = 0
        else:
            animindex += 1
        
    def checkBounds(self, rect):
        # check if the rect is in the bound of the display
        pass
