import pygame

class Button():
    def __init__(self,x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        #check if mouse over
        if self.rect.collidepoint(pos):
            #changes clicked to True when mouse is over rect and left clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        #changes clicked back to false after clicking a button so you can click again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
