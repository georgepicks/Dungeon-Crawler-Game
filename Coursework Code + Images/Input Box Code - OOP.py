import pygame

pygame.init()
screen = pygame.display.set_mode((400,200))
font = pygame.font.Font("Retro.ttf", 32)

white = (255,255,255)
red = (255,0,0)

text = ""

def draw_text(text, font, colour, surface, screen_x, screen_y):
    render = font.render(text, True, colour)
    text_surface = render.get_rect()
    text_surface = (screen_x, screen_y)
    screen.blit(render, text_surface)
    
run = True

while run == True:
    screen.fill((28, 17, 23))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text = ""
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
    
        draw_text(text, font, red, screen, 200, 100)    
        pygame.display.flip()

