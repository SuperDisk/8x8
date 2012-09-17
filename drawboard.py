#8x8 ascii editor
#Nick Faro

import pygame
from pygame.locals import *
import inputengine

class Drawboard:
    def __init__(self, rect):
        self.surface = pygame.Surface((rect[2], rect[3]))
        self.rect = pygame.Rect(rect)
        self.array = [[' '] * (range(rect[2] // 8)[-1] + 1) for x in range(rect[3] // 8)]
        #print(self.array)

    def draw(self, mousepos, character):
        mousepos = list(mousepos)
        
        #Snap mouse click to 8x8 grid
        while mousepos[0] % 8 != 0:
            mousepos[0] -= 1

        while mousepos[1] % 8 != 0:
            mousepos[1] -= 1
            
        #self.surface.fill((0, 0, 0), (mousepos[0], mousepos[1]))
        self.array[mousepos[1] // 8][mousepos[0] // 8] = chr(character[1])
        self.surface.blit(character[0], (mousepos[0], mousepos[1]))

    def erase(self, mousepos):
        mousepos = list(mousepos)
        
        #Snap mouse click to 8x8 grid
        while mousepos[0] % 8 != 0:
            mousepos[0] -= 1
        
        while mousepos[1] % 8 != 0:
            mousepos[1] -= 1
            
        self.array[mousepos[1] // 8][mousepos[0] // 8] = ' '
        self.surface.fill((0, 0, 0), (mousepos, (8, 8)))

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.rect.topleft

    def getarray(self):
        return self.array
