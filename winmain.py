#8x8 ascii editor
#Nick Faro

#Imports
import drawboard
import chipselector
import fontslicer

#Reusable
import inputengine
import mousehandler

import pygame
from pygame.locals import *

import util


class Winmain:
    def __init__(self):
        pygame.init()

        self.tv = pygame.display.set_mode((400, 400), DOUBLEBUF | HWACCEL) #Screen

        pygame.display.set_caption("8x8 Ascii Character Mapper")

        self.fontslicer = fontslicer.Font("data/8x8font.tga")
        self.chipset = fontslicer.Charsheet("data/8x8tiles.tga")

        self.drawboard = drawboard.Drawboard((40, 40, 296, 296)) 	 #Drawing gui
        self.chipselector = chipselector.Chipselector((40, 360, 296, 296)) #Chip picking GUI

        #Reusable stuff
        self.inputengine = inputengine.Inputengine()
        self.mousehandler = mousehandler.Mousehandler()
    
        #Some variables
        self.placechar = (self.chipset.getchar(1), 1)

    def mainloop(self):
        while 1:
            self.tv.fill((0, 0, 0))

            #*****INPUT CODE*****
            self.mousehandler.update()
            self.inputengine.copybuffer() 

            self.inputengine.killifrequest()

            if self.inputengine.mouseispushed(1): #Do if first mousebutton is pushed
                if util.hoveringover(self.mousehandler, self.drawboard):
                    self.drawboard.draw(self.mousehandler.getsurfacepos(self.drawboard.getrect()), self.placechar)
                
                if util.hoveringover(self.mousehandler, self.chipselector):
                    self.placechar = self.chipselector.pick(self.mousehandler.getsurfacepos(self.chipselector.getrect()))
                    self.tv.blit(self.placechar[0], (0, 0))
        
            if self.inputengine.mouseispushed(3):
                self.drawboard.erase(self.mousehandler.getsurfacepos(self.drawboard.getrect()))

            self.inputengine.delbuffer()

            #*****RENDERING******
            self.tv.blit(pygame.transform.scale2x(self.fontslicer.renderstring("XEight Character Mapper")), (0, 0))
            self.tv.blit(self.drawboard.getsurface(), self.drawboard.getrect())
            pygame.draw.rect(self.tv, (255, 255, 255), self.drawboard.getrect(), 1)
            self.tv.blit(self.chipselector.getsurface(), self.chipselector.getrect())
            pygame.draw.rect(self.tv, (255, 255, 255), self.chipselector.getrect(), 1)

            with open('aw.txt', 'wb') as file:
                array = self.drawboard.getarray()
                for y in array:
                    for x in range(len(y)):
                        file.write(y[x].encode())
                    file.write("\n".encode())

            pygame.display.flip() #We don't need optimization


#Start program
winmain = Winmain()
winmain.mainloop()
