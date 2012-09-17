#8x8 ascii editor
#Nick Faro
#Fontslicer is the stupidly-named character image handler

import pygame
from pygame.locals import *

import string

class Font:
    def __init__(self, filename):
        self.fontfile = pygame.image.load(filename)

        self.fontdict = {}

        slicex = 0
        slicey = 0

        #Chop each tile into a list element
        for letter in string.ascii_uppercase:
            newsurf = pygame.Surface((8, 8))
            newsurf.set_colorkey((255, 0, 255))
            newsurf.blit(self.fontfile, (0, 0), (slicex, slicey, 8, 8))
            self.fontdict[letter] = newsurf
            if slicex > 128: slicex = 8; slicey += 8
            slicex += 8
            

        #Finished
        #The following code really sucks, please ignore it.
        newsurf = pygame.Surface((8, 8))
        newsurf.set_colorkey((255, 0, 255))
        newsurf.blit(self.fontfile, (0, 0), (0, 8, 8, 8))
        self.fontdict['Q'] = newsurf

        newsurf = pygame.Surface((8, 8))
        newsurf.set_colorkey((255, 0, 255))
        newsurf.blit(self.fontfile, (0, 0), (8, 8, 8, 8))
        self.fontdict['R'] = newsurf

        newsurf = pygame.Surface((8, 8))
        newsurf.set_colorkey((255, 0, 255))
        newsurf.blit(self.fontfile, (0, 0), (120, 8, 8, 8))
        self.fontdict['NULL'] = newsurf

        self.fontdict[' '] = pygame.Surface((8, 8)).convert_alpha()


    def renderstring(self, string):
        newsurf = pygame.Surface((len(string) * 8, 8)).convert_alpha()
        i = 0
        for letter in string:
            newsurf.blit(self.getletter(letter), (i * 8, 0))
            i += 1

        return newsurf
            

    def getletter(self, letter):
        letter = letter.upper()
        try: return self.fontdict[letter]
        except KeyError: return self.fontdict['NULL']

class Charsheet:
    def __init__(self, filename):
        self.fontfile = pygame.image.load(filename)
        self.fontfile.set_colorkey(self.fontfile.get_at((0, 0)))
        
        self.charcount = (self.fontfile.get_width() // 8) * (self.fontfile.get_width() // 8)
            
        self.charlist = []
            
        #Loop through every character
        for y in range(self.fontfile.get_height() // 8):
            for x in range(self.fontfile.get_width() // 8):
                newsurf = pygame.Surface((8, 8))
                newsurf.set_colorkey((255, 0, 255))
                newsurf.blit(self.fontfile, (0, 0), (x * 8, y * 8, 8, 8))
                self.charlist.append(newsurf)
    
    
    def getchar(self, number):
        return self.charlist[number]







