import pygame
import random
h = 800
w = 1000

timer=0
ms = 0

pl = 0
bot = 0

posy =0
posx = 0
blue = (0,0,255)
white = (255,255,255)
green = (0,128,0)
black = (38,38,38)
xs = 0
ys = 0
xs2 = 2
ys2 = 2
f = 50
f2 = 20
hitbox = 40
pygame.init()
dis = pygame.display.set_mode([w,h])
pygame.display.set_caption("BotV001")
img = pygame.image.load("vr.png")
bgimg = pygame.image.load("bg.png")
font = pygame.font.SysFont("monospace", 20)
c = pygame.time.Clock() 
def vrs(x,y):
   dis.blit(img,(x,y))
def bg(x,y):
 for i in range(2):
   dis.blit(bgimg,(x,y))
   x+=500
 y = 300
 x = 10
 for i in range(2):
   dis.blit(bgimg,(x,y))
   x+=500
 x = 10
 y = 600
 for i in range(2):
   dis.blit(bgimg,(x,y))
   x+=500
x = 100
y = 100
x2 = 400
y2 = 450
fl = True

while fl == True:
##   print "mouseY = ",posy," mouseX = ",posx
   timer+=1
   text = font.render("Player "+str(pl)+"  Bot "+str(bot), True, (102,205,170))
   for ev in pygame.event.get():
     if ev.type == pygame.QUIT:
          fl = False
      # elif ev.type == pygame.MOUSEBUTTONUP:
     if  f > f2:
       
            
       #up
        if  y >=  y2-150 and y <= y2-50:
         if x <= x2+100 and x >= x2-100:
             xs2 = 0
             ys2 = -4
       #upleft      
        if  y >=  y2-150 and y <= y2-20:
         if x <= x2-50 and x >= x2-100:
             xs2 = -2
             ys2 = -2
       #upright      
        if  y >=  y2-150 and y <= y2-20:
         if x <= x2+100 and x >= x2+50:
             xs2 = 2
             ys2 = -2
       #left      
        if  y >=  y2-50 and y <= y2+50:
         if x <= x2 and x >= x2-150:
             xs2 = -4
             ys2 = 0
       #right      
        if  y >=  y2-50 and y <= y2+50:
         if x <= x2+150 and x >= x2:
             xs2 = 4
             ys2 = 0
       #down      
        if  y >=  y2+50 and y <= y2+150:
         if x <= x2+100 and x >= x2-100:
             xs2 = 0
             ys2 = 4
             
       #downleft
        if  y >=  y2+20 and y <= y2+150:
         if x <= x2-50 and x >= x2-100:
             xs2 = -2
             ys2 =  2
       #downright
        if  y >=  y2+20 and y <= y2+150:
         if x <= x2+100 and x >= x2+50:
             xs2 = 2
             ys2 = 2
       
       #isInEdge     
     if y2 <= 50:
           ys2 = 2
     elif y2 >= h-50:
           ys2 = -2
     elif x2 <=50:
        xs2 = 2
     elif x2 >=w+75:
        xs2 = -2

       #mouse controll    
     if posy >  y:
          ys = 3
          
     if posy < y:
          ys = -3
         
             
     if posx >  x:
          xs = 3
          
     if posx < x:
          xs = -3
          
     if posx == 0:
           xs = 0
     if posy == 0:
          ys = 0
          
     
   try:
     ms = ev.pos
      
     posx = int(str(ms)[1:len(str(ms))-6])
     posy = int(str(ms)[5:len(str(ms))-1])
     if posy < 100 and posy >0:
        posx = int(str(ms)[1:len(str(ms))-5])
        
   except ValueError:
      ms = ev.pos
      
      try: 
       posx = int(str(ms)[1:len(str(ms))-6])
       posy = int(str(ms)[5:len(str(ms))-1])
      except ValueError:
          posx = 10
          posy  = 10
   except AttributeError:
     posy = 0
     posx = 0

    
   #enemy hit box       
   if y < y2+hitbox and y > y2-hitbox:
      if x > x2-hitbox and x < x2+hitbox:
        ran = random.randint(10,800)
        ran2 = random.randint(10,1000)
        if f >= f2:
           bot+=1
           x = ran2
           y = ran
           f2 = 20
           f+=(f2/4)
           hitbox+=5
        else:
           pl+=1
           x2 = ran2
           y2 = ran
           f2+=(f/4)
           
   #virus hitbox
   if y2 > 350 and y2 < 450:
    if x2 > 450 and x2 < 550:
      if f >38: 
       f = f-(f/32)


   if y > 350 and y < 450:
    if x > 450 and x < 550:
      if f2 >38:  
       f2 = f2-(f2/32)
      
   if timer == 300:
      f2+=1
      timer = 0
   
     
   x2+= xs2
   y2+= ys2
   x += xs
   y += ys         
   dis.fill(black)
   bg(10,10)

   pygame.draw.circle(dis, green,(x,y), int(f2))  
   vrs(450,350)
   pygame.draw.circle(dis, (0,0,139),(x2,y2), int(f+10))
   pygame.draw.circle(dis, (128,138,135),(x2,y2), int(f))
   dis.blit(text,
   (10,10))
   pygame.display.update()
   c.tick(70)
     
pygame.quit()
quit()

