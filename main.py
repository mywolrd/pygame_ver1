import sys, os, time
from Manager import Manager
import stages.levels as lvl

import pygame as pg
from pygame.locals import *

def main():
    
    myMgr = Manager()
    lvl0 = lvl.level0(myMgr)
    lvl0.run(input)

#make an input handler class        
def input(events):
    for event in events:
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit(0)
            

if __name__ == "__main__":
    main()
