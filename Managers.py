import os, sys
from pygame.locals import *
import pygame as pg
import stages.levels as levels

class ResourceManager:
    def __init__(self):

        self.images = {}
        self.sounds = {}
        self.sprites = {}

        zombie = {K_DOWN : [(0,0,32,36), (46,0,32,36), (92,0,32,36)],
                  K_RIGHT : [(0,36,32,36), (46,36,32,36), (92,36,32,36)],
                  K_UP : [(0,72,32,36), (46,72,32,36), (92,72,32,36)],
                  K_LEFT : [(0,108,32,36), (46,108,32,36), (92,108,32,36)]}

        self.load_resources("img", self.load_img, self.images)
        self.load_resources("snd", self.load_sound, self.sounds)
 
        self.load_spritesheet("zombie", zombie)

        self.fullscreen_dim = pg.display.list_modes()[0]

    # load a sprite sheet to a dictionary that maps an animation name
    # and images that make up animation.
    # sheetinfo is a dictionary that maps an animation name
    # to a list of PyGame rectangle coordinates
    def load_spritesheet(self,name,sheetinfo):
        
        spriteimage = self.images[name]
        dic = {}

        for key, value in sheetinfo.iteritems():
            for coordinates in value:
                rect = pg.Rect(coordinates)
                image = spriteimage.subsurface(rect)
                image.convert()
                dic.setdefault(key, []).append(image)
        self.sprites[name] = dic

    # creates pygame.image with a given name
    # name : name of an image file
    def load_img(self, name):
        try:
            image = pg.image.load(name)
        except pg.error, message:
            print "FAILED LOADING AN IMAGE ", name
            raise SystemExit, message
        return image

    # creates pygame.mixer.Sound with a given name
    # name : name of a sound file
    def load_sound(self, name):
        class NoneSound:
            def play(self): pass
        if not pg.mixer:
            return NoneSound()
        try:
            # Sound does not work. change to a class of a file name with 
            # mixer.music.load, play, stop maybe
            sound = pg.mixer.Sound(name)
        except pg.error, message:
            print "FAILED LOADING SOUND ", name
            raise SystemExit, message
        return sound

    # load all resources in a directory
    # rtype : resource type which is also a directory name for the resource type
    # func : function to be use to load 'rtype' resources
    #        image files use load_img
    #        sound files use load_sound
    # dic  : dictionary to hold a list of resources for each level
    def load_resources(self,rtype,func,dic):

        names = os.listdir(rtype)
        
        for name in names:
            loc = os.path.join(rtype, name)
            res = func(loc)
            
            # files will be either .ogg or .png
            # so this is enough to get rid of a file extension
            name = name[:-4]
            dic[name] = res

    # return a sprite sheet in a dictionary.
    # The dictionary maps a name to a list of PyGame Rect coordiantes.
    # Name describes the action by the images from the Rect coordinates on
    # sprite sheet.
    def get_spritesheet(self, name):
        return self.sprites[name]
                   
    # returns a PyGame image object
    def get_image(self, name):        
        return self.images[name]

    # returns a PyGame Sound object
    def get_sound(self, name):        
        return self.sounds[name]

    # returns full screen dimention tuple (width, height)
    def get_fullscreendim(self):
        return self.fullscreen_dim

# when there is an input, it calls EventManager.post to send the input.
class InputManager:
    def __init__(self, evmgr):

        self.eventmgr = evmgr
        self.eventmgr.register_listener(self)
        
    def notify(self, ev):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.eventmgr.post(event.key)
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.eventmgr.post(event.key)
            elif event.type == KEYDOWN and event.key == K_UP:
                self.eventmgr.post(event.key)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.eventmgr.post(event.key)
            #elif event.type == KEYDOWN and event.key == :
            #    print (event.key)


# holds level object that is rendered on a screen.
# when a level finishes, it calles level.next_level()
# which sends an event 'next level'. It triggers LevelManager.init_level     
class LevelManager:
    def __init__(self, evmgr):
        self.resmgr = ResourceManager()

        self.eventmgr = evmgr
        self.eventmgr.register_listener(self)

        self.lvlname = 'level0'
        self.init_level(self.lvlname)

    def set_level(self, lvl):
        self.lvl = lvl

    def get_level(self):
        return self.lvl

    # creates a level object with the given name
    def init_level(self, lvlname):
        cons = getattr(levels, lvlname)
        self.lvl = cons(self.resmgr)

    def notify(self, ev):
        # only acts on level related events
        self.lvl.notify(ev)

# in charge of mediating events to objects
# from github.com/sjbrown/writing_games_tutorial/code_example/example.py
class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
    
    # register an object for an event
    def register_listener(self, listener):
        self.listeners[listener] = 1

    # unregister an object for an event
    def unregister_listener(self, listener):
        if listener in self.listeners:
            del self.listeners[listener]

    # send an event to all registered objects
    def post(self, event):
        for listener in self.listeners:
            listener.notify(event)

class GameManager:
    def __init__(self, evmgr):
        self.init_pyGame()

        self.eventmgr = evmgr
        self.eventmgr.register_listener(self)

        self.clock = pg.time.Clock()
    
    # initializes pygame and creates a screen
    def init_pyGame(self):
        
        # initializes PyGame components
        pg.init()
        
        # enables key press and hold
        pg.key.set_repeat(50, 50)

        screen = pg.display.set_mode((800, 600), RESIZABLE)

    # returns pygame.time.Clock object
    def get_clock(self):
        return self.clock

    # sets display screen size to width = 800, height = 600
    #def set_display_mode_original(self):
    #    self.screen = pg.display.set_mode((800, 600))

    """
    need to figure out how to quit
    # pop up window for yes or no selection
    def yesno_popup(self, yesfunc, yesparam=None, nofunc, noparam=None):

        temp = gui.Container(width=WIDTH, height=HEIGHT)
        app = gui.App()

        app.init(temp)
        
        yes = gui.Button("YES")
        yes.connect(gui.CLICK, yesfunc, yesparam)
        
        no = gui.Button("NO")
        no.connect(gui.CLICK, nofunc, noparam)

        app.add(yes, 0, 0)
        app.add(no, 50, 0)

        app.paint(screen)

    def finish(self):
        py.quit()
        sys.exit(0) """

    def notify(self, ev):
        pass

    # game loop
    def run(self):
        while True:
            self.eventmgr.post(1)
