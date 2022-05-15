import pygame

class Ship:
    def __init__(self,ai_game): #passing instance of game
        self.screen = ai_game.screen #sets screen from instance
        self.screen_rect = ai_game.screen.get_rect() #sets screen rectangle from instance, get_rect() gets rectangle
        
        self.image = pygame.image.load('images/ship.bmp') #how to load image
        self.rect = self.image.get_rect() #sets the ship rectangle to image rectange
        self.rect.midbottom = self.screen_rect.midbottom #sets ship to be placed midbottom of screen (other keywords(x,y))
    
    def blitme(self):
        self.screen.blit(self.image, self.rect) #.blit() draws one image on top of another        