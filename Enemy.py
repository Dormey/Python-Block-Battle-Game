import pygame
pygame.init()

class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 11
        self.img = pygame.image.load("assets/enemy.png").convert()

    def moveDown(self):
        if self.y < 5:
            self.y += 1

    def moveSideways(self):
        if self.x + self.width > 800:
            self.speed = -11
        elif self.x < 0:
            self.speed = +11
        self.x += self.speed
        
    def obstCollisions(self, cList):
        collisionList = self.rect.collidelistall(cList)
        if collisionList !=[]:
            return cList[collisionList[0]]
        else:
            return False
    
    def getX(self):
        return self.x

    def update(self,window):
        self.moveDown()
        self.moveSideways()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)    
        window.blit(self.img, self.rect)

