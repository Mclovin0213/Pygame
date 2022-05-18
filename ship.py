import pygame

class Ship:
    def __init__(self,ai_game): #passing instance of game
        self.screen = ai_game.screen #sets screen from instance
        self.screen_rect = ai_game.screen.get_rect() #sets screen rectangle from instance, get_rect() gets rectangle
        
        self.settings = ai_game.settings #allowing access to instance settings
        
        self.image = pygame.image.load('images/ship.bmp') #how to load image
        self.rect = self.image.get_rect() #sets the ship rectangle to image rectange
        self.rect.midbottom = self.screen_rect.midbottom #sets ship to be placed midbottom of screen (other keywords(x,y))
        
        self.x = float(self.rect.x)
        
        self.moving_right = False #Movement flag
        self.moving_left = False

    def update(self):
        # Update the ship's position based on the movement
        if self.moving_right and self.rect.right < self.screen_rect.right: #checks if we are going right and if right edge of ship is behind right edge of screen
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x #update rect object from self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect) #.blit() draws one image on top of another    
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)    