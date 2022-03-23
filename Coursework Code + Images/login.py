import pygame
pygame.init()

screen_x = 300
screen_y = 500

#Setting the Font and clour used in the login section 
font = pygame.font.Font("Retro.ttf", 150)
red = (255,0,0)
white = (255,255,255)

win = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Login Window")
username_ph = ""
password_ph = ""

def draw_text(text, font, colour, surface, screen_x, screen_y):
        render = font.render(text, True, colour)
        text_surface = render.get_rect()
        text_surface = (screen_x, screen_y)
        win.blit(render, text_surface)

run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(win, red, (screen_x/2, screen_y/2, 100,50))
    #draw_text("Test", font, white, win, screen_x/2-110, screen_y/2-150)
    pygame.display.update()
pygame.quit()