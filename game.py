import pygame, sys
import time
from sys import exit


class Player(pygame.sprite.Sprite):
        
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill((200,30,30))
        self.rect = self.image.get_rect(center = (400,400))
        self.current_health = 1000
        self.max_health = 1000
        self.target_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 5



        

        

    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health <= 0:
            self.target_health = 0
            print(self.target_health)






    def update(self):
        self.basic_health()

    def basic_health(self):
        pygame.draw.rect(screen,(255,0,0),(400,40,self.target_health / self.health_ratio,25))
        pygame.draw.rect(screen,(255,255,255),(400,40,self.health_bar_length,25),4) 


class player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.image.fill((200,30,30))
		self.rect = self.image.get_rect(center = (400,400))
		self.current_health = 1000
		self.target_health = 1000
		self.max_health = 1000
		self.health_bar_length = 400
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 5

	def get_damage2(self,amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health < 0:
			self.target_health = 0





	def update(self):
		self.basic_health()

	def basic_health(self):
		pygame.draw.rect(screen,(255,0,0),(10,10,self.target_health / self.health_ratio,25)) 
		pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4) 









def display_score() :
        current_time = pygame.time.get_ticks()
        score_s =test_font.render(f'{current_time}', False ,(64,64,64))
        score_r = score_s.get_rect(center = (400,50))
        screen.blit(score_s,score_r)

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("martia-games")
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(Player())
player2 = pygame.sprite.GroupSingle(player2())

#load music and sounds
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))



test_font = pygame.font.Font(None, 35)
test_surface = pygame.image.load('city.png').convert()
#text_surface = test_font.render("THE terminator run",None,"red")

enemy_terminator = pygame.image.load("enemy_terminator.png").convert_alpha()
enemy_terminator_rect = enemy_terminator.get_rect(midtop = (800,300))
enemy_terminator_x = 0
t_gravity = 0



terminator = pygame.image.load("terminator-800.png").convert_alpha()
t_rect = terminator.get_rect(midtop = (100,300))
tt_gravity = 0


projectile =  pygame.image.load("project.png").convert_alpha()
projectile_rect = projectile.get_rect(midtop = (660,200))

t_projectile =  pygame.image.load("t-projrct.png").convert_alpha()
t_projectile_rect = projectile.get_rect(midtop = (320,190))

jhony_projectile =  pygame.image.load("jhony.png").convert_alpha()
jhony_projectile_rect = projectile.get_rect(midtop = (150,200))


block = False
crouch = False
block2 = False
crouch2 = False
onthegraond = False
game_activ = False
game_activ2 = False
game_activ3 = False
crouch_cut = False
sonya_rage = False
fatality = False
end = False
fatality1 = False
d_punh =  False
nut_punch = False
nut_punch1 = False 
nut_punch2 = False
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()     




        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_q :
                terminator = pygame.image.load("putch.png").convert_alpha()
            else:
                terminator = pygame.image.load("terminator-800.png").convert_alpha()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_q :
                block = False
                crouch = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_q :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if enemy_terminator_rect.colliderect(t_rect) and block2 == False and crouch2 == False  and onthegraond == False and sonya_rage == False and not fatality and not nut_punch and not nut_punch1 and not nut_punch2 : 
                    player.sprite.get_damage(200)
                if enemy_terminator_rect.colliderect(t_rect) and block2 == True and not fatality   :
                    player.sprite.get_damage(2)
                if enemy_terminator_rect.colliderect(t_rect) and crouch2 == True   :
                    player.sprite.get_damage(0)
                if enemy_terminator_rect.colliderect(t_rect) and  fatality  :
                    player.sprite.get_damage(0)
                if enemy_terminator_rect.colliderect(t_rect) and  nut_punch  :
                    player.sprite.get_damage(0)
                if enemy_terminator_rect.colliderect(t_rect) and  nut_punch1  :
                    player.sprite.get_damage(0)
                if enemy_terminator_rect.colliderect(t_rect) and  nut_punch2  :
                    player.sprite.get_damage(0)
                if enemy_terminator_rect.colliderect(t_rect) and onthegraond == True and not fatality :
                    player.sprite.get_damage(150)
                if enemy_terminator_rect.colliderect(t_rect) and sonya_rage and game_activ2 and player.sprite.target_health <= 200 and not fatality  :
                    player.sprite.get_damage(100)





        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_z :
                terminator = pygame.image.load("kik.png").convert_alpha()
                d_punh =  True
            else:
                terminator = pygame.image.load("terminator-800.png").convert_alpha()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_z :
                block = False
                crouch = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_z :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if enemy_terminator_rect.colliderect(t_rect) and block2 == True  :
                    player.sprite.get_damage(2)
                    onthegraond = True
                if enemy_terminator_rect.colliderect(t_rect) and block2 == False and crouch2 == False : 
                    onthegraond = True
                    player.sprite.get_damage(200)
                if enemy_terminator_rect.colliderect(t_rect) and block2 == True and crouch == True :      
                    player.sprite.get_damage(2)
                if enemy_terminator_rect.colliderect(t_rect) and crouch2 == True :
                    player.sprite.get_damage(300)
                if enemy_terminator_rect.colliderect(t_rect) and sonya_rage and game_activ2 and player.sprite.target_health <= 200 :
                    player.sprite.get_damage(100)
                if enemy_terminator_rect.colliderect(t_rect) and  fatality  :
                    player.sprite.get_damage(0)

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r :
                block = False
                crouch = False
                
                while event.type == pygame.KEYDOWN and event.key == pygame.K_r :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if enemy_terminator_rect.colliderect(t_rect) and d_punh  :
                     player.sprite.get_damage(400)
                     terminator = pygame.image.load("d-punch.png").convert_alpha()
                     d_punh = False
                     enemy_terminator_rect.x += 100


        if player.sprite.target_health <= 200 and game_activ2 :
                    sonya_rage = True
                    print(sonya_rage)



        if player2.sprite.target_health <= 0 and not end  :
                    fatality = True
                    print(fatality)
                    if fatality :
                        terminator = pygame.image.load("terminator-800.png").convert_alpha()

        if player.sprite.target_health <= 0 and not end  :
                    fatality1 = True
                    print(fatality1)
                    

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_p  and  game_activ :
                        enemy_terminator = pygame.image.load("p2_puntch.png").convert_alpha()
            if event.key == pygame.K_p  and  game_activ2 :
                        enemy_terminator = pygame.image.load("sonya-p.png").convert_alpha()
            if event.key == pygame.K_p  and  game_activ3 :
                        enemy_terminator = pygame.image.load("jhony-p.png").convert_alpha()
            if event.key == pygame.K_p  and   game_activ2 and sonya_rage :    
                        enemy_terminator = pygame.image.load("sonya-rp.png").convert_alpha()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_p :
                block2 = False 
                crouch2 = False
                crouch_cut = False
                nut_punch = False 
                nut_punch1 = False 
                nut_punch2 = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_p  :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if enemy_terminator_rect.colliderect(t_rect) and block == False and crouch == False and onthegraond == False and not game_activ2  and not fatality1 and not game_activ3 and game_activ : 
                    player2.sprite.get_damage2(200)
                if enemy_terminator_rect.colliderect(t_rect) and block == False and crouch == False and onthegraond == False and not game_activ2  and not fatality1 and  game_activ3 and not game_activ : 
                    player2.sprite.get_damage2(200)
                if enemy_terminator_rect.colliderect(t_rect) and block == True :
                    player2.sprite.get_damage2(2)
                if game_activ :    
                    if enemy_terminator_rect.colliderect(t_rect) and crouch == True and onthegraond == True  and not fatality1 :
                        player2.sprite.get_damage2(0)
                if enemy_terminator_rect.colliderect(t_rect) and game_activ2 and not fatality1  :
                    player2.sprite.get_damage2(150)
                if enemy_terminator_rect.colliderect(t_rect) and sonya_rage and game_activ2 and player.sprite.target_health <= 200 and not  fatality1 :
                    player2.sprite.get_damage2(350)
                if fatality1  and enemy_terminator_rect.colliderect(t_rect) :
                     player2.sprite.get_damage2(0)





        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_y  and  game_activ2 :
                if crouch2 :
                    crouch2 = False
                    crouch_cut = True
                    enemy_terminator = pygame.image.load("sonya-appercut.png").convert_alpha()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_y  and  game_activ2 and crouch_cut :
                print(crouch_cut)
                while event.type == pygame.KEYDOWN and event.key == pygame.K_y  :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()

                if enemy_terminator_rect.colliderect(t_rect) and block == True :
                    player2.sprite.get_damage2(2)   
                elif enemy_terminator_rect.colliderect(t_rect) and block == False and crouch_cut:
                        player2.sprite.get_damage2(200)
                if game_activ2 and enemy_terminator_rect.colliderect(t_rect) and block == False and crouch_cut :
                        tt_gravity = -20 

        mouse = pygame.mouse.get_pos()

        if projectile_rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN :
            game_activ2 = True
        
        if t_projectile_rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN :
            game_activ = True

        if jhony_projectile_rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN :
            game_activ3 = True

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_k :
                block2 =  False 
                crouch2 = False 
                crouch_cut = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_k  :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if game_activ2 :
                    enemy_terminator = pygame.image.load("sonya-kik.png").convert_alpha()
                if game_activ3 :
                    enemy_terminator = pygame.image.load("jhony-kik.png").convert_alpha()
                if   game_activ2 and sonya_rage :    
                        enemy_terminator = pygame.image.load("sonya-rk.png").convert_alpha()
                if  nut_punch :
                    
                    enemy_terminator_rect.x += -100
                    enemy_terminator = pygame.image.load("jhony-kik+.png").convert_alpha()

                if enemy_terminator_rect.colliderect(t_rect) and block == True and not fatality1 :
                    player2.sprite.get_damage2(2)
                if enemy_terminator_rect.colliderect(t_rect) and block == False and crouch == False and not fatality1 : 
                    player2.sprite.get_damage2(0)
                if enemy_terminator_rect.colliderect(t_rect) and block == True and crouch == True and not fatality1 :
                   player2.sprite.get_damage2(2)
                if enemy_terminator_rect.colliderect(t_rect) and crouch == True and not fatality1 :
                    player2.sprite.get_damage2(200)
                if enemy_terminator_rect.colliderect(t_rect) and sonya_rage and game_activ2 and player.sprite.target_health <= 200 and not fatality1 :
                    player2.sprite.get_damage2(200)
                if fatality1  and enemy_terminator_rect.colliderect(t_rect) :
                     player2.sprite.get_damage2(0)
                if enemy_terminator_rect.colliderect(t_rect) and  game_activ3 and not block :
                    player2.sprite.get_damage2(200)
                if enemy_terminator_rect.colliderect(t_rect) and  game_activ3 and nut_punch and not block :
                    player2.sprite.get_damage2(200)
                if enemy_terminator_rect.colliderect(t_rect) and  game_activ3 and nut_punch and  block :
                    player2.sprite.get_damage2(0)

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_a :
                block = True
        if block :
            print(block)
            terminator = pygame.image.load("blockt1.png").convert_alpha()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_c :
                crouch = True
        if crouch :
            print(crouch)
            terminator = pygame.image.load("croucht1.png").convert_alpha()


        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_m :
                block2 = True
        if block2 and  game_activ :
            print(block2)
            enemy_terminator = pygame.image.load("blockt2.png").convert_alpha()
        if block2 and game_activ2 :
                enemy_terminator = pygame.image.load("sonya-block.png").convert_alpha()     
        if block2 and game_activ3 :
                enemy_terminator = pygame.image.load("jhony-block.png").convert_alpha()

                print(block2)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_n :
                crouch2 = True
        if crouch2 and  game_activ :
            print(crouch2)
            enemy_terminator = pygame.image.load("croucht2.png").convert_alpha()

        if crouch2 and  game_activ2 :
            print(crouch2)
            enemy_terminator = pygame.image.load("crouch-sonya.png").convert_alpha()

        if crouch2 and  game_activ3 :
            print(crouch2)
            enemy_terminator = pygame.image.load("jhony-ch.png").convert_alpha()

        if onthegraond and  game_activ :
            enemy_terminator = pygame.image.load("ontheground2.png").convert_alpha()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                 nut_punch = True

        if event.type == pygame.KEYDOWN and game_activ3 :
            if event.key == pygame.K_LEFT and game_activ3 and nut_punch :
                 nut_punch = False 
                 nut_punch1 = True 
                 if nut_punch1 :    
                    enemy_terminator = pygame.image.load("nut-p1.png").convert_alpha() 
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_b and nut_punch1 and game_activ3 and not fatality1 :
                 nut_punch1 = False 
                 nut_punch2 = True 
                 enemy_terminator = pygame.image.load("nut-punch.png").convert_alpha()
                 if enemy_terminator_rect.colliderect(t_rect) and  game_activ3 and nut_punch2 :
                    player2.sprite.get_damage2(500)
                    nut_punch2 = False
                 if enemy_terminator_rect.colliderect(t_rect) and fatality1 :
                    player2.sprite.get_damage2(0)
                    nut_punch2 = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_e :
                block = False
                crouch = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_e  :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                terminator = pygame.image.load("t_a.png").convert_alpha()
                if  block2 == True and not fatality  :
                    player.sprite.get_damage(2)
                if  block2 == False and crouch2 == False and not fatality : 
                    player.sprite.get_damage(20)
                if  block2 == True and crouch2 == True and not fatality :
                    player.sprite.get_damage(1)
                if  crouch2 == True and not fatality :
                    player.sprite.get_damage(80)
                if   sonya_rage and game_activ2 and player.sprite.target_health <= 200 and not fatality :
                    player.sprite.get_damage(5)
                if  fatality :
                    player.sprite.get_damage(0)

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_o :
                block2 = False 
                crouch2 = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_o  :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                if  onthegraond == False and  game_activ :
                    enemy_terminator = pygame.image.load("ob.png").convert_alpha()

                if  block == True and not fatality1 :
                    player2.sprite.get_damage2(2)
                if  block == False and crouch == False and not fatality1 : 
                    player2.sprite.get_damage2(50)
                if  block == True and crouch == True and not fatality1 :
                    player2.sprite.get_damage2(2)
                if  crouch == True and not fatality1 :
                    player2.sprite.get_damage2(150)
                if  onthegraond == True and not fatality1 :
                    player2.sprite.get_damage2(0)
                if fatality1 :
                     player2.sprite.get_damage2(0)
                     
                     

            if event.key == pygame.K_o and fatality and game_activ2  :
                 terminator = pygame.image.load("sonya-fatality.png").convert_alpha()
                 print('fatality:  sonya blade')
                 fatality = False
                 end = True
                 enemy_terminator = pygame.image.load("shutgun.png").convert_alpha()

            if event.key == pygame.K_o  and game_activ3 and enemy_terminator_rect.colliderect(t_rect) and fatality :
                 enemy_terminator = pygame.image.load("jhony-kik+.png").convert_alpha()
                 fatality = False
                 end = True
                 print('fatality:  jhony cage')
                 terminator = pygame.image.load("sonya-fatality.png").convert_alpha()

            if event.key == pygame.K_o and fatality1 and game_activ2  :
                 enemy_terminator = pygame.image.load("ts1.png").convert_alpha()
                 print('fatality:  sonya blade')
                 fatality1 = False
                 fatality2 = True
                 terminator = pygame.image.load("sf2.png").convert_alpha()

            if event.key == pygame.K_x and fatality2 and game_activ2  :
                 enemy_terminator = pygame.image.load("ts2.png").convert_alpha()
                 print('fatality:  sonya blade')
                 fatality2 = False
                 fatality3 = True
                 terminator = pygame.image.load("t_a.png").convert_alpha()

            if event.key == pygame.K_h and fatality3 and game_activ2  :
                 enemy_terminator = pygame.image.load("ts3.png").convert_alpha()
                 print('fatality:  sonya blade')
                 fatality3 = False
                 terminator = pygame.image.load("t_a.png").convert_alpha()

            if event.key == pygame.K_9 and end  :
                 exit()
            
                 
                 


        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_w :

                while event.type == pygame.KEYDOWN and event.key == pygame.K_w :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()   
                    if  not fatality  : 
                            t_rect.x += 4
                    if  fatality  :
                         t_rect.x += 0
                    pygame.display.update()
                    clock.tick(60)



                        



        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                if game_activ2 :
                    block2 = False 
                    crouch2 = False
                    crouch_cut = False
                    nut_punch = False 
                    nut_punch1 = False 
                    nut_punch2 = False
                while event.type == pygame.KEYDOWN and event.key == pygame.K_UP :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()    
                        block2 = False
                    if game_activ and onthegraond :
                        enemy_terminator_rect.x -= 0
                    if  not fatality1  : 
                        enemy_terminator_rect.x -= 4
                    if  fatality1  :
                        enemy_terminator_rect.x -= 0
                                                               
                    if   game_activ2  :    
                        enemy_terminator = pygame.image.load("sonya.png").convert_alpha()
                    if   game_activ2 and sonya_rage  :    
                        enemy_terminator = pygame.image.load("sonya-rage.png").convert_alpha()
                    if    game_activ :
                        enemy_terminator = pygame.image.load("enemy_terminator.png").convert_alpha()
                    if    game_activ3 :
                        enemy_terminator = pygame.image.load("jhony-cage.png").convert_alpha()
                    pygame.display.update()
                    clock.tick(120)



        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_s :

                while event.type == pygame.KEYDOWN and event.key == pygame.K_s :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()    
                    if  not fatality  : 
                            t_rect.x -= 4
                    if  fatality  :
                         t_rect.x += 0
                    pygame.display.update()
                    clock.tick(60)        

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :

                while event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()
                    block2 = False
                    crouch_cut = False
                    nut_punch = False 
                    nut_punch1 = False 
                    nut_punch2 = False
                    if game_activ and onthegraond :
                        enemy_terminator_rect.x += 0
                    if  not fatality1  : 
                        enemy_terminator_rect.x += 4
                    if  fatality1  :
                        enemy_terminator_rect.x -= 0
                    if   game_activ2  :    
                        enemy_terminator = pygame.image.load("sonya.png").convert_alpha()
                    if   game_activ2 and sonya_rage  :    
                        enemy_terminator = pygame.image.load("sonya-rage.png").convert_alpha()
                    if    game_activ :
                        enemy_terminator = pygame.image.load("enemy_terminator.png").convert_alpha()     
                    if    game_activ3 :
                        enemy_terminator = pygame.image.load("jhony-cage.png").convert_alpha()                   

                    pygame.display.update()
                    clock.tick(120)



        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_e :
                while event.type == pygame.KEYDOWN and event.key == pygame.K_e :
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            exit()



            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and onthegraond and not game_activ2 :
                    onthegraond = False
                if event.key == pygame.K_SPACE and game_activ2 and enemy_terminator_rect.bottom >= 300 :
                    t_gravity = -20

        if event.type == pygame.KEYUP :
           print('key up')



                

        #if sonya_rage :
         #   test_surface = pygame.image.load('city-rage.png').convert()
             




    screen.blit(test_surface,(0,0))



    if not game_activ2  : 
        test_surface = pygame.image.load('mainscreen.png').convert()
        screen.blit(t_projectile,(t_projectile_rect))
        screen.blit(projectile,(projectile_rect))

    if not game_activ  : 
        test_surface = pygame.image.load('mainscreen.png').convert()
        screen.blit(t_projectile,(t_projectile_rect))
        screen.blit(projectile,(projectile_rect))

    if game_activ2 :   
            screen.blit(enemy_terminator,(enemy_terminator_rect))
            screen.blit(terminator,t_rect)
            test_surface = pygame.image.load('city.png').convert()
            projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            t_projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            player.update()
            player2.update()


    if game_activ :   
            screen.blit(enemy_terminator,(enemy_terminator_rect))
            screen.blit(terminator,t_rect)
            test_surface = pygame.image.load('city.png').convert()
            projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            t_projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            player.update()
            player2.update()

    if game_activ3 :   
            screen.blit(enemy_terminator,(enemy_terminator_rect))
            screen.blit(terminator,t_rect)
            test_surface = pygame.image.load('city.png').convert()
            projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            t_projectile =  pygame.image.load("t-projrct2.png").convert_alpha()
            player.update()
            player2.update()



    enemy_terminator_x = 500

    #player
    t_gravity += 1
    enemy_terminator_rect.y  += t_gravity

    if enemy_terminator_rect.bottom >= 450  :
      enemy_terminator_rect.bottom = 450
      




    tt_gravity += 1
    t_rect.y  += tt_gravity
    if   t_rect.bottom >= 450 :
      t_rect.bottom = 450

    
      






    
    
    pygame.display.update()
    clock.tick(60)



