import pygame, random, sys
sys.dont_write_bytecode = True

pygame.init()

window = pygame.display.set_mode((800,750), pygame.SCALED)
pygame.display.set_caption("Block Battle")
bg = pygame.image.load("assets/bg.png").convert()

text_font = pygame.font.SysFont("Arial", 40)

from Objects import Object
from Objects import TrailBlock
from Objects import Projectile
from Enemy import Enemy
from Player import Player
plyr = Player(400,500)
enemy = Enemy(400,-75)
      
CUSTOM_INTERVAL_EVENT = pygame.event.custom_type()
custom_interval = 500
pygame.time.set_timer(CUSTOM_INTERVAL_EVENT, custom_interval)

r_list=[]
co_list=[]
t_list=[]
t_len= 5
pp_list = []
ep_list=[]

enemy_active = False
enemy_lives = 3
score = 1
run = True

while run:
  pygame.time.delay(23)
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      run = False
    if event.type == CUSTOM_INTERVAL_EVENT:
      i = random.randint(0,10)
      if i == 5:
        r_x = random.randint(0,680)
        co_list.append(Object(r_x, -120,1))
      else:
        if enemy_active == False:
          score+=1
          r_x = random.randint(0,680)
          r_list.append(Object(r_x, -120,0))
    if event.type == CUSTOM_INTERVAL_EVENT and enemy_active:
      i = random.randint(0,2)
      if i == 2:
        ep_list.append(Projectile(enemy.getX(),0,1))
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        plyr.movementSwitch()
      if event.key == pygame.K_LSHIFT and t_len>0 and enemy_active:
        pp_list.append(Projectile(plyr.getX(),plyr.getY(),0))
        del t_list[-1]
        t_len -= 1

  obst_collision = plyr.obstCollisions(r_list)
  if obst_collision!= False: 
    if t_list==[]:
      plyr.setColour((252, 73, 73))
      plyr.update(window)
      run = False
    else:
      r_list.remove(obst_collision)
      del t_list[-1]
      t_len -= 1
 
  ep_collision = plyr.obstCollisions(ep_list)
  if ep_collision!= False: 
    if t_list==[]:
      plyr.setColour((252, 73, 73))
      plyr.update(window)
      run = False
    else:
      ep_list.remove(ep_collision)
      del t_list[-1]
      t_len -= 1
  
  pp_collision = enemy.obstCollisions(pp_list)
  if pp_collision!= False:
    if enemy_lives == 1:
      enemy_active = False
    else:
      enemy_lives -= 1
      pp_list.remove(pp_collision) 


  co_collision = plyr.obstCollisions(co_list)
  if co_collision!= False:
    co_list.remove(co_collision)
    t_len += 1

  t_list.append(TrailBlock(plyr.getX()+30,plyr.getY()+50))
  if len(t_list) > t_len:
    del t_list[0]

  window.blit(bg, (0, 0))

  for r in r_list:
    if r.isVisible():
      r.update(window)

  for co in co_list:
    if co.isVisible():
      co.update(window)

  for t in t_list:
    t.update(window)

  for ep in ep_list:
    ep.update(window)
  
  for p in pp_list:
    p.update(window)

  score_surface = text_font.render("Score: {}".format(score), False, (0,0,0))
  window.blit(score_surface,(10,10))

  if score % 100 == 0:
    score +=1
    enemy_active = True
    enemy_lives = 3

  plyr.update(window)

  if enemy_active:
    enemy.update(window)

  pygame.display.update()




pygame.quit()
