level_num = 1

if level_num ==1:
    demon_health = 100
    ghost_health = 125
    rogue_health = 75
    boss_health = 200

    player = player(510, 110, 1000000)#Done
    health_bar = health(-15,-65)#Done

    demon_sprite = enemy(150, 525, demon_health)#Done
    demon_sprite_2 = enemy(150, 65, demon_health)#Done
    demon_sprite_3 = enemy(800, 430, demon_health)#Done

    rogue_sprite = enemy(75, 350, rogue_health)#Done
    rogue_sprite2 = enemy(600, 575, rogue_health)#Done
    rogue_sprite3 = enemy(400, 125, rogue_health)#Done

    ghost_sprite = enemy(40, 200, ghost_health)#Done
    ghost_sprite2 = enemy(350, 550, ghost_health)#Done
    ghost_sprite3 = enemy(350, 300, ghost_health)#Done

    coin = environment(demon_sprite_2.x, demon_sprite_2.y+50)#Done
    door = environment(810, 150)#Done
    chest = environment(490,490)
    level_layout1 = environment(50,50)

    boss_sprite = enemy(795, 250, boss_health)#Done
if level_num ==2:
        demon_sprite = enemy(500, 525, demon_health)#Done