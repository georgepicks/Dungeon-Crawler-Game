#libraries that are required for the program to funciton correctly
import  pygame, random, time
#images and menu are seperate aspects of the solution that are imported into the main game code
from images import *
from menu import *

pygame.init() #initialises the pygame window

screen_x = 1000#screen width
screen_y = 750#screen height 

#different sized fonts for different aspects of the game
font_small = pygame.font.Font("Retro.ttf", 100)
font_big = pygame.font.Font("Retro.ttf", 150)
font_ehealth = pygame.font.Font("Retro.ttf", 25)
font_help = pygame.font.Font("Retro.ttf", 60)

#starts the timer that records how fast the player completed the game
start_time = time.time()

#these varibles hold the RGB colour values for black and red that are used when diplaying text on the pygame window
black = (0,0,0)
red = (255, 0, 0)

win = pygame.display.set_mode((screen_x, screen_y)) #sets the dimensions of the pygame window
pygame.display.set_caption("Game Window") #sets the caption of this pygame window
fps = pygame.time.Clock()#variable used to set the Frames Per Second that the program will run at

class player(): #class that deals with all of the player animations and most of the logic, e.g. damage etc.
    def __init__(self,x,y,health):
        #every variable that is used with and by the player sprite
        self.x = x
        self.y = y
        self.vel = 7
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
        self.player_dmg = 30
        self.idle = True
        
    def draw_player(self, win):
      #these 'counts' control which image is displayed on the screen and increase in order to cycle through images
          #once they reach the end of the list, they are set to 0 in order to create that cycle of images
        if self.attack_count +1 >=18:
            self.attack_count = 0
        if self.h_walk_count  +1>=15:
            self.h_walk_count = 0
        if self.v_walk_count +1 >=12:
            self.v_walk_count = 0

      #these actions occur when a keybind is pressed in the main game loop
            #and deal with the animations of the player sprite - movement and attacking animations
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
            win.blit(r_attack[self.attack_count // 9], (self.x, self.y))
            self.attack_count +=1
        if self.l_attack:
            win.blit(l_attack[self.attack_count//9], (self.x, self.y))
            self.attack_count +=1
                    
class enemy():
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.idle_count = 0
        self.ghost_count = 0
        self.dead_count = 0
        self.health = health
        self.in_range = False
    def draw_demon(self, win):
        if self.health<0:
            self.health = 0
        if self.idle_count +1 >= 24:
            self.idle_count = 0
        if self.dead_count >=10:
            self.dead_count = 10

        dmg = random.randint(1,500)
        if player.x > self.x and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(demon_attack[self.idle_count // 9], (self.x, self.y))
            self.idle_count += 1
            if self.idle_count>=18:#dmg >=400:
                player.health -=1
            draw_text(str(self.health), font_ehealth, black, win, self.x+50, self.y+30)
        elif player.x < self.x and player.x >self.x-20 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(demon_attack_flip[self.idle_count // 9], (self.x, self.y))
            self.idle_count += 1
            draw_text(str(self.health), font_ehealth, black, win, self.x+50, self.y+30)
            if self.idle_count>=18:#dmg >=400:
                player.health -=1
        if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            if player.l_attack ==True or player.r_attack == True:
                if dmg >=400:
                    self.health -= player.player_dmg
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
        dmg = random.randint(1,500)
        if player.x > self.x - 35 and player.x < self.x + 85 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            draw_text(str(self.health), font_ehealth, black, win, self.x+55, self.y+20)            
            if dmg >=400:
                player.health -=1
            if player.l_attack ==True or player.r_attack == True:
                if dmg >=400:
                    self.health -= player.player_dmg


    def draw_rogue(self,win):
        if self.idle_count +1 >= 18:
            self.idle_count = 0
        if self.dead_count +1 >=12:
            self.dead_count = 12
        dmg = random.randint(1,500)
        if player.x > self.x -20 and player.x < self.x+40 and player.y > self.y-40 and player.y < self.y +20 and self.health>0:
            win.blit(rogue_attack[self.idle_count // 3], (self.x, self.y))
            self.idle_count += 1
            draw_text(str(self.health), font_ehealth, black, win, self.x+20, self.y-15)
            if dmg >=400:
                player.health -=1
            if player.l_attack ==True or player.r_attack == True:
                if dmg >=400:
                    self.health -= player.player_dmg
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

        dmg = random.randint(1,500)
        if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health>0:
            win.blit(ghost_attack[self.ghost_count // 3], (self.x, self.y))
            self.ghost_count += 1
            draw_text(str(self.health), font_ehealth, black, win, self.x+50, self.y+20)
            if dmg >=400:
                player.health -=1
            if player.l_attack ==True or player.r_attack == True:
                if dmg >=400:
                    self.health -= player.player_dmg
        elif self.health <=0:
            win.blit(ghost_dead[self.dead_count//3], (self.x,self.y))
            self.dead_count+=1
        else:
            win.blit(ghost_idle[self.idle_count//6], (self.x, self.y))
            self.idle_count +=1

class environment():
      #defining all variables used in the enemy class
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.door_count = 0
        self.chest_count = 0
        self.coin_count = 0
        self.trap_count = 0
        self.vel = 8
        self.picked_up = False
        self.red_key_up = False
        self.yellow_key_up = False
        self.blue_key_up = False
        self.green_key_up = False

        #this section of code deals with the animations of the coin that is dropped from 1 of the enemies;
        #it checks whether or not the enemy has been defeated, if so the coin will appear on screen;
        #then if the player is within range it will be picked up and appear in the inventory/UI aspect of the window
        # indictating it has been picked up and the chest can now be opened
    def coin_draw(self,win):
        if self.coin_count +1 >=18:
            self.coin_count = 0
            if player.x > self.x-65 and player.x <self.x+20 and player.y > self.y-65 and player.y <self.y+20 : 
                if level_num ==1 and demon_sprite.health<=0:
                    coin.picked_up = True
                if level_num ==2 and demon_sprite4.health <=0:
                    coin_2.picked_up = True
        if self.picked_up == True:
            win.blit(inventory_coin, (120,15))
        else:
            if level_num ==1:
                if demon_sprite.health <=0:
                    win.blit(coin_anim[self.coin_count//6], (self.x+40,self.y+40))
                    self.coin_count +=1
            elif level_num ==2:
                if demon_sprite4.health <=0:
                    win.blit(coin_anim[self.coin_count//6], (self.x+40,self.y+40))
                    self.coin_count +=1
      #This code checks to see if the coin has been picked up, if so the chest opens when the player is near it
      # if the player is within range their health will increase, up to 100
    def chest_draw(self,win):
        if coin.picked_up == True or coin_2.picked_up == True:
            if player.x > self.x-65 and player.x <self.x+20 and player.y > self.y-55 and player.y <self.y+20 :
                win.blit(chest_open[1], (self.x,self.y))
                if player.health <100:
                    player.health +=1
                else:
                    player.health+=0
            else:
                win.blit(chest_open[0], (self.x,self.y))
        else:
            win.blit(chest_open[0], (self.x,self.y))

      #this section deals the with the door, it checks to see if all the keys on a level have been collected'
            #if so the door will open and if the player is within range of the door they will advance
            #to the next level, or win!
    def door_draw(self,win):
        if self.door_count +1 >= 18:
            self.door_count = 0
        if level_num ==2:
            win.blit(door_open, (810,150))
            if key_red_2.red_key_up == True and key_yellow_2.yellow_key_up == True and key_green_2.green_key_up == True and key_blue_2.blue_key_up == True:
                win.blit(door_open, (self.x, self.y))
            else:
                win.blit(doors[self.door_count // 6], (self.x, self.y))
                self.door_count += 1
        elif level_num ==1:
            if key_red.red_key_up == True and key_yellow.yellow_key_up == True and key_green.green_key_up == True and key_blue.blue_key_up == True:
                win.blit(door_open, (self.x, self.y))
            else:
                win.blit(doors[self.door_count // 6], (self.x, self.y))
                self.door_count += 1
    def draw_level(self,win):
        win.blit(level_layout, (self.x, self.y))
        #this code animates the spike traps and checks to see if the player is stood on top of the trap;
            #if so the players health decreases
    def trap_draw(self,win):
        if self.trap_count +1>18:
            self.trap_count = 0
        dmg = random.randint(1,500)
        if player.x > self.x and player.x <self.x+20 and player.y > self.y-65 and player.y <self.y+20:
            win.blit(trap_images[self.trap_count//6], (self.x,self.y))
            self.trap_count +=1
            if dmg>=400 and player.health >=0+10:
                player.health -=10
        else:
            win.blit(trap_images[0], (self.x,self.y))
      #this section of code determines which animation set to use in order to display the fire trap;
      #depending on its direction/velocity
    def draw_fire_trap(self,win):
        if self.trap_count +1>18:
            self.trap_count = 0
        if player.x > self.x+63 and player.y> self.y+81 and player.x<self.x+130 and player.y< self.y+126:
            player.health -=1
        if self.vel ==8:
            win.blit(fire_trap_images[self.trap_count//9], (self.x,self.y))
            self.trap_count +=1
            if self.x <700:
                self.x+=self.vel
            else:
                self.vel = self.vel * -1
        if self.vel !=8:
            win.blit(fire_trap_images_flip[self.trap_count//9], (self.x,self.y))
            self.trap_count +=1
            if self.x >0:
                self.x+=self.vel
            else:
                self.vel = self.vel * -1
                
    #Controls the Red key animations and checks wether or not it has been picked up
    def red_key_draw (self,win):
        if level_num ==1:
            if rogue_sprite.health <=0 and key_red.red_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(red_key, (key_red.x+40, key_red.y+40))
                if player.x > key_red.x-65 and player.x <key_red.x+20 and player.y > key_red.y-55 and player.y <key_red.y+40 : 
                    key_red.red_key_up = True
        elif level_num ==2:
            if rogue_sprite4.health <=0 and key_red_2.red_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(red_key, (key_red_2.x+40,key_red_2.y+40))
                if player.x > key_red_2.x-65 and player.x <key_red_2.x+20 and player.y > key_red_2.y-55 and player.y <key_red_2.y+40 : 
                    key_red_2.red_key_up = True
        if self.red_key_up == True:
            win.blit(red_key, (175,30))

    #Controls the Yellow key animations and checks wether or not it has been picked up
    def yellow_key_draw (self,win):
        if level_num ==1:
            if ghost_sprite.health <=0 and key_yellow.yellow_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(yellow_key, (key_yellow.x+40,key_yellow.y+40))
                if player.x > key_yellow.x-65 and player.x <key_yellow.x+20 and player.y > key_yellow.y-55 and player.y <key_yellow.y+40 : 
                    key_yellow.yellow_key_up = True
        elif level_num ==2:
            if ghost_sprite4.health <=0 and key_yellow_2.yellow_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(yellow_key, (key_yellow_2.x+40,key_yellow_2.y+40))
                if player.x > key_yellow_2.x-65 and player.x <key_yellow_2.x+20 and player.y > key_yellow_2.y-55 and player.y <key_yellow_2.y+40 : 
                    key_yellow_2.yellow_key_up = True
        if self.yellow_key_up == True:
            win.blit(yellow_key, (215,30))
        
    #Controls the Green key animations and checks wether or not it has been picked up
    def green_key_draw (self,win):
        if level_num ==1:
            if demon_sprite_3.health <=0 and key_green.green_key_up ==False: 
                win.blit(green_key, (key_green.x+40,key_green.y+40))
                if player.x > key_green.x-65 and player.x <key_green.x+20 and player.y > key_green.y-55 and player.y <key_green.y+40 : 
                    key_green.green_key_up = True
        elif level_num ==2:
            if demon_sprite4.health <=0 and key_green_2.green_key_up ==False:
                win.blit(green_key, (key_green_2.x+40, key_green_2.y+40))
                if player.x > key_green_2.x-65 and player.x <key_green_2.x+20 and player.y > key_green_2.y-55 and player.y <key_green_2.y+40 : 
                    key_green_2.green_key_up = True
        if self.green_key_up == True:
            win.blit(green_key, (255,30))
    #Controls the Blue key animations and checks wether or not it has been picked up
    def blue_key_draw (self,win):
        if level_num ==1:
            if boss_sprite.health <=0 and key_blue.blue_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(blue_key, (key_blue.x+40,key_blue.y+40))
                if player.x > key_blue.x-65 and player.x <key_blue.x+20 and player.y > key_blue.y-55 and player.y <key_blue.y+40 : 
                    key_blue.blue_key_up = True
        elif level_num ==2:
            if boss_sprite4.health <=0 and key_blue_2.blue_key_up ==False: #and demon_sprite_2.health<=0 and demon_sprite_3.health <=0:
                win.blit(blue_key, (key_blue_2.x+40,key_blue_2.y+40))
                if player.x > key_blue_2.x-65 and player.x <key_blue_2.x+20 and player.y > key_blue_2.y-55 and player.y <key_blue_2.y+40 : 
                    key_blue_2.blue_key_up = True
        if self.blue_key_up == True:
            win.blit(blue_key, (295,30))

    def potion_draw(self,win):
        if self.picked_up == False:
            if potion_enemy ==1:
                if demon_sprite.health <=0:
                    win.blit(orange_pot, (self.x, self.y))
                else:
                    pass
            if potion_enemy ==2:
                if rogue_sprite2.health <=0:
                    win.blit(orange_pot, (self.x, self.y))
                else:
                    pass
            if potion_enemy == 3:
                if ghost_sprite3.health <=0:
                    win.blit(orange_pot, (self.x, self.y))
                else:
                    pass
        if player.x > self.x-65 and player.x <self.x+20 and player.y > self.y-65 and player.y <self.y+20 : 
            self.picked_up = True
        if self.picked_up == True:
            player.player_dmg = 20
            player.vel = 10
    
def draw_text(text, font, colour, surface, screen_x, screen_y):
    render = font.render(text, True, colour)
    text_surface = render.get_rect()
    text_surface = (screen_x, screen_y)
    win.blit(render, text_surface)

def update_window(): #function that draws all sprites, then updates the pygame window
    #Level 1 sprites/objects
    if level_num ==1:
        win.fill((28, 17, 23))#fills the pygame window

        draw_text(str(player.health), font_small, red, win, 10, 0)
        level_layout1.draw_level(win)

        door.door_draw(win)
        chest.chest_draw(win)
        
        #This passes the values/variables, associated with the various traps on the map, to the correct method
        trap.trap_draw(win)
        trap_2.trap_draw(win)
        trap_3.trap_draw(win)
        trap_4.trap_draw(win)
        trap_5.trap_draw(win)

        fire_trap.draw_fire_trap(win)
        fire2_trap.draw_fire_trap(win)
        fire3_trap.draw_fire_trap(win)
        fire4_trap.draw_fire_trap(win)

        #This passes the values/variables, associated with the boss sprites, to the correct method
        boss_sprite.draw_boss(win)
        boss_sprite_2.draw_boss(win)

        #This passes the values/variables, associated with the rogue sprites, to the correct method
        rogue_sprite.draw_rogue(win)
        rogue_sprite2.draw_rogue(win)
        rogue_sprite3.draw_rogue(win)
                
        #This passes the values/variables, associated with the demon sprites. to the correct method
        demon_sprite.draw_demon(win)
        demon_sprite_2.draw_demon(win)
        demon_sprite_3.draw_demon(win)
        
        #This passes the values/variables, associated with the ghost sprites, to the correct method
        ghost_sprite.draw_ghost(win)
        ghost_sprite2.draw_ghost(win)
        ghost_sprite3.draw_ghost(win)

        #This passes the values/variables, associated with the keys, to the correct method
        key_red.red_key_draw(win)
        key_yellow.yellow_key_draw(win)
        key_green.green_key_draw(win)
        key_blue.blue_key_draw(win)
        coin.coin_draw(win)

        rand_potion.potion_draw(win)

        #This passes the values/variables, associated with the player sprite, to the correct method
        player.draw_player(win)
    #Passing the values to the correct methods for level 2 
    if level_num ==2:
    #Level 2 sprites/objects
        win.fill((28, 17, 23))
        level_layout1.draw_level(win)
        draw_text(str(player.health), font_small, red, win, 10, 0)

        chest_2.chest_draw(win)
        door_2.door_draw(win)

        trap_6.trap_draw(win)
        trap_7.trap_draw(win)
        trap_8.trap_draw(win)
        trap_9.trap_draw(win)

        fire_trap.draw_fire_trap(win)
        fire2_trap.draw_fire_trap(win)
        fire3_trap.draw_fire_trap(win)
        fire4_trap.draw_fire_trap(win)

        demon_sprite4.draw_demon(win)
        demon_sprite5.draw_demon(win)
        demon_sprite6.draw_demon(win)

        rogue_sprite4.draw_rogue(win)
        rogue_sprite5.draw_rogue(win)
        rogue_sprite6.draw_rogue(win)

        ghost_sprite4.draw_ghost(win)
        ghost_sprite5.draw_ghost(win)
        ghost_sprite6.draw_ghost(win)

        boss_sprite3.draw_boss(win)
        boss_sprite4.draw_boss(win)

        key_red_2.red_key_draw(win)
        key_yellow_2.yellow_key_draw(win)
        key_green_2.green_key_draw(win)
        key_blue_2.blue_key_draw(win)
        coin_2.coin_draw(win)

        player.draw_player(win)

    if level_num ==3:
        win.fill((28,17,23))
        draw_text("GAME OVER!", font_big, red, win, screen_x/2-260, screen_y/2-75)
        draw_text("Press ESC to Exit...", font_small, red, win, screen_x/2-300, screen_y/2+50)

    if level_num == 4:
        win.fill((28,17,23))
        draw_text("YOU WIN!", font_big, red, win, screen_x/2-200, screen_y/2-75)
        draw_text("Press ESC to Exit...", font_small, red, win, screen_x/2-300, screen_y/2+50)
    
    if level_num ==5:
        win.fill((28, 17, 23))
        draw_text("Help", font_big, red, win, screen_x/2-100, screen_y/2-360)
        draw_text("WASD to move the character", font_help, red, win, screen_x/2-465, screen_y/2-200)
        draw_text("Q to attack left and E to attack right", font_help, red, win, screen_x/2-465, screen_y/2-100)
        draw_text("Defeat all enemies to collect the 4 keys", font_help, red, win, screen_x/2-465, screen_y/2)
        draw_text("Collect the coin to open the chest", font_help, red, win, screen_x/2-465, screen_y/2+100)
        draw_text("Press ESC to return to game...", font_help, red, win, screen_x/2-465, screen_y/2+200)

    pygame.display.update()#updates the pyame window

level_num = 1
chest_location = random.randint(1,3)

if normal_dif == True: 
    lvl_1_health = level_num*100
    lvl_2_health = level_num*110
elif hard_dif == True:
    lvl_1_health = level_num*110
    lvl_2_health = level_num*120

#level 1 values for all sprites, e.g. x, y, health etc.
demon_health = lvl_1_health
ghost_health = lvl_1_health+50
rogue_health = lvl_1_health-50
boss_health = lvl_1_health*3

demon_health_lvl2 = lvl_2_health
rogue_health_lvl2 = lvl_2_health-50
ghost_health_lvl2 = lvl_2_health+50
boss_health_lvl2 = lvl_2_health+200

player = player(400, 100, 100)#player(510, 110, 1000000)#Done
level_layout1 = environment(50, 50)

#Level 1 Enemy Values
demon_sprite = enemy(random.randint(45,172), random.randint(102,210), demon_health)#Done
demon_sprite_2 = enemy(random.randint(172,500), random.randint(195,412), demon_health)#Done
demon_sprite_3 = enemy(random.randint(500,700), random.randint(412,500), demon_health)#Done

rogue_sprite = enemy(random.randint(45,172), random.randint(210,412), rogue_health)#Done
rogue_sprite2 = enemy(random.randint(400,600), random.randint(102,195), rogue_health)#Done
rogue_sprite3 = enemy(random.randint(172, 500), random.randint(412,550), rogue_health)#Done

ghost_sprite = enemy(random.randint(45,172), random.randint(412,550), ghost_health)#Done
ghost_sprite2 = enemy(random.randint(172,400), random.randint(102,195), ghost_health)#Done
ghost_sprite3 = enemy(random.randint(500,700), random.randint(195,412), ghost_health)#Done

boss_sprite = enemy(655, 130, boss_health)#Done
boss_sprite_2 = enemy(775, 230, boss_health)#Done

fire_trap = environment(350,60)
fire2_trap = environment(200,175)
fire3_trap = environment(700,300)
fire4_trap = environment(500,425)

#Level 1 environmet object values
trap = environment(505,505)
trap_2 = environment(193,410)
trap_3 = environment(193,193)
trap_4 = environment (457, 217)

key_red = environment(rogue_sprite.x-20, rogue_sprite.y-30)
key_yellow = environment(ghost_sprite.x+10, ghost_sprite.y-20)
key_green = environment(demon_sprite_3.x+10, demon_sprite_3.y+30)
key_blue = environment(boss_sprite.x+15, boss_sprite.y)

door = environment(810, 150)#Done
coin = environment(demon_sprite.x+20, demon_sprite.y+30)

#Level 2 enemy values
demon_sprite4 = enemy(random.randint(100, 101), random.randint(100, 101), demon_health_lvl2)#Done
demon_sprite5 = enemy(random.randint(100, 101), random.randint(300, 301), demon_health_lvl2)#Done
demon_sprite6 = enemy(random.randint(700, 701), random.randint(500, 501), demon_health_lvl2)#Done

rogue_sprite4 = enemy(random.randint(300, 301), random.randint(100, 101), rogue_health_lvl2)#Done
rogue_sprite5 = enemy(random.randint(300, 301), random.randint(300, 301), rogue_health_lvl2)#Done
rogue_sprite6 = enemy(random.randint(300, 301), random.randint(500, 501), rogue_health_lvl2)#Done

ghost_sprite4 = enemy(random.randint(500, 501), random.randint(100, 101), ghost_health_lvl2)#Done
ghost_sprite5 = enemy(random.randint(500, 501), random.randint(300, 301), ghost_health_lvl2)#Done
ghost_sprite6 = enemy(random.randint(500, 501), random.randint(500, 501), ghost_health_lvl2)#Done

boss_sprite3 = enemy(100, 400, boss_health_lvl2)#Done
boss_sprite4 = enemy(200, 525, boss_health_lvl2)#Done


#Level 2 object values
key_red_2 = environment(rogue_sprite4.x-20, rogue_sprite4.y-30)
key_yellow_2 = environment(ghost_sprite4.x+10, ghost_sprite4.y-20)
key_green_2 = environment(demon_sprite4.x+10, demon_sprite4.y+30)
key_blue_2 = environment(boss_sprite4.x+15, boss_sprite4.y)

door_2 = environment(75, 525)#Done
coin_2 = environment(demon_sprite4.x+20, demon_sprite4.y+30)

trap_5 = environment(842, 555)
trap_6 = environment(193, 410)
trap_7 = environment(193, 193)
trap_8 = environment(457, 217)
trap_9 = environment(505, 505)

if chest_location == 1:
    chest = environment(85,120)
    chest_2 = environment(900, 610)
elif chest_location ==2:
    chest = environment(85,610)
    chest_2 = environment(900,120)
elif chest_location ==3:
    chest = environment(900, 610)
    chest_2 = environment(85,120)

potion_enemy = random.randint(1,3)
if potion_enemy == 1:
    rand_potion = environment(demon_sprite_2.x+55, demon_sprite_2.y+75)
elif potion_enemy ==2:
    rand_potion = environment(rogue_sprite2.x+20, rogue_sprite2.y+10)
elif potion_enemy ==3:
    rand_potion = environment(ghost_sprite3.x+55, ghost_sprite3.y+20)

#Time calculation code taken and adapted from https://www.codespeedy.com/how-to-create-a-stopwatch-in-python/
def export_time(sec):
    mins = sec//60
    sec = sec % 60
    hours = mins//60
    mins = mins % 60
    time_save = open("timer_output.txt", "a")
    time_save.write(text)
    time_save.write(" - {0}:{1}:{2}\n".format(int(hours), int(mins), (int(sec))))

#Main Loop, features keybinds, break conditions and level_num changes
if level_num !=4:
    start_time = time.time()
run = True
while run:
    keys = pygame.key.get_pressed() #collects all of the keys pressed by the player
    fps.tick(30) #allows me to tweak the Frames Per Second; by increasing it, the animations will look smoother, but will require more processing power
    for event in pygame.event.get(): #if the pygame window is exited - the loop breaks and the Quit() function is run
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            end_time = time.time()
            total_time = end_time - start_time
            export_time(total_time)
            run = False
    if player.health <0:
        player.health = 0
#keybind setup for character movement, character attack and temporary keybinds for testing
    if keys[pygame.K_r]:
        ghost_sprite.health = -1
        ghost_sprite2.health = -1
        ghost_sprite3.health = -1
        rogue_sprite.health = -1
        rogue_sprite2.health = -1
        rogue_sprite3.health = -1
        demon_sprite.health = -1
        demon_sprite_2.health = -1
        demon_sprite_3.health = -1
        boss_sprite.health = -1
        boss_sprite_2.health = -1
    if keys[pygame.K_LSHIFT] and keys[pygame.K_r]:
        ghost_sprite4.health = -1
        ghost_sprite5.health = -1
        ghost_sprite6.health = -1
        rogue_sprite4.health = -1
        rogue_sprite5.health = -1
        rogue_sprite6.health = -1
        demon_sprite4.health = -1
        demon_sprite5.health = -1
        demon_sprite6.health = -1
        boss_sprite3.health = -1
        boss_sprite4.health = -1
    if keys[pygame.K_t]:
        player.health = 1
    if keys[pygame.K_h] and level_num !=5:
        level_num =5
    if keys[pygame.K_ESCAPE] and level_num ==5:
        level_num =1
    elif keys[pygame.K_ESCAPE] and level_num ==3 or keys[pygame.K_ESCAPE] and level_num ==4:
        run = False
        #each keybind sets a specific variable to true which idicates which direction the player
        #wishes to move, this then triggers the animations in the player() class
    if keys[pygame.K_d] and keys[pygame.K_w] and player.y>82 and player.x <882:
        player.x +=player.vel
        player.y -= player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_a] and keys[pygame.K_w] and player.x >45 and player.y>82:
        player.x -=player.vel
        player.y -= player.vel
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_a] and keys[pygame.K_s] and player.y <570 and player.x >45:
        player.x -=player.vel
        player.y += player.vel
        player.left = True
        player.right = False
        player.up = False
        player.down = False
        player.l_attack = False
        player.r_attack = False
        player.idle = False
    elif keys[pygame.K_d] and keys[pygame.K_s] and player.x <882 and player.y <570:
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
        #checks to see if all keys have been picked up, if they have and player is within range of the door; the player adavances to the next level
        #each level triggers a new sety of sprites to be loaded in
    if key_red.red_key_up == True and key_yellow.yellow_key_up == True and key_green.green_key_up == True and key_blue.blue_key_up == True:
        if player.x > door.x-20 and player.x <door.x+50 and player.y > door.y-20 and player.y <door.y+50:
            coin.picked_up = False
            rand_potion.picked_up = False
            level_num = 2
    if key_red_2.red_key_up == True and key_yellow_2.yellow_key_up == True and key_green_2.green_key_up == True and key_blue_2.blue_key_up == True:
        if player.x > door_2.x-20 and player.x <door_2.x+50 and player.y > door_2.y-20 and player.y <door_2.y+50:
            level_num = 4
    if player.health <=0:
        level_num =3
        #pass
    update_window()
quit()
