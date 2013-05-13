import sys, os, time
from Managers import Manager
import stages.levels as lvl

import pygame as pg
from pygame.locals import *

def main():
    
    gamemgr = GameManager()
    
    # should create a level manager that loads all levels
    lvl0 = lvl.level0(myMgr)
    lvl0.run()

if __name__ == "__main__":
    main()
