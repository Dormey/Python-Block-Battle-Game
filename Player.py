import pygame
pygame.init()

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 13
        self.dir_r = True
        self.colour = (65, 213, 215)

    def movementSwitch(self):
        if self.dir_r == False:
            self.speed = 13
            self.dir_r = True
        elif self.dir_r == True:
            self.speed = -13
            self.dir_r = False
    
    def obstCollisions(self, cList):
        collisionList = self.rect.collidelistall(cList)
        if collisionList !=[]:
            return cList[collisionList[0]]
        else:
            return False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setColour(self,c):
        self.colour = c
          
    def update(self,window):
        if self.dir_r == True and self.x + self.width < 800:
            self.x += self.speed
        elif self.dir_r == False and self.x > 5:
            self.x += self.speed
        else:
            self.movementSwitch()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        pygame.draw.circle(window,(255,255,255),(self.x+self.width/2,self.y+self.height/2),25)
        pygame.draw.circle(window,(0,0,0),(self.x+self.width/2,self.y+15),10)
    