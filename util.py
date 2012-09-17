#Utilities

def hoveringover(mousehandler, element):
    return mousehandler.getrect().colliderect(element.getrect())
