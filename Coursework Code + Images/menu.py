#libraries needed in order for the code to run
import pygame, time
#external file of images imported into pygame
from images import *
pygame.init()

#Dimensions of the pygame window
screen_x = 450
screen_y = 500

#establishing the window size and the caption of the window
win = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Menu Window")

#Setting the Font used for the menu options
font = pygame.font.Font("retro.ttf", 150)
font_small = pygame.font.Font("retro.ttf", 50)

#RGB  colour Values
white = (255,255,255)
red = (255,0,0)


def draw_text(text, font, colour, surface, screen_x, screen_y):
    render = font.render(text, True, colour)
    text_surface = render.get_rect()
    text_surface = (screen_x, screen_y)
    win.blit(render, text_surface)

def menu():
    global play, Quit
    play = True
    Quit = False
    run = True
    #Main Loop
    while run:
        win.fill((28, 17, 23))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        win.blit(menu_demon, (-60, -60))
        win.blit(menu_player,(310,320))        
        #win.blit(menu_chest, (40,400))

        if play ==True:
                if keys[pygame.K_s]:
                    Quit = True
                    play = False
                else:
                    play = True
        if Quit ==True:
            if keys[pygame.K_w]:
                play = True
                Quit = False
            else:
                Quit = True
        elif keys[pygame.K_ESCAPE]:
            quit()
        if play ==True:
            if keys[pygame.K_RETURN]:
                run = False
                difficulty()
            draw_text("Play", font, white, win, screen_x/2-110, screen_y/2-150)
        else:
            draw_text("Play", font, red, win, screen_x/2-110, screen_y/2-150)
        if Quit ==True:
            if keys[pygame.K_RETURN]:
                quit()
            draw_text("Quit", font, white, win, screen_x/2-110, screen_y/2+20)
        else:
            draw_text("Quit", font, red, win, screen_x/2-110, screen_y/2+20)
        pygame.display.update()

def difficulty():
    global normal, hard, normal_dif, hard_dif
    normal = False
    hard = False
    normal_dif = False
    hard_dif = False
    run = True
    while run:
        win.fill((28,17,23))
        keys = pygame.key.get_pressed()
        draw_text("Select Difficulty:", font_small, white, win, screen_x/2-155, screen_y/2-200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if normal != True and hard!= True:
            if keys[pygame.K_w] or keys[pygame.K_s]:
                normal = True
        if normal ==True:
                if keys[pygame.K_s]:
                    hard = True
                    normal = False
                else:
                    normal = True
        if hard ==True:
            if keys[pygame.K_w]:
                normal = True
                hard = False
            else:
                hard = True
        elif keys[pygame.K_ESCAPE]:
            quit()
        if normal ==True:
            if keys[pygame.K_RETURN]:
                normal_dif = True
                run = False
                user_name()
            draw_text("Normal", font, white, win, screen_x/2-165, screen_y/2-150)
        else:
            draw_text("Normal", font, red, win, screen_x/2-165, screen_y/2-150)
            
        if hard ==True:
            if keys[pygame.K_RETURN]:
                hard_dif = True
                run = False
                user_name()
            draw_text("Hard", font, white, win, screen_x/2-110, screen_y/2)
        else:
            draw_text("Hard", font, red, win, screen_x/2-110, screen_y/2)
        pygame.display.update()
        #Reading the .txt file and printing the contents onto the screen
        #time_read = open("timer_output.txt", "r")
        #previous_time = time_read.readlines()
        #previous = len(previous_time)
        #draw_text(str(previous_time[previous-1]), font_small, red, win, screen_x/2-170, screen_y/2+150)
        #time_read.close()
        #pygame.display.update()

def user_name():
    global text
    text = ""
    run = True
    while run:
        win.fill((28, 17, 23))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(text)
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                #VALIDATION
                elif len(text) <11:
                    text += event.unicode
            draw_text("Create a username:", font_small, white, win, screen_x/2-170, screen_y/2-100)
            draw_text(text, font_small, red, win, screen_x/2-130, screen_y/2) 
            draw_text("Press H for help screen", font_small, red, win, screen_x/2-200, screen_y/2+100)
            pygame.display.flip()
menu()
