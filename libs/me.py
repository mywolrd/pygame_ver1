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

    def update(self, ev, collidables):

        update_pos = (0, 0)

        # if any of four moves(up, down, right, left) is entered
        # update self.posx, self.posy. self.posx, self.posy is top-left
        # coordinate of this image on the screen.
        if ev == UP:
            update_pos = (0, self.speed)
        elif ev == DOWN:
            update_pos = (0, -self.speed)
        elif ev == LEFT:
            update_pos = (-self.speed, 0)
        elif ev == RIGHT:
            update_pos = (self.speed, 0)
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

        # check for collision. If there is, don't update.
        if not pg.sprite.spritecollideany(self, collidables):
            pass
            
        self.rect.topleft = (self.posx, self.posy)
        
                    
        # change self.image to the next motion in spritesheet
        if animindex == INDEXMAX:
            animindex = 0
        else:
            animindex += 1
        


    
