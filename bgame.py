# ballet game
import pygame
import os
import button

f = open("about.txt", "r")
file = f.read().splitlines()
pygame.init()

# window constants: width, height, window title, window color, fps
WIDTH = 1000
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballet Game")
WINCOLOR = (255, 182, 193)
FPS = 60

#text constants
FONT = pygame.font.SysFont('arialblack', 40)
SMALLFONT = pygame.font.SysFont('arialblack', 20)
TEXTCOL = (170, 51, 106)

# images
BALLERINA0 = pygame.image.load('ballerina1.png')
START_IMG = pygame.image.load('start.png')
QUIT_IMG = pygame.image.load('quit.png')
ABOUT_IMG = pygame.image.load('about.png')
BACK_IMG = pygame.image.load('back.png')

#buttons
start_butt = button.Button(610, 100, START_IMG, .55)
quit_butt = button.Button(610, 250, QUIT_IMG, .8)
about_butt = button.Button(610, 400, ABOUT_IMG, .8)
back_butt = button.Button(10, 10, BACK_IMG, .3)

def draw_text(text, font, col, x, y):
    img = font.render(text, True, col)
    WINDOW.blit(img, (x, y))
    
def draw_start():
    WINDOW.fill(WINCOLOR)
    WINDOW.blit(BALLERINA0, (20, -5))
    draw_text('Ballet Game', FONT, TEXTCOL, 600, 20)
    start_butt.draw(WINDOW)
    quit_butt.draw(WINDOW)
    about_butt.draw(WINDOW)
    # update display manually every time it changes
    pygame.display.update()

def draw_games():
    WINDOW.fill(WINCOLOR)
    back_butt.draw(WINDOW)
    pygame.display.update()

def draw_about():
    WINDOW.fill(WINCOLOR)
    spacing = 70
    for item in file:
        draw_text(item, SMALLFONT, TEXTCOL, 50, spacing)
        spacing = spacing + 20
    back_butt.draw(WINDOW)
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True

    draw_start()
    
    while run:
        clock.tick(FPS)
        if start_butt.draw(WINDOW):
            draw_games()
        if quit_butt.draw(WINDOW):
            run = False
        if about_butt.draw(WINDOW):
            draw_about()
        if back_butt.draw(WINDOW):
            draw_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    f.close()
    pygame.quit()


# will only run main if running this file
if __name__ == "__main__":
    main()
