
import pygame, random #libraries needed for this code to run 

#variables to store the values that determines the sizes of 
#the different sprites/images
demon_size = 130
rogue_size = 65
ghost_size = 130
door_size = 105
chest_size = 30
coin_size = 20
inv_coin_size = 50
slime_size = 140
trap_size = 48
key_size = 30
potion_size = 2


#This large section of code loads all of the images used throughout the program
# These images are used to create all the animations for each sprite and object in the game

#Images to animate the player sprite moving left
left1 =pygame.image.load("left0.png")
left2 =pygame.image.load("left1.png")
left3 =pygame.image.load("left2.png")
left4 =pygame.image.load("left3.png")
left5 =pygame.image.load("left4.png")
left6 =pygame.image.load("left5.png")

#Images to animate the player sprite moving right
right1 = pygame.image.load("right0.png")
right2 = pygame.image.load("right1.png")
right3 = pygame.image.load("right2.png")
right4 = pygame.image.load("right3.png")
right5 = pygame.image.load("right4.png")
right6 = pygame.image.load("right5.png")

#Images to animate the player sprite moving up
up1 =pygame.image.load("run0.png")
up2 =pygame.image.load("run1.png")
up3=pygame.image.load("run2.png")
up4=pygame.image.load("run3.png")
up5=pygame.image.load("run4.png")

#Images to animate the player sprite moving down
down1 =pygame.image.load("down0.png")
down2 =pygame.image.load("down1.png")
down3 =pygame.image.load("down2.png")
down4 =pygame.image.load("down3.png")
down5 =pygame.image.load("down4.png")

#Images to animate the player sprite attacking left
l_attack1 = pygame.image.load("l_attack1.png") 
l_attack2 = pygame.image.load("l_attack2.png") 
l_attack3 =  pygame.image.load("l_attack3.png") 

#Images to animate the player sprite attacing right
r_attack1 = pygame.image.load("r_attack1.png") 
r_attack2 = pygame.image.load("r_attack2.png") 
r_attack3 =  pygame.image.load("r_attack3.png") 

#Images to animate the player sprite stood still
idle1 = pygame.image.load("idle0.png")
idle2 = pygame.image.load("idle1.png")
idle3 = pygame.image.load("idle2.png")
idle4 = pygame.image.load("idle3.png")

#images to animate the demon sprite idleing
demon1 = pygame.image.load("ready_1.png")
demon2 =pygame.image.load("ready_2.png")
demon3 =pygame.image.load("ready_3.png")
demon4 =pygame.image.load("ready_4.png")
demon5 =pygame.image.load("ready_5.png")
demon6 = pygame.image.load("ready_6.png")
#Ressizing these images
demon1 = pygame.transform.scale(demon1, (demon_size, demon_size ))
demon2 = pygame.transform.scale(demon2, (demon_size, demon_size ))
demon3 = pygame.transform.scale(demon3, (demon_size, demon_size ))
demon4 = pygame.transform.scale(demon4, (demon_size, demon_size ))
demon5 = pygame.transform.scale(demon5, (demon_size, demon_size ))
demon6 = pygame.transform.scale(demon6, (demon_size, demon_size ))

#images used to animate the door whilst it's closed and the image
#of the open door
door1 = pygame.image.load("Door_Close_1.png")
door2 =pygame.image.load("Door_Close_2.png")
door3 =pygame.image.load("Door_Close_3.png")
door4 =pygame.image.load("Door_Close_4.png")
door_open = pygame.image.load("Door_Open.png")
#Resizing the images
door1 = pygame.transform.scale(door1, (door_size, door_size))
door2 = pygame.transform.scale(door2, (door_size, door_size))
door3 = pygame.transform.scale(door3, (door_size, door_size))
door4 = pygame.transform.scale(door4, (door_size, door_size))
door_open = pygame.transform.scale(door_open, (door_size, door_size))

#images to animate the demon sprite falling over
demon_dead_1 = pygame.image.load("dead_1.png")
demon_dead_2 = pygame.image.load("dead_2.png")
demon_dead_3 = pygame.image.load("dead_3.png")
demon_dead_4 = pygame.image.load("dead_4.png")
#Resizing the images
demon_dead_1 = pygame.transform.scale(demon_dead_1, (demon_size, demon_size))
demon_dead_2 = pygame.transform.scale(demon_dead_2, (demon_size, demon_size))
demon_dead_3 = pygame.transform.scale(demon_dead_3, (demon_size, demon_size))
demon_dead_4 = pygame.transform.scale(demon_dead_4, (demon_size, demon_size))

#images used to animate the demon attacking the player
demon_attack_1 = pygame.image.load("attack1_2.png")
demon_attack_2 = pygame.image.load("attack1_3.png")
demon_attack_3 = pygame.image.load("attack1_4.png")
demon_attack_4 = pygame.image.load("attack1_5.png")
#Resizing the images 
demon_attack_1 = pygame.transform.scale(demon_attack_1, (demon_size, demon_size))
demon_attack_2 = pygame.transform.scale(demon_attack_2, (demon_size, demon_size))
demon_attack_3 = pygame.transform.scale(demon_attack_3, (demon_size, demon_size))
demon_attack_4 = pygame.transform.scale(demon_attack_4, (demon_size, demon_size))
#Horizontally flipping the images to face where the player is on the screen
demon_attack_1_flip = pygame.transform.flip(demon_attack_1, True, False)
demon_attack_2_flip = pygame.transform.flip(demon_attack_2, True, False)
demon_attack_3_flip = pygame.transform.flip(demon_attack_3, True, False)
demon_attack_4_flip = pygame.transform.flip(demon_attack_4, True, False)

#images for the chest opening/closing animation
chest1 = pygame.image.load("chest1.png")
chest2 = pygame.image.load("chest2.png")
chest3 = pygame.image.load("chest3.png")
#Resizing the images
chest1 = pygame.transform.scale(chest1, (chest_size,chest_size))
chest2 = pygame.transform.scale(chest2, (chest_size,chest_size))
chest3 = pygame.transform.scale(chest3, (chest_size,chest_size))

#images used for the coin animation
coin1 = pygame.image.load("coin1.png")
coin2 = pygame.image.load("coin2.png")
coin3 = pygame.image.load("coin3.png")
coin4 = pygame.image.load("coin4.png")
#Resizing the images
coin1 = pygame.transform.scale(coin1, (coin_size,coin_size))
coin2 = pygame.transform.scale(coin2, (coin_size,coin_size))
coin3 = pygame.transform.scale(coin3, (coin_size,coin_size))

inventory_coin = pygame.image.load("coin1.png")
inventory_coin = pygame.transform.scale(inventory_coin, (inv_coin_size, inv_coin_size))

#Level Images
level_layout = pygame.image.load("level layout.png")
#level_layout = pygame.transform.scale(level_layout, (1400, 850))

#Slime/Boss images
slime1 = pygame.image.load("slime1.png")
slime2 = pygame.image.load("slime2.png")
slime3 = pygame.image.load("slime3.png")
slime4 = pygame.image.load("slime4.png")
#Resizing the images
slime1 = pygame.transform.scale(slime1, (slime_size, slime_size))
slime2 = pygame.transform.scale(slime2, (slime_size, slime_size))
slime3 = pygame.transform.scale(slime3, (slime_size, slime_size))
slime4 = pygame.transform.scale(slime4, (slime_size, slime_size))

#Slime defeated images
slime_dead1 = pygame.image.load("slime_dead1.png")
slime_dead2 = pygame.image.load("slime_dead2.png")
slime_dead3 = pygame.image.load("slime_dead3.png")
slime_dead4 = pygame.image.load("slime_dead4.png")
#Resizing the images
slime_dead1 = pygame.transform.scale(slime_dead1, (slime_size, slime_size))
slime_dead2 = pygame.transform.scale(slime_dead2, (slime_size, slime_size))
slime_dead3 = pygame.transform.scale(slime_dead3, (slime_size, slime_size))
slime_dead4 = pygame.transform.scale(slime_dead4, (slime_size, slime_size))

#Rogue attack Images
rogue_attack1 = pygame.image.load("rogue_attack1.png")
rogue_attack2 = pygame.image.load("rogue_attack2.png")
rogue_attack3 = pygame.image.load("rogue_attack3.png")
rogue_attack4 = pygame.image.load("rogue_attack4.png")
rogue_attack5 = pygame.image.load("rogue_attack5.png")
rogue_attack6 = pygame.image.load("rogue_attack6.png")
#Resizing the images
rogue_attack1 = pygame.transform.scale(rogue_attack1, (rogue_size, rogue_size))
rogue_attack2 = pygame.transform.scale(rogue_attack2, (rogue_size, rogue_size))
rogue_attack3 = pygame.transform.scale(rogue_attack3, (rogue_size, rogue_size))
rogue_attack4 = pygame.transform.scale(rogue_attack4, (rogue_size, rogue_size))
rogue_attack5 = pygame.transform.scale(rogue_attack5, (rogue_size, rogue_size))
rogue_attack6 = pygame.transform.scale(rogue_attack6, (rogue_size, rogue_size))

#Rogue idle images
rogue_idle1 = pygame.image.load("rogue_idle1.png")
rogue_idle2 = pygame.image.load("rogue_idle2.png")
rogue_idle3 = pygame.image.load("rogue_idle3.png")
rogue_idle4 = pygame.image.load("rogue_idle4.png")
#Resizing the images
rogue_idle1 = pygame.transform.scale(rogue_idle1, (rogue_size, rogue_size))
rogue_idle2 = pygame.transform.scale(rogue_idle2, (rogue_size, rogue_size))
rogue_idle3 = pygame.transform.scale(rogue_idle3, (rogue_size, rogue_size))
rogue_idle4 = pygame.transform.scale(rogue_idle4, (rogue_size, rogue_size))

#Rogue sprite death images
rogue_dead1 = pygame.image.load("rogue_dead1.png")
rogue_dead2 = pygame.image.load("rogue_dead2.png")
rogue_dead3 = pygame.image.load("rogue_dead3.png")
rogue_dead4 = pygame.image.load("rogue_dead4.png")
rogue_dead5 = pygame.image.load("rogue_dead5.png")
#Resizing the images
rogue_dead1 = pygame.transform.scale(rogue_dead1, (rogue_size, rogue_size))
rogue_dead2 = pygame.transform.scale(rogue_dead2, (rogue_size, rogue_size))
rogue_dead3 = pygame.transform.scale(rogue_dead3, (rogue_size, rogue_size))
rogue_dead4 = pygame.transform.scale(rogue_dead4, (rogue_size, rogue_size))
rogue_dead5 = pygame.transform.scale(rogue_dead5, (rogue_size, rogue_size))

#Ghost idle images
ghost_idle1 = pygame.image.load("ghost_idle1.png")
ghost_idle2 = pygame.image.load("ghost_idle2.png")
ghost_idle3 = pygame.image.load("ghost_idle3.png")
ghost_idle4 = pygame.image.load("ghost_idle4.png")
#Reszing the images
ghost_idle1 = pygame.transform.scale(ghost_idle1, (ghost_size, ghost_size))
ghost_idle2 = pygame.transform.scale(ghost_idle2, (ghost_size, ghost_size))
ghost_idle3 = pygame.transform.scale(ghost_idle3, (ghost_size, ghost_size))
ghost_idle4 = pygame.transform.scale(ghost_idle4, (ghost_size, ghost_size))

#Ghost attack images
ghost_attack1 = pygame.image.load("ghost_attack1.png")
ghost_attack2 = pygame.image.load("ghost_attack2.png")
ghost_attack3 = pygame.image.load("ghost_attack3.png")
ghost_attack4 = pygame.image.load("ghost_attack4.png")
ghost_attack5 = pygame.image.load("ghost_attack5.png")
ghost_attack6 = pygame.image.load("ghost_attack6.png")
#Resizing the images
ghost_attack1 = pygame.transform.scale(ghost_attack1, (ghost_size, ghost_size))
ghost_attack2 = pygame.transform.scale(ghost_attack2, (ghost_size, ghost_size))
ghost_attack3 = pygame.transform.scale(ghost_attack3, (ghost_size, ghost_size))
ghost_attack4 = pygame.transform.scale(ghost_attack4, (ghost_size, ghost_size))
ghost_attack5 = pygame.transform.scale(ghost_attack5, (ghost_size, ghost_size))
ghost_attack6 = pygame.transform.scale(ghost_attack6, (ghost_size, ghost_size))

#Ghost sprite death images
ghost_dead2 = pygame.image.load("ghost_dead2.png")
ghost_dead3 = pygame.image.load("ghost_dead3.png")
ghost_dead4 = pygame.image.load("ghost_dead4.png")
ghost_dead5 = pygame.image.load("ghost_dead5.png")
ghost_dead6 = pygame.image.load("ghost_dead6.png")
#Resizing these images
ghost_dead2 = pygame.transform.scale(ghost_dead2, (ghost_size, ghost_size))
ghost_dead3 = pygame.transform.scale(ghost_dead3, (ghost_size, ghost_size))
ghost_dead4 = pygame.transform.scale(ghost_dead4, (ghost_size, ghost_size))
ghost_dead5 = pygame.transform.scale(ghost_dead5, (ghost_size, ghost_size))
ghost_dead6 = pygame.transform.scale(ghost_dead6, (ghost_size, ghost_size))

#Spike trap images
trap1 = pygame.image.load("trap1.png")
trap2 = pygame.image.load("trap2.png")
trap3 = pygame.image.load("trap3.png")
trap4 = pygame.image.load("trap4.png")
#Resizing these images
trap1 = pygame.transform.scale(trap1, (trap_size, trap_size))
trap2 = pygame.transform.scale(trap2, (trap_size, trap_size))
trap3 = pygame.transform.scale(trap3, (trap_size, trap_size))
trap4 = pygame.transform.scale(trap4, (trap_size, trap_size))

#Key images
red_key = pygame.image.load("red_key.png")
green_key = pygame.image.load("green_key.png")
blue_key = pygame.image.load("blue_key.png")
yellow_key = pygame.image.load("yellow_key.png")
#Resizing the key images
red_key = pygame.transform.scale(red_key, (key_size, key_size))
green_key = pygame.transform.scale(green_key, (key_size, key_size))
blue_key = pygame.transform.scale(blue_key, (key_size, key_size))
yellow_key = pygame.transform.scale(yellow_key, (key_size, key_size))

#Potions images
orange_pot = pygame.image.load("orange_pot.png")
#Resizing the images
orange_pot = pygame.transform.scale(orange_pot, (potion_size, potion_size))

#Fire ball trap images
fireball_1 = pygame.image.load("fireball_1.png")
fireball_2 = pygame.image.load("fireball_2.png")
fireball_3 = pygame.image.load("fireball_3.png")
fireball_4 = pygame.image.load("fireball_4.png")
#Flipping these images
fireball_1_flip = pygame.transform.flip(fireball_1, True, False)
fireball_2_flip = pygame.transform.flip(fireball_2, True, False)
fireball_3_flip = pygame.transform.flip(fireball_3, True, False)
fireball_4_flip = pygame.transform.flip(fireball_4, True, False)

#Lists of each set of image, that are then cycled through to
#create the animations

#These lists are used store the images that animate 
#the player sprite
l_walk = [left1,left2,left3,left4,left5,left6]
r_walk = [right1,right2,right3,right4,right5,right6]
u_walk = [up1,up2,up3,up4,up5]
d_walk = [down1,down2,down3,down4,down5]
r_attack =[r_attack1,r_attack2,r_attack3]
l_attack = [l_attack1,l_attack2,l_attack3]
idle = [idle1, idle2, idle3,idle4]

#These lists are used to store the images that animate 
# the demon sprite images, when the sprite is facing right
demon_idle = [demon1, demon2, demon3, demon4, demon5, demon6]
demon_dead = [demon_dead_1, demon_dead_2, demon_dead_3, demon_dead_4]
demon_attack = [demon_attack_1, demon_attack_2, demon_attack_3, demon_attack_4]
#images for when the demon sprite is facing left
demon_attack_flip = [demon_attack_1_flip, demon_attack_2_flip, demon_attack_3_flip, demon_attack_4_flip]

#These lists are used to store the images that animate 
# the slime/boss sprite
slime_idle = [slime1, slime2, slime3, slime4]
slime_dead = [slime_dead1, slime_dead2, slime_dead3, slime_dead4]

#These lists are used to store the images that animate 
#certain parts of the evironent that the player can 
#interact with
chest_open = [chest1, chest2,chest3]
doors = [door1, door2, door3, door4]
coin_anim = [coin1, coin2, coin3, coin4]
trap_images = [trap1, trap2, trap3, trap4]
fire_trap_images = [fireball_1, fireball_2, fireball_3, fireball_4]
fire_trap_images_flip = [fireball_1_flip, fireball_2_flip, fireball_3_flip, fireball_4_flip]

#These lists are used store the images that
# animate the rogue sprite
rogue_attack = [rogue_attack1, rogue_attack2, rogue_attack3, rogue_attack4, rogue_attack5, rogue_attack6]
rogue_idle = [rogue_idle1, rogue_idle2, rogue_idle3, rogue_idle4]
rogue_dead = [rogue_dead1, rogue_dead2, rogue_dead3, rogue_dead4, rogue_dead5]

#These lists are used store the images that animate
# the ghost sprite
ghost_idle = [ghost_idle1, ghost_idle2, ghost_idle3, ghost_idle4]
ghost_attack = [ghost_attack1, ghost_attack2, ghost_attack3, ghost_attack4, ghost_attack5, ghost_attack6]
ghost_dead = [ghost_dead2, ghost_dead3, ghost_dead4, ghost_dead5, ghost_dead6]

#Images specific to the menu
menu_demon_size = 250
menu_demon = pygame.image.load("attack1_4.png")
menu_demon = pygame.transform.scale(menu_demon, (menu_demon_size, menu_demon_size))

menu_player_size = 150
menu_player = pygame.image.load("idle0.png")
menu_player = pygame.transform.scale(menu_player, (menu_player_size, menu_player_size))

#menu_chest_size = 50
#menu_chest = pygame.image.load("chest1.png")
#menu_chest = pygame.transform.scale(menu_chest, (menu_chest_size, menu_chest_size))
