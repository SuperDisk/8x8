#A simple Mouse Handler for offsets and updating mouserect
#Programmed by SapperEngineer

import pygame
from pygame.locals import *

import ctypes

class Mousehandler:
    def __init__(self):
        self.mouserect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
        self.mouseoffset = [0, 0]
        self.posondisplay = [0, 0]

    def update(self): #Yes, it's cheesy.
        self.mouserect.topleft = (pygame.mouse.get_pos()[0] + self.mouseoffset[0], pygame.mouse.get_pos()[1] + self.mouseoffset[1])
        
    def getrect(self):
        return self.mouserect

    def getpos(self):
        return self.mouserect.topleft

    def getposx(self):
        return self.mouserect.topleft[0]

    def getposy(self):
        return self.mouserect.topleft[1]

    def getsurfacepos(self, rect):
        rect = pygame.Rect(rect)
        return (self.getpos()[0] - rect.topleft[0], self.getpos()[1] - rect.topleft[1])

    def getsurfacerect(self, rect):
        return pygame.Rect(self.getsurfacepos(rect), (1, 1))

