#Input Engine, just delivers inputs back
#Programmed by SapperEngineer

import sys
import pygame
from pygame.locals import *


#When using this, be sure to first do copybuffer,
#Process the events, and then delbuffer.


class Inputengine:
    def __init__(self):
        self.eventlist = []
        self.mousepushes = {1 : False, 2 : False, 3 : False}

    def copybuffer(self):
        for item in pygame.event.get():
            self.savemouse(item)
            self.eventlist.append(item)

    def savemouse(self, event):
        if event.type == MOUSEBUTTONDOWN:
            #print(event.button)
            self.mousepushes[event.button] = True

        elif event.type == MOUSEBUTTONUP:
            self.mousepushes[event.button] = False

    def getbuffer(self):
        return self.eventlist

    def delbuffer(self):
        self.eventlist = []

    def showbuffer(self):
        print(self.eventlist)

    def buffernotempty(self):
        return self.eventlist != []

    def getkeys(self): #Generator!
        for event in self.eventlist:
            if event.type == KEYDOWN:
                yield event.key

    def getchars(self):
        for event in self.eventlist:
            if event.type == KEYDOWN:
                yield event.unicode

    def charpushed(self, char):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.unicode == char:
                return True

        return False


    def keypushed(self, key):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.key == key:
                return True

        return False

    def keyrelease(self, key):
        for event in self.eventlist:
            if event.type == KEYUP and event.key == key:
                return True

        return False

    def mousepushed(self, button):
        for event in self.eventlist:
            if event.type == MOUSEBUTTONUP and event.button == button:
                return True

        return False

    def mousemotion(self):
        for event in self.eventlist:
            if event.type == MOUSEMOTION:
                return event.rel

        return False

    def mouserelease(self, button):
        for event in self.eventlist:
            if event.type == MOUSEBUTTONUP and event.button == button:
                return True

        return False

    def mouseispushed(self, button):
        return self.mousepushes[button] 


    def killifrequest(self):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.key == K_ESCAPE:sys.exit()
            if event.type == QUIT: sys.exit()
