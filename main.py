import sys, os, time
import pygame as pg
from pygame.locals import *

def main():

    pygame.init()

    window = pygame.display.set_mode((800, 600))
    screen = pygame.display.get_surface()
    pygame.display.set_caption("MOONSKI")    
    man = pygame.image.load("img/img1.png")
    hello = load_sound("snd/hello.mp3")
    time.sleep(2)
    screen = pygame.display.set_mode((800, 600), FULLSCREEN)
    size = screen.get_rect()
    man = pygame.transform.scale(man, (size.width,size.height))
    screen.blit(man, (0, 0))
    hello.play()
    pygame.display.flip()
    
    time.sleep(4)
    screen.fill((0,0,0))
    screen = pygame.display.set_mode((800, 600))

    while True:
        input(pygame.event.get())
        
def input(events):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        else:
            pass

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error, message:
        print "Cannot load sound:", wav
        raise SystemExit, message
    return sound


if __name__ == "__main__":
    main()
