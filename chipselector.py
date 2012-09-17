#8x8 ascii editor
#Nick Faro

import fontslicer
import pygame
from pygame.locals import *

class Chipselector:
    def __init__(self, rect):
        self.surface = pygame.Surface((rect[2], rect[3]))
        self.rect = rect
    
        self.chipset = fontslicer.Charsheet("data/8x8tiles.tga")
    
        loopx = 0
        loopy = 0
        for i in range(self.chipset.charcount):
            self.surface.blit(self.chipset.getchar(i), (loopx, loopy))
            loopx += 8
            if loopx > 256: loopy += 8; loopx = 0

    def pick(self, mousepos):
        mousepos = list(mousepos)
        
        #Snap mouse click to 8x8 grid
        while mousepos[0] % 8 != 0:
            mousepos[0] -= 1
        
        while mousepos[1] % 8 != 0:
            mousepos[1] -= 1

        '''if mousepos[1] == 0: thing = 0
        if mousepos[1] == 8: thing = 1
        if mousepos[1] == 16: thing = 2
        if mousepos[1] == 24: thing = 3
        if mousepos[1] == 32: thing = 4''' #YIKES!
        offset = mousepos[1] // 8 #:D
                
        #Squick
        chipsetpos = mousepos[0] // 8 + ((mousepos[1] * 4) + offset)

        return (self.chipset.getchar(chipsetpos), chipsetpos)

        
    def getsurface(self):
        return self.surface
        
    def getrect(self):
        return self.rect
