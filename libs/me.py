from base import BaseSpriteSheet
from pygame.locals import *
import copy
import pygame as pg

WALK = 5
RUN = 10
INDEXMAX = 2
DEAD = 200
RUN = 210

class Me(BaseSpriteSheet):
    def __init__(self, spritesheet):
        super(Me, self).__init__(spritesheet)
        self.speed  = WALK
        self.animation = K_LEFT

        self.image = (self.spritesheet[self.animation])[self.animindex]
        self.rect = self.image.get_rect()

    def setPosition(self, pos):
        self.rect.topleft = pos

    def update(self, ev, collidables=None):

        dx, dy = 0, 0

        # if any of four moves(up, down, right, left) is entered
        # update self.posx, self.posy. self.posx, self.posy is top-left
        # coordinate of this image on the screen.
        def setAnimation(ev):
            if self.animation != ev:
                self.animation = ev

        if ev == K_UP:
            dy = self.speed
            setAnimation(ev)
        elif ev == K_DOWN:
            dy = -self.speed
            setAnimation(ev)
        elif ev == K_LEFT:
            dx = -self.speed
            setAnimation(ev)
        elif ev == K_RIGHT:
            dx = self.speed
            setAnimation(ev)
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
        
        # need to make a copy of topleft corner of the next image
        # because self.rect.topleft becomes (0, 0) when I change the image.
        # an unexpected behavior but makes sense, since self.rect solely depends
        # on the self.image

        self.image = (self.spritesheet[self.animation])[self.animindex]
        copy_topleft = self.rect.topleft
        self.rect = self.image.get_rect()
        self.rect.topleft = copy_topleft

        copy_me = copy.deepcopy(self)        
        copy_me.rect.move_ip(dx, dy)

        # check for collision. If there is, don't update.
        # Boundary checks neccessary ? Not sure if PyGame takes care of it....
        # C source code does not seem to check boundaries.
        if collidables:
            if not pg.sprite.spritecollideany(copy_me, collidables):
                self.rect.move_ip(dx, dy)
            
        # change self.image to the next motion in spritesheet
        if self.animindex == INDEXMAX:
            self.animindex = 0
        else:
            self.animindex += 1
        
    def checkBounds(self, rect):
        # check if the rect is in the bound of the display
        pass
