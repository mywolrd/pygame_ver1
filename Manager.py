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
            dic.setdefault(lvl, []).append(name)

    def get_resources(self, rtype, lvlname):
        if rtype == "image":
            return self.images[lvlname]
        else:
            return self.sounds[lvlname]

class Manager:
    def __init__(self):
        self.res = Resources()
        
    def initPyGame(self):
        pg.init()
