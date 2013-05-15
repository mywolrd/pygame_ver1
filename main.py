import sys, os, time
from Managers import GameManager, LevelManager, EventManager, ResourceManager
import stages.levels as lvl

import pygame as pg
from pygame.locals import *

def main():

    evmgr = EventManager()
    gamemgr = GameManager(evmgr)
    inputmgr = InputManager(evmgr)
    levelmgr = LevelManager(evmgr)

    gamemgr.run()
    
if __name__ == "__main__":
    main()
