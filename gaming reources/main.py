# KEYS CAN BE PRESSED ON KEYBOARD:
# KEY_SPACE,W,S,D,UP,LEFT,RIGHT,DOWN.
#PRESS SPACE TO RESTART
# CITE IMAGES FORM https://www.aigei.com/

from os import remove
import pygame 
from sys import exit 
import random  
from pygame.locals import *
#making enemies spawning 
class Enemies : 

       def __init__(self):
             
             self.enemy_list = [] # storing all the rec 
             self.spawn = pygame.USEREVENT  #spawning 
             self.e1 = pygame.image.load("C:\gaming reources\enemyeffect.GIF").convert()
             self.e1 = pygame.transform.scale(self.e1,(70,60)).convert()
              
            #  
             self.e2 = pygame.image.load("C:\gaming reources\enemyeffect.GIF").convert()
             self.e2 = pygame.transform.scale(self.e1,(80,60)).convert()
             self.e3 = pygame.image.load("C:\gaming reources\ether.png").convert_alpha()
             self.e3 = pygame.transform.scale(self.e3,(400,250)).convert_alpha()
             
             self.e6 = pygame.image.load("C:\gaming reources\enemy2.gif").convert()

             self.e7 = pygame.image.load("C:\gaming reources\enemy1.gif").convert()
             
       def position(self):# return a tuple to help spawn at various positions
             positions = [(1600,50),(1600,100),(1600,150),(1600,80) ,(1600,260) ,(1600,380),(1600,400),(1600,440),(1600,600),(1600,300) ]
             position = random.choice(positions)
             return position
        
             
              
       
       def move(self):  # move 
            self.e1_rect.x -= 20
       def creat_enenmy(self): # create rec for images and return them
          
           new_enemy   = self.e1.get_rect(center = self.position( ))
           more   = self.e2.get_rect(center = self.position( ) )
           return  new_enemy , more

       def move_enemy(self,enemies): # move every rec passed in 
           for enemy in enemies :
               enemy.centerx -= 15
           return enemies    
       def draw_enemy(self,enemies):    # draw rec passed in
     
            for enemy in enemies:
               main.my_screen.blit(self.e1,enemy)   # blit function (image,position)
               main.my_screen.blit(self.e2,enemy) 
class Player :
       
      def __init__(self):
            self.player_list = []# storing all the rec 
            self.ally_vel = 8 #velocity of ally
            self.PLAYER_y = 300 # initial position of player
            self.PLAYER_X = 88
            self.MOTOR_PLAYER = pygame.image.load("C:\gaming reources\player.png")
            self.MOTOR_PLAYER = pygame.transform.scale(self.MOTOR_PLAYER,(150,80)).convert_alpha()
            self.MOTOR_PLAYER_rect = self.MOTOR_PLAYER.get_rect(center = ( self.PLAYER_X,self.PLAYER_y))
            self.e4 = pygame.image.load("C:\gaming reources\qally1.gif").convert()
             
          
            self.e5 = pygame.image.load("C:\gaming reources\qally2.gif").convert()
             
      def key_controls(self):   
            run = True # Booleens
            if  self.MOTOR_PLAYER_rect.y <= 220 or player.MOTOR_PLAYER_rect.y >= 600 :     
                
                    self.MOTOR_PLAYER_rect.x , self.MOTOR_PLAYER_rect.y = center =   self.PLAYER_X,self.PLAYER_y 
                    main.game_active = False
                    enemy.enemy_list.clear()

            if run == True: # if True player can move 
                keys_pressed = pygame.key.get_pressed()
                if run == True:
                   if keys_pressed[pygame.K_UP] and self.MOTOR_PLAYER_rect.y >= 280:
                     self.MOTOR_PLAYER_rect.y -= main.VOLECITY_CAR                                           
                   if keys_pressed[pygame.K_DOWN ] and self.MOTOR_PLAYER_rect.y <= 540:
                      self.MOTOR_PLAYER_rect.y += main.VOLECITY_CAR 
                if keys_pressed[pygame.K_LEFT] and self.MOTOR_PLAYER_rect.x >= -20:
                      self.MOTOR_PLAYER_rect.x -= main.VOLECITY_CAR                                            
                if keys_pressed[pygame.K_RIGHT] and self.MOTOR_PLAYER_rect.x <= 512:
                     self.MOTOR_PLAYER_rect.x += main.VOLECITY_CAR  
                
      def  creat_ally(self):# create rec for images and return them
           new_palyer  = self.e4.get_rect(center = ( -100 , self.MOTOR_PLAYER_rect.y) )
           more   = self.e5.get_rect(center = ( -100  , self.MOTOR_PLAYER_rect .y ) )
           return  new_palyer , more
      def move_ally(self,allies):# move every rec passed in 
           for ally in allies :
               ally.centerx += self.ally_vel
           return allies   
                           
      def draw_ally(self,allies):# draw rec passed in
     
            for ally in allies:
               main.my_screen.blit(self.e4,ally)  
               main.my_screen.blit(self.e5,ally)        

       

class Mainclass:
        game_countdown = 3000 # put game_countdown -= 1 in while to define winning
        ally_shot_count = 5 # counts of help from ally palyer can get
        game_active = True # premises to deactivate the game
        
        teleport = 150 
        VOLECITY_CAR = 3
        FPS = 60 # frame per second
        size = width,heigh = (1024,640) # screen size
        my_screen = pygame.display.set_mode(( size))
        clock = pygame.time.Clock()  # frame speed
        surface_bg = pygame.image.load("C:\gaming reources\qroad.png") # load image
          
        The_sky = pygame.image.load("C:\gaming reources\sky.PNG").convert()# convert function make the images loaded better
        indicator = pygame.image.load("C:\gaming reources\item1.png")
        indicator = pygame.transform.scale(indicator,(30,1024))# change size
        indicator = pygame.transform.rotate(indicator,90) # rotate the image
        victory = pygame.image.load("C:\gaming reources\okvictory.png")
        
        def __init__(self):

          pass
        def check_collision(self,enemies): # checking collisons between rec, passing in the list of all enemies to check with Player rec
          for enemy in enemies: 
              if player.MOTOR_PLAYER_rect.colliderect(enemy):# if hit deactivate the game
                   self.game_active = False
               
        def check_collision_ally_to_enemy(self,allies,list_enemy): #checking collisons between rec, passing in the list of all enemies and allies and use for loops to check with each other
          for enemies in list_enemy:
            for ally in allies: 
              for enemies in list_enemy:
               if enemies.colliderect(ally):# if hit enemies disappear
                 enemy.enemy_list.remove( enemies )
                   
                    
                 


        def mainfunction (self) :
              pygame.init() # initiate the game
              pygame.time.set_timer(enemy.spawn,1200) # event pops according to time
              pygame.mixer.pre_init(44100,16,2,4096)  # bgm init
              pygame.display.set_caption("Torrnet racer") # title
              pygame.mixer.music.load("C:\gaming reources\Daniel Deluxe - Air.mp3")# load  the mp3
              pygame.mixer.music.set_volume(0.5) # 0 to 1
              pygame.mixer.music.play(2)# times of playing the bgm. -1 is repetitive 
               
              while True:
                pygame.display.update() # keep updating images
                 
                for event in pygame.event.get(): # loop events 
                  if event.type == pygame.QUIT: 
                   pygame.quit()
                   exit()    # quitting the game 
                  if event.type == enemy.spawn:
                      enemy.enemy_list.extend(enemy.creat_enenmy()) # line 144 activates enemies sapwning
                  if event.type == pygame.KEYDOWN: # only press once at a time
                   if  event.key == pygame.K_d and self.ally_shot_count > 1:

                     player.player_list.extend(player.creat_ally()) # pressing key_d to spawn a ally
                     self.ally_shot_count -= 1 # reduce 


                    
                    
                  
                   if  event.key == pygame.K_w and  player.MOTOR_PLAYER_rect.x <= 700: 
                           
                            
                           player.MOTOR_PLAYER_rect.y -= 0
                           player.MOTOR_PLAYER_rect.y -= main.teleport 
                           player.MOTOR_PLAYER_rect.x += main.teleport
                   if  event.key == pygame.K_s and player.MOTOR_PLAYER_rect.x <= 700 :
                           
                            
                           player.MOTOR_PLAYER_rect.y -= 0
                           player.MOTOR_PLAYER_rect.y += main.teleport       
                           player.MOTOR_PLAYER_rect.x += main.teleport   # press certain keys to teleport 
                   if  event.key == pygame.K_SPACE and self.game_active == False:
                      self.game_active = True
                      player.MOTOR_PLAYER_rect.x ,player.MOTOR_PLAYER_rect.y = center =   player.PLAYER_X,player.PLAYER_y  
                      enemy.enemy_list.clear()
                      player.player_list.clear()
                      self.ally_shot_count = 5
                      self.game_countdown = 3000
                          # press Space to reactivate the game when it is being deactivated, and reset values
                      

                     


                               




                self.game_countdown -= 2 # win condition 
                if self.game_countdown <= 0:
                  self.game_active = False
                  main.my_screen.blit(main.victory,(350,50)) # drawing a falg to indicate winning

                  
                
                if self.game_active:  #When active 
                  p1.images_load(  ) 
                  
                   
                  
                  player.key_controls()       
                  main.clock.tick(main.FPS)
  
                  p1.position_moving( )               
                  enemy.enemy_list = enemy.move_enemy( enemy.enemy_list )
                  player.player_list = player.move_ally( player.player_list)   
                  enemy.draw_enemy(enemy.enemy_list)
                  player.draw_ally(player.player_list)
                  main.check_collision(enemy.enemy_list)
                  main.check_collision_ally_to_enemy(player.player_list,enemy.enemy_list)
                 
                 
                        
                                
                

class Draw_Image:
     
    move_x = 0
    sky_move_x = 0
    battom_move_x = 0
    def __init__(self):
        pass


       
    def images_load(self ): # BLIt function to draw
       
        main.my_screen.blit(main.The_sky,( self.sky_move_x ,0))
        main.my_screen.blit(main.The_sky,( self.sky_move_x+ 1024,0))
        main.my_screen.blit(main.surface_bg,(self.move_x   ,0))
        main.my_screen.blit(main.surface_bg,(self.move_x  + 1024,0))
        main.my_screen.blit(player.MOTOR_PLAYER,player.MOTOR_PLAYER_rect)
        main.my_screen.blit(main.indicator,(  self.battom_move_x ,610))
        main.my_screen.blit(main.indicator,(  self.battom_move_x  + 1024,610))
        main.my_screen.blit(enemy.e3,(700,10))
        
           
        main.my_screen.blit(enemy.e6,(700,0))
        main.my_screen.blit(enemy.e7,(800,30))

        
        #enemies:
      

    def position_moving(self): # in while loop to make images move

            if self.move_x  <= - 1024:
              self.move_x   = 0
            if self.sky_move_x <= -1024:
              self.sky_move_x = 0
            if self.battom_move_x <= -1024:
               self.battom_move_x = 0     
              
            p1.move_x  -= 10
            p1.sky_move_x -= 1   
            p1.battom_move_x -= 10 
         
            
player = Player()
enemy = Enemies()         
main = Mainclass()
p1 = Draw_Image()
 
main.mainfunction()       




