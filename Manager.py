import os
import pygame as pg
from pygame.locals import *

class Resources:
    def __init__(self):

        self.images = {}
        self.sounds = {}

        self.load_resources("img", self.load_img, self.images)
        self.load_resources("snd", self.load_sound, self.sounds)

    def load_img(self, name):
        try:
            image = pg.image.load(name)
        except pg.error, message:
            print "FAILED LOADING AN IMAGE ", name
            raise SystemExit, message
        return image

    def load_sound(self, name):
        class NoneSound:
            def play(self): pass
        if not pg.mixer:
            return NoneSound()
        try:
            sound = pg.mixer.Sound(name)
        except pg.error, message:
            print "FAILED LOADING SOUND ", name
            raise SystemExit, message
        return sound

    def load_resources(self,rtype,func,dic):

        names = os.listdir(rtype)

        for name in names:
            loc = os.path.join(rtype, name)
            res = func(loc)
            resinfo  = name.split('_')
            lvl = resinfo[0]
            name = resinfo[1]            
            dic.setdefault(lvl, []).append((name, res))
       
    def get_images(self, lvlname):
        return self.images[lvlname]

    def get_sounds(self, lvlname):
        return self.sounds[lvlname]

class Manager:
    def __init__(self):
        self.init_pyGame()


        self.res = Resources()        
        self.clock = pg.time.Clock()
    
    def init_pyGame(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600), RESIZABLE)
        self.fullscreen_dim = pg.display.list_modes()[0]

    def get_fullscreendim(self):
        return self.fullscreen_dim

    # returns a dictionary of resources for the level "lvlname"
    # key : image name
    # value : pygame.image object
    def get_images(self, lvlname):        
        dic = {}
        reslist = self.res.get_images(lvlname) 
        for name, obj in reslist:
            dic[name] = obj
        return dic

    # returns a dictionary of resources for the level "lvlname"
    # key : sound name
    # value : pygame.mixer.Sound object
    def get_sounds(self, lvlname):
        dic = {}
        reslist = self.res.get_sounds(lvlname)
        for name, obj in reslist:
            dic[name] = obj
        return dic

    def get_clock(self):
        return self.clock

    def set_display_mode_original(self):
        self.screen = pg.display.set_mode((800, 600))
