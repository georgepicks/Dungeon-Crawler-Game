import  pygame, random
from images import *
from menu import *

pygame.init() #initialises the pygame window

screen_x = 1000#screen width
screen_y = 750#screen height

win = pygame.display.set_mode((screen_x, screen_y)) #sets the dimensions of the pygame window
pygame.display.set_caption("Game Window") #sets the caption of this pygame window
fps = pygame.time.Clock()#variable used to set the Frames Per Second that the program will run at

class player(): #class that deals with all of the player animations and most of the logic, e.g. damage etc.
    def __init__(self,x,y,health):
        #every variable that is used with and by the player sprite
        self.x = x
        self.y = y
        self.vel = 7.5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.r_attack = False
        self.l_attack = False
        self.h_walk_count = 0
        self.v_walk_count = 0
        self.attack_count = 0
        self.health = health
        self.player_dmg = 5
        self.idle = True
        
    def draw_player(self, win):
        if self.attack_count +1 >=18:
            self.attack_count = 0
        if self.h_walk_count  +1>=15:
            self.h_walk_count = 0
        if self.v_walk_count +1 >=12:
            self.v_walk_count = 0
            
        if self.right:
            win.blit(r_walk[self.h_walk_count//6], (self.x, self.y))
            self.h_walk_count +=1
        if self.left:
            win.blit(l_walk[self.h_walk_count//6], (self.x, self.y))
            self.h_walk_count +=1
        if self.up:
            win.blit(u_walk[self.v_walk_count//6], (self.x, self.y))
            self.v_walk_count +=1
        if self.down:
            win.blit(d_walk[self.v_walk_count//6], (self.x, self.y))
            self.v_walk_count +=1
        if self.idle == True:
            win.blit(idle[0], (self.x, self.y))

        if self.r_attack:
            #Demon sprites 
            if player.x > demon_sprite.x - 40 and player.x < demon_sprite.x + 70 and player.y > demon_sprite.y - 40 and player.y < demon_sprite.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                demon_sprite.health -=self.player_dmg
                self.attack_count +=1
            if player.x > demon_sprite_2.x - 40 and player.x < demon_sprite_2.x + 70 and player.y > demon_sprite_2.y - 40 and player.y < demon_sprite_2.y + 70:
                win.blit(r_attack[self.attack_count // 9], (self.x, self.y))
                demon_sprite_2.health -= self.player_dmg
                self.attack_count += 1
            if player.x > demon_sprite_3.x - 40 and player.x < demon_sprite_3.x + 70 and player.y > demon_sprite_3.y - 40 and player.y < demon_sprite_3.y + 70:
                win.blit(r_attack[self.attack_count // 9], (self.x, self.y))
                demon_sprite_3.health -= self.player_dmg
                self.attack_count += 1
            #Boss Sprites
            if player.x > boss_sprite.x - 40 and player.x < boss_sprite.x + 70 and player.y > boss_sprite.y - 40 and player.y < boss_sprite.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                boss_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > boss_sprite_2.x - 40 and player.x < boss_sprite_2.x + 70 and player.y > boss_sprite_2.y - 40 and player.y < boss_sprite_2.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                boss_sprite_2.health -= self.player_dmg
                self.attack_count +=1
            #Rogue Sprites
            if player.x > rogue_sprite.x - 40 and player.x < rogue_sprite.x + 70 and player.y > rogue_sprite.y - 40 and player.y < rogue_sprite.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                rogue_sprite.health -= self.player_dmg
                self.attack_count +=1
            #Ghost Sprites
            if player.x > ghost_sprite.x - 40 and player.x < ghost_sprite.x + 70 and player.y > ghost_sprite.y - 40 and player.y < ghost_sprite.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > ghost_sprite2.x - 40 and player.x < ghost_sprite2.x + 70 and player.y > ghost_sprite2.y - 40 and player.y < ghost_sprite2.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite2.health -= self.player_dmg
                self.attack_count +=1
            if player.x > ghost_sprite3.x - 40 and player.x < ghost_sprite3.x + 70 and player.y > ghost_sprite3.y - 40 and player.y < ghost_sprite3.y + 70:
                win.blit(r_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite3.health -= self.player_dmg
                self.attack_count +=1
            
            else:
                win.blit(r_attack[self.attack_count // 9], (self.x, self.y))
                self.attack_count +=1

        if self.l_attack:
            #Demon Sprites
            if player.x > demon_sprite.x - 40 and player.x < demon_sprite.x + 70 and player.y > demon_sprite.y - 40 and player.y < demon_sprite.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                demon_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > demon_sprite_2.x - 40 and player.x < demon_sprite_2.x + 70 and player.y > demon_sprite_2.y - 40 and player.y < demon_sprite_2.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                demon_sprite_2.health -= self.player_dmg
                self.attack_count +=1
            if player.x > demon_sprite_3.x - 40 and player.x < demon_sprite_3.x + 70 and player.y > demon_sprite_3.y - 40 and player.y < demon_sprite_3.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                demon_sprite_3.health -= self.player_dmg
                self.attack_count +=1
            #Boss Sprites
            if player.x > boss_sprite.x - 40 and player.x < boss_sprite.x + 70 and player.y > boss_sprite.y - 40 and player.y < boss_sprite.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                boss_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > boss_sprite_2.x - 40 and player.x < boss_sprite_2.x + 70 and player.y > boss_sprite_2.y - 40 and player.y < boss_sprite_2.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                boss_sprite_2.health -= self.player_dmg
                self.attack_count +=1
            #Rogue Sprites
            if player.x > rogue_sprite.x - 40 and player.x < rogue_sprite.x + 70 and player.y > rogue_sprite.y - 40 and player.y < rogue_sprite.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                rogue_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > rogue_sprite2.x - 40 and player.x < rogue_sprite2.x + 70 and player.y > rogue_sprite2.y - 40 and player.y < rogue_sprite2.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                rogue_sprite2.health -= self.player_dmg
                self.attack_count +=1
            if player.x > rogue_sprite3.x - 40 and player.x < rogue_sprite3.x + 70 and player.y > rogue_sprite3.y - 40 and player.y < rogue_sprite3.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                rogue_sprite3.health -= self.player_dmg
                self.attack_count +=1
            #Ghost Sprites
            if player.x > ghost_sprite.x - 40 and player.x < ghost_sprite.x + 70 and player.y > ghost_sprite.y - 40 and player.y < ghost_sprite.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite.health -= self.player_dmg
                self.attack_count +=1
            if player.x > ghost_sprite2.x - 40 and player.x < ghost_sprite2.x + 70 and player.y > ghost_sprite2.y - 40 and player.y < ghost_sprite2.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite2.health -= self.player_dmg
                self.attack_count +=1
            if player.x > ghost_sprite3.x - 40 and player.x < ghost_sprite3.x + 70 and player.y > ghost_sprite3.y - 40 and player.y < ghost_sprite3.y + 70:
                win.blit(l_attack[self.attack_count//9], (self.x, self.y))
                ghost_sprite3.health -= self.player_dmg
                self.attack_count +=1
            else:
                win.blit(l_attack[self.attack_count // 9], (self.x, self.y))
                self.attack_count += 1

        dmg = random.randint(1,500)
        #if player.health >100:
            #player.health = 100
        if dmg >=400:
            #Demon Sprites
            if demon_sprite.health >0:
                if player.x>demon_sprite.x-20 and player.x<demon_sprite.x+70 and player.y >demon_sprite.y-20 and player.y <demon_sprite.y+70 :
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            if demon_sprite_2.health >0:
                if player.x>demon_sprite_2.x-20 and player.x<demon_sprite_2.x+70 and player.y>demon_sprite_2.y-20 and player.y<demon_sprite_2.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            if demon_sprite_3.health >0:
                if player.x>demon_sprite_3.x-20 and player.x<demon_sprite_3.x+70 and player.y>demon_sprite_3.y-20 and player.y<demon_sprite_3.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            #Boss Sprites
            if boss_sprite.health >0:
                if player.x>boss_sprite.x-20 and player.x<boss_sprite.x+70 and player.y>boss_sprite.y-20 and player.y<boss_sprite.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health
            if boss_sprite_2.health >0:
                if player.x>boss_sprite_2.x-20 and player.x<boss_sprite_2.x+70 and player.y>boss_sprite_2.y-20 and player.y<boss_sprite_2.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            #Ghost Sprites
            if ghost_sprite.health >0:
                if player.x>ghost_sprite.x-20 and player.x<ghost_sprite.x+70 and player.y>ghost_sprite.y-20 and player.y<ghost_sprite.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            if ghost_sprite2.health >0:
                if player.x>ghost_sprite2.x-20 and player.x<ghost_sprite2.x+70 and player.y>ghost_sprite2.y-20 and player.y<ghost_sprite2.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health

            if ghost_sprite3.health >0:
                if player.x>ghost_sprite3.x-20 and player.x<ghost_sprite3.x+70 and player.y>ghost_sprite3.y-20 and player.y<ghost_sprite3.y+70:
                    player.health -=3
                    print(player.health)
                else:
                    player.health = player.health
            
        else:
            player.health = player.health
        
        #Rogue Sprites
        if dmg>=300:
            if rogue_sprite.health >0:
                if player.x>rogue_sprite.x-20 and player.x<rogue_sprite.x+70 and player.y>rogue_sprite.y-20 and player.y<rogue_sprite.y+70:
                    player.health -=1
                else:
                    player.health = player.health
            if rogue_sprite2.health >0:
                if player.x>rogue_sprite2.x-20 and player.x<rogue_sprite2.x+70 and player.y>rogue_sprite2.y-20 and player.y<rogue_sprite2.y+70:
                    player.health -=1
                else:
                    player.health = player.health
            if rogue_sprite3.health >0:
                if player.x>rogue_sprite3.x-20 and player.x<rogue_sprite3.x+70 and player.y>rogue_sprite3.y-20 and player.y<rogue_sprite3.y+70:
                    player.health -=1
                else:
                    player.health = player.health


class enemy():
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.idle_count = 0
        self.ghost_count = 0
        self.dead_count = 0
        self.health = health
    def draw_demon(self, win):
        if self.health<0:
            self.health = 0
        if self.idle_count +1 >= 24:
            self.idle_count = 0
        if self.dead_count >=10:
            self.dead_count = 10
        if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(demon_attack[self.idle_count // 9], (self.x, self.y))
            self.idle_count += 1
        elif self.health<=0:
            win.blit(demon_dead[self.dead_count // 3], (self.x, self.y))
            self.dead_count += 1
        else:
            win.blit(demon_idle[self.idle_count // 6], (self.x, self.y))
            self.idle_count += 1

    def draw_boss(self,win):
        if self.idle_count +1 >=18:
            self.idle_count = 0
        if self.dead_count +1 >=18:
            self.dead_count = 18
        if self.health<=0:
            win.blit(slime_dead[self.dead_count // 6], (self.x, self.y))
            self.dead_count += 1
        else:
            win.blit(slime_idle[self.idle_count//6], (self.x,self.y))
            self.idle_count +=1

    def draw_rogue(self,win):
        if self.idle_count +1 >= 18:
            self.idle_count = 0
        if self.dead_count +1 >=12:
            self.dead_count = 12
        if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(rogue_attack[self.idle_count // 3], (self.x, self.y))
            self.idle_count += 1
        elif self.health <=0:
            win.blit(rogue_dead[self.dead_count//3], (self.x,self.y))
            self.dead_count +=1
        else:
            win.blit(rogue_idle[self.idle_count//6], (self.x,self.y))
            self.idle_count +=1

    def draw_ghost(self,win):
        if self.idle_count +1 >=18:
            self.idle_count = 0
        if self.ghost_count +1>=15:
            self.ghost_count = 0
        if self.dead_count +1 >=12:
            self.dead_count = 12

        if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(ghost_attack[self.ghost_count // 3], (self.x, self.y))
            self.ghost_count += 1
        elif self.health <=0:
            win.blit(ghost_dead[self.dead_count//3], (self.x,self.y))
            self.dead_count+=1
        else:
            win.blit(ghost_idle[self.idle_count//6], (self.x, self.y))
            self.idle_count +=1
    
class health():
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def player_health(self,win):
        if player.health >=80:
            win.blit(p_health[4], (self.x,self.y))
        elif player.health >=60:
            win.blit(p_health[3], (self.x,self.y))
        elif player.health >=40:
            win.blit(p_health[2], (self.x,self.y))
        elif player.health>=20:
            win.blit(p_health[1], (self.x,self.y))
        elif player.health >=0:
            win.blit(p_health[0], (self.x,self.y))

class environment():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.door_count = 0
        self.chest_count = 0
        self.coin_count = 0
        self.picked_up = False

    def coin_draw(self,win):
        if self.coin_count +1 >=18:
            self.coin_count = 0
        if demon_sprite_2.health <=0: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
            if player.x > coin.x-65 and player.x <coin.x+20 and player.y > coin.y-55 and player.y <coin.y+40 : 
                self.picked_up = True
                pass
        if self.picked_up == True:
            win.blit(coin_anim[0], (150,10))
        else:
            if demon_sprite_2.health <=0: #and demon_sprite_2.health <=0 and demon_sprite_3.health<=0:
                win.blit(coin_anim[self.coin_count//6], (self.x+40,self.y+40))
                self.coin_count +=1
            else:
                pass

    def chest_draw(self,win):
        if coin.picked_up == True:
            if player.x > chest.x-65 and player.x <chest.x+20 and player.y > chest.y-55 and player.y <chest.y+20 :
                win.blit(chest_open[1], (self.x,self.y))
                if player.health <100:
                    player.health +=1
                    print(player.health)
                else:
                    player.health+=0
            else:
                win.blit(chest_open[0], (self.x,self.y))
        else:
            win.blit(chest_open[0], (self.x,self.y))
    def door_draw(self,win):
        if self.door_count +1 >= 18:
            self.door_count = 0
        if coin.picked_up ==True:
            win.blit(door_open, (door.x, door.y))
        else:
            win.blit(doors[self.door_count // 6], (door.x, door.y))
            self.door_count += 1
    def draw_level(self,win):
        win.blit(level_layout, (self.x, self.y))

def update_window(): #function that draws all sprites, then updates the pygame window
    if level_num ==1:
        win.fill((28, 17, 23))#fills the pygame window
        level_layout1.draw_level(win)
        coin.coin_draw(win)
        door.door_draw(win)
        chest.chest_draw(win)

        boss_sprite.draw_boss(win)
        boss_sprite_2.draw_boss(win)

        rogue_sprite.draw_rogue(win)
        rogue_sprite2.draw_rogue(win)
        rogue_sprite3.draw_rogue(win)
                
        demon_sprite.draw_demon(win)
        demon_sprite_2.draw_demon(win)
        demon_sprite_3.draw_demon(win)
                
        ghost_sprite.draw_ghost(win)
        ghost_sprite2.draw_ghost(win)
        ghost_sprite3.draw_ghost(win)

        health_bar.player_health(win)
        player.draw_player(win)
    elif level_num ==2:
        win.fill((28, 17, 23))
    pygame.display.update()#updates the pyame window

level_num = 1
chest_location = random.randint(1,4)

#level 1 values for all sprites, e.g. x, y, health etc.
demon_health = 200
ghost_health = 250
rogue_health = 150
boss_health = 400

player = player(450,300, 100)#player(510, 110, 1000000)#Done
health_bar = health(-15,-65)#Done

demon_sprite = enemy(random.randint(45,172), random.randint(102,210), demon_health)#Done
demon_sprite_2 = enemy(random.randint(172,500), random.randint(195,412), demon_health)#Done
demon_sprite_3 = enemy(random.randint(500,700), random.randint(412,550), demon_health)#Done

rogue_sprite = enemy(random.randint(45,172), random.randint(210,412), rogue_health)#Done
rogue_sprite2 = enemy(random.randint(500,700), random.randint(102,195), rogue_health)#Done
rogue_sprite3 = enemy(random.randint(172, 500), random.randint(412,550), rogue_health)#Done

ghost_sprite = enemy(random.randint(45,172), random.randint(412,550), ghost_health)#Done
ghost_sprite2 = enemy(random.randint(172,400), random.randint(102,195), ghost_health)#Done
ghost_sprite3 = enemy(random.randint(500,700), random.randint(195,412), ghost_health)#Done

boss_sprite = enemy(655, 130, boss_health)#Done
boss_sprite_2 = enemy(775, 230, boss_health)#Done


coin = environment(demon_sprite_2.x, demon_sprite_2.y+50)#Done
door = environment(810, 150)#Done
level_layout1 = environment(50,50)

if chest_location == 1:
    chest = environment(85,120)
elif chest_location ==2:
    chest = environment(85,610)
elif chest_location ==3:
    chest = environment(900, 120)
elif chest_location ==4:
    chest = environment(900, 610)

#Main Game Loop
run = True
while run:
    keys = pygame.key.get_pressed() #collects all of the keys pressed by the player
    mx, my = pygame.mouse.get_pos()#gets the coordinates of the mouse cursor
    fps.tick(30) #allows me to tweak the Frames Per Second; by increasing it, the animations will look smoother, but will require more processing power
    for event in pygame.event.get(): #if the pygame window is exited - the loop breaks and the Quit() function is run
        if event.type == pygame.QUIT:
            run = False
    if player.health <=0:
        pass
        #run = False
    if keys[pygame.K_ESCAPE]:
        quit()
#keybind setup for character movement, character attack and temporary keybinds for testing purposes
    if keys[pygame.K_r]:
        demon_sprite.health = -1
        boss_sprite.health =-1
    if keys[pygame.K_d] and keys[pygame.K_w]:
        player.x +=player.vel
        player.y -= player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_a] and keys[pygame.K_w]:
        player.x -=player.vel
        player.y -= player.vel
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        player.x -=player.vel
        player.y += player.vel
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_d] and keys[pygame.K_s]:
        player.x +=player.vel
        player.y += player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_a] and player.x >45:
        player.x -= player.vel
        player.r_attack = False
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_d] and player.x < 882:
        player.x += player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_w] and player.y>82:
        player.y -= player.vel
        player.up = True
        player.right = False
        player.left = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_s] and player.y <570:
        player.y += player.vel
        player.down = True
        player.right = False
        player.left = False
        player.up = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_q]:
        player.l_attack = True
        player.down = False
        player.right = False 
        player.left = False
        player.up = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_e]:
        player.r_attack = True
        player.down = False
        player.right = False
        player.left = False
        player.up = False
        player.l_attack = False
        player.idle = False
    else:
        player.h_walk_count = 0
        player.v_walk_count = 0
        player.idle_count = 0
        player.attack_count = 0

    if level_num ==18:
        if player.x > 570-5 and player.x <570+5 and player.y >102.5-10 and player.y<102+10:
            player.x = 382
            player.y = 270
        elif player.x > 382-5 and player.x <382+5 and player.y >260-10 and player.y<260+10:
            player.x = 550
            player.y = 102
        elif player.x > 70-5 and player.x <70+5 and player.y >395-10 and player.y<395+10:
            player.x = 80
            player.y = 575
        elif player.x > 67-5 and player.x <67+5 and player.y >575-10 and player.y<575+10:
            player.x = 70+20
            player.y = 395
    if player.x > door.x-20 and player.x <door.x+50 and player.y > door.y-20 and player.y <door.y+50 and coin.picked_up == True:
        level_num = 2
    if level_num ==2:
        pass
    print(("x = ", player.x), ("y = ", player.y))
    update_window()