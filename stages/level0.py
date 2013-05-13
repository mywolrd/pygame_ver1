from stage import stage
import pygame as pg
from pygame.locals import *

class level0(stage):
    def __init__(self, resource):
        super(level0, self).__init__(resource)

        self.mgr = resource
        self.images = self.mgr.get_images("level0")
        self.sounds = self.mgr.get_sounds("level0")

        self.hello = self.sounds["hello.mp3"]
        self.man = self.images["img2.png"]

        self.screendim = self.mgr.get_fullscreendim()
        self.mandim = self.man.get_size()

    def run(self, func):
        screen = pg.display.set_mode((1000, 500), RESIZABLE)

        delay = 1000
        i = 0

        while i < 5:
            
            screen.fill((0,0,0))

            size = self.calculate_size(i)
            self.man = pg.transform.scale(self.man, size)
            
            self.hello.play()
            pg.time.delay(500)
            
            #1000, 1000, 500, 500/3, 500/12 updates
            #images will get bigger each time it updates
            pg.time.delay(delay)            
            i += 1
            delay /= i
            
        while True:
            func(pg.event.get())

        self.mgr.set_display_mode_original()

    def calculate_size(self, i):

        percent = (i+1) * 0.2

        scrwidth, scrheight = self.screendim
        imgwidth, imgheight = self.mandim
        
        height = scrheight * percent
        ratio = height/imgheight

        return (int(imgwidth*ratio), int(height))

    def next_level(self):
        pass

    
    

