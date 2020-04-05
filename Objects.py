import pygame
pygame.init()

class Object():
    def __init__(self,x, y, t):
        self.width = 120 -(60*t)
        self.height = 120 -(60*t)
        self.x = x
        self.y = y
        self.type = t
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colours = [(0,0,0),(65, 213, 215)]
        self.colour = self.colours[t]
        self.speed = 13.5

    def moveDown(self):
        self.y += self.speed

    def isVisible(self):
        if self.y <750:
            return True
        else:
            return False
   
    def update(self,window):
        self.moveDown()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.type == 0:
            pygame.draw.rect(window, self.colour, self.rect)
        else:
            pygame.draw.circle(window, self.colour,(self.x+self.width/2,self.y+self.height/2),30)


class TrailBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (55, 203, 205)
        self.speed = 13

    def moveDown(self):
        self.y += self.speed

    def setColour(self,c):
        self.colour = c

    def update(self,window):
        self.moveDown()
        pygame.draw.circle(window, self.colour,(self.x,self.y), 30)


class Projectile():
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.colours = [(65, 213, 215),(252, 73, 73)]
        self.colour = self.colours[t]
        self.speed = 19
        self.type = t
        self.rect = pygame.Rect(self.x - 30, self.y - 30 ,30,30)

    def moveUpOrDown(self):
        if self.type == 0:
            self.y -= self.speed
        else:
            self.y += self.speed
    
    def getType(self):
        return self.type

    def update(self,window):
        self.moveUpOrDown()
        self.rect = pygame.Rect(self.x - 30, self.y - 30 ,30,30)
        pygame.draw.circle(window, self.colour,(self.x,self.y), 30)