import pygame
pygame.init()

#Enemy class which shoot at the player
class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 11
        self.img = pygame.image.load("assets/enemy.png").convert()

    #Move the enemy down until it reaches the desired y 
    def moveDown(self):
        if self.y < 5:
            self.y += 5

    #Move enemy sideways and change direction when it hits a point
    def moveSideways(self):
        if self.x + self.width > 800:
            self.speed = -11
        elif self.x < 0:
            self.speed = +11
        self.x += self.speed

    #Player update method, movement and drawing character
    def update(self,window):
        self.moveDown()
        self.moveSideways()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)    
        window.blit(self.img, self.rect)
