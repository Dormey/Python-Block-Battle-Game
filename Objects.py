import pygame
pygame.init()

#Objects class (rect obstacles, coloured objects)
#These are the objects that move down the screen and can be collided with
class Object():
    def __init__(self,x, y,c):
        self.width = 120 -(60*c)
        self.height = 120 -(60*c)
        self.x = x
        self.y = y
        self.op = c
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colours = [(0,0,0),(65, 213, 215)]
        self.colour = self.colours[c]
        self.speed = 13.5

    #Move downwards at set speed
    def moveDown(self):
        self.y += self.speed

    #Check if object is still visible on screen
    def isVisible(self):
        if self.y <750:
            return True
        else:
            return False
   
   #Object update method, move down and draw object 
    def update(self,window):
        self.moveDown()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.op == 0:
            pygame.draw.rect(window, self.colour, self.rect)
        else:
            pygame.draw.circle(window, self.colour,(self.x+self.width/2,self.y+self.height/2),30)

#Trail block class, these become like a tail for the player and act as extra lives
class TrailBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (55, 203, 205)
        self.speed = 13

    #Move trail block down a set speed
    def moveDown(self):
        self.y += self.speed

    #Set colour of the trailblock
    def setColour(self,c):
        self.colour = c

    #Trail block update method, move down and draw object
    def update(self,window):
        self.moveDown()
        pygame.draw.circle(window, self.colour,(self.x,self.y), 30)

#Projectile class
class Projectile():
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.colours = [(65, 213, 215),(252, 73, 73)]
        self.colour = self.colours[t]
        self.speed = 18 +(2*t)
        self.type = t

    #Move up or down depending on if it is a player projectile or enemy projectile (type)
    def moveUpOrDown(self):
        if self.type == 0:
            self.y -= self.speed
        else:
            self.y += self.speed

    #Projectile update method, movement and draw object
    def update(self,window):
        self.moveUpOrDown()
        pygame.draw.circle(window, self.colour,(self.x,self.y), 30)