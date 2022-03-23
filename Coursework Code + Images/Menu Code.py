import pygame, sys

pygame.init()
pygame.display.set_caption('Menu')

x = 800
y = 800
screen = pygame.display.set_mode((x, y))

font = pygame.font.SysFont('Calibri', 35)
font_colour = (0,0,0)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

click = False
 
def main_menu():
    while True:
        button_1 = pygame.Rect(x/2-45, y/2, 100, 50)
        button_2 = pygame.Rect(x/2-70, y/2+50, 100, 50)
        button_3 = pygame.Rect(x/2-45, y/2+100, 100, 50)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0,0), button_2)
        pygame.draw.rect(screen, (255, 0,0), button_3)
        
        screen.fill((255,255,255))
        #screen.blit(bg, (-100, -100))
        draw_text('Main Menu', font, font_colour, screen, x/2-90, y/2-50)
        draw_text('Play', font, font_colour, button_1, x/2-45, y/2)
        draw_text('Options', font, font_colour, button_2, x/2-70, y/2+50)
        draw_text("Quit", font, font_colour, button_3, x/2-45, y/2+100)

        

        mx, my = pygame.mouse.get_pos()         
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()

def Quit():
      pygame.quit()
      quit()        
      pygame.display.update()

