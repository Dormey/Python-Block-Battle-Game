import pygame, random, sys
sys.dont_write_bytecode = True

pygame.init()

#Setup display/window and background
window = pygame.display.set_mode((800,750), pygame.SCALED)
pygame.display.set_caption("Block Battle")
bg = pygame.image.load("assets/bg.png").convert()

#Setup score text font and surface
text_font = pygame.font.SysFont("Arial", 40)
score = 1
score_surface = text_font.render("Score: {}".format(score), False, (0,0,0))

#Setup music and sound effects
music = pygame.mixer.music.load("assets/ES_Yammerer - Martin Klem.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1,0.0)

dir_sound = pygame.mixer.Sound("assets/ES_Electronic Drum 1 - SFX Producer.ogg")
dir_sound.set_volume(0.2)
trail_sound = pygame.mixer.Sound("assets/ES_Beep Electronic 1 - SFX Producer.ogg")
trail_sound.set_volume(0.3)
lose_trail_sound = pygame.mixer.Sound("assets/ES_Beep Electronic 5 - SFX Producer.ogg")
lose_trail_sound.set_volume(0.3)
die_sound = pygame.mixer.Sound("assets/ES_Hit Electronic 2 - SFX Producer.ogg")
die_sound.set_volume(0.3)

#Import player class and create player object
from Player import Player
plyr = Player(400,500)
#Import classes from Objects file
from Objects import Object
from Objects import TrailBlock
from Objects import Projectile
#Import enemy
from Enemy import Enemy
      
#Custom event and timer to spawn objects every interval and use as points interval
CUSTOM_INTERVAL_EVENT = pygame.event.custom_type()
custom_interval = 500
pygame.time.set_timer(CUSTOM_INTERVAL_EVENT, custom_interval)

#List that will contain rect obstacle objects
r_list=[]
#List that will contain coloured obstacle objects which give you trail blocks
co_list=[]
#List that will contain trail block objects
t_list=[]
#Variable determining how many trailblocks plyr currently has
t_len= 4
#Whether or not an enemy battle is going on
enemy_spawned = False
#List that will contain enemies
e_list = []
#List of player projectiles
pp_list = []
#List of enemy projectiles
ep_list=[]


#Whether or not the player died
died = False

#mainloop  
run = True
while run:
  pygame.time.delay(23)
  #Event loop
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      run = False
    #Runs every custom interval, spawns rect or coloured objects
    #If it is time for an enemy battle, objects will stop spawning
    elif event.type == CUSTOM_INTERVAL_EVENT and enemy_spawned == False:
      score+=1
      #Chance of coloured object spawning instead of rect obstacle
      #Coloured objects give you a trail block
      i = random.randint(0,10)
      if i == 4:
        r_x = random.randint(0,680)
        co_list.append(Object(r_x, -120,1))
      else:
        r_x = random.randint(0,680)
        r_list.append(Object(r_x, -120,0))
    #If the player presses space, change direction and play the sound fx
    #If the player presses L_Shift shoot one of their trailblocks if they have any left
    elif event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_SPACE:
        pygame.mixer.Sound.play(dir_sound)
        plyr.movementSwitch()
      elif event.key == pygame.K_LSHIFT and t_len>0:
        pp_list.append(Projectile(plyr.getX(),plyr.getY(),0))
        del t_list[-1]
        t_len -= 1

  #Check if player has collided with rect obstacles
  obst_collision = plyr.obstCollisions(r_list)
  if obst_collision!= False: 
    #If plyr has no trail blocks the game is over
    if t_list==[]:
      pygame.mixer.music.stop()
      plyr.setColour((252, 73, 73))
      plyr.update(window)
      died = True
      run = False
    #If the plyr has trail blocks then 1 is taken away
    else:
      pygame.mixer.Sound.play(lose_trail_sound)
      r_list.remove(obst_collision)
      del t_list[-1]
      t_len -= 1

  #Check if player has collided with a coloured object
  #If they have they gain 1 trail block
  co_collision = plyr.cObstCollisions(co_list)
  if co_collision!= False:
    pygame.mixer.Sound.play(trail_sound)
    co_list.remove(co_collision)
    t_len += 1

  #Constantly removes and adds in new trailblocks every loop
  #The trail blocks move down at a set speed and then get replaced
  #The constant replacing/updating of trailblocks creates good "tail" fx
  #Also ensures that the replacing and updating amount of trail blocks is correct
  t_list.append(TrailBlock(plyr.getX()+30,plyr.getY()+50))
  if len(t_list) > t_len:
    del t_list[0]

  #Sets the window background to the bg image
  #Object updating/drawing must come after this to appear on the display
  window.blit(bg, (0, 0))

  #Iterate over each rect obstacle and update them if they are visible still
  for r in r_list:
    if r.isVisible():
      r.update(window)

  #Iterate over each coloured object and update them if they are visible still
  for co in co_list:
    if co.isVisible():
      co.update(window)

  #Iterate over each trail block and update them
  for t in t_list:
    t.update(window)

  #Iterate over enemies and update them
  for e in e_list:
    e.update(window)
  
  #Iterate over player's projectiles and update them
  for p in pp_list:
    p.update(window)

  #Set the score surface with the plyr's current score, then set the text to appear on screen
  score_surface = text_font.render("Score: {}".format(score), False, (0,0,0))
  window.blit(score_surface,(10,10))

  #Check if score has reached interval, if so spawn enemy
  if score % 100 == 0:
    score +=1
    enemy_spawned = True
    e_list.append(Enemy(400, - 75))

  #Update the player 
  plyr.update(window)
  #Update the pygame display
  pygame.display.update()

#If the player died then play the death sound, if not just quit
if died:
  pygame.mixer.Sound.play(die_sound)
while pygame.mixer.get_busy():
  pass
else:
  pygame.quit()

