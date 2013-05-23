from base import BaseSpriteSheet

WALK = 6
RUN = 12
INDEXMAX = 2

class Liveling(BaseSpriteSheet):
    def __init__(self, spritesheet, sheetinfo):
        
        super(Liveling, self).__init__(spritesheet, sheetinfo)
        
        # A pair of coordinates representing
        # start, end point of this.path.
        # or it can be a spline.
        self.path = None
        self.speed = WALK
        

    # for each AI, pre-define a route to follow and stick on to it.
    # for more advanced AIs, make them able to leave their route
    # when a certain event occurs and move back to their old route
    # or give them a new route.
    def update(self):
        pass

    # visibility check
    def is_in_sight(self):
        pass
