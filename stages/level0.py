from libs.me import Me
import pygame as pg
from pygame.locals import *

class level0:
    def __init__(self, resmgr):
        self.resmgr = resmgr

        #self.images = self.resmgr.get_images("level0")
        #self.sounds = self.resmgr.get_sounds("level0")
        
        #self.hello = self.sounds["hello.mp3"]
        #self.man = self.images["img2.png"]
        
        self.screendim = (1000, 700)
        self.screen = pg.display.get_surface()
        #self.resmgr.load_spritesheet("me", ())
        #self.screendim = self.resmgr.get_fullscreendim()
        #self.mandim = self.man.get_size()
        self.player = Me(self.resmgr.get_spritesheet("zombie"))
        self.player.setPosition((500, 500))
        
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.player)

        self.background = pg.Surface(self.screen.get_size())
        self.background.fill((250, 250, 250))
        self.background = self.background.convert()
        
    def run(self):
        surface = pg.display.get_surface()
        osize = surface.get_size()

        screen = pg.display.set_mode(self.screendim, RESIZABLE)
 
        centerx, centery = screen.get_rect().center
        
        delay = 1000
        i = 0

        while i < 5:
            
            screen.fill((0,0,0))

            sizex, sizey = self.calculate_size(i)
            self.man = pg.transform.scale(self.man, (sizex, sizey))

            screen.blit(self.man, (centerx - int(sizex/2), 
                                   centery - int(sizey/2)))
            pg.display.flip()
            self.hello.play()
            pg.time.delay(500)
            
            #1000, 1000, 500, 500/3, 500/12 updates
            #images will get bigger each time it updates
            pg.time.delay(delay)            
            i += 1
            delay /= i
        
        pg.display.set_mode((800, 600), RESIZABLE)
        #self.resmgr.set_display_mode_original()

    # everything happens in there.
    # master game loop will call this.
    def notify(self, ev):
        self.update(ev)

    def update(self, ev):        
        self.player.update(ev)
        self.draw()

    def draw(self, ev=None):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        pg.display.flip()
        
    def calculate_size(self, i):

        percent = (i+1) * 0.2

        scrwidth, scrheight = self.screendim
        imgwidth, imgheight = self.mandim
        
        height = scrheight * percent
        ratio = height/imgheight

        return (int(imgwidth*ratio), int(height))

    def next_level(self):
        pass

    
    

