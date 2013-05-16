from base import BaseSpriteSheet

class Liveling(BaseSpriteSheet):
    def __init__(self, spritesheet, sheetinfo):
        pass

    # for each AI, pre-define a route to follow and stick on to it.
    # for more advanced AIs, make them able to leave their route
    # when a certain event occurs and move back to their old route
    # or give them a new route.
    def update(self):
        pass

    # visibility check
    def is_in_sight(self):
        pass
