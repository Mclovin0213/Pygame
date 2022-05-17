import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    
    def __init__(self):
        pygame.init() #Starts Pygame
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption('Alien Invasion') #Sets display caption
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        while True:
            self._check_events() 
            self.ship.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get(): #.event.get() returns a list of events that have occured within the loop
            if event.type == pygame.QUIT: #Checks if close button is clicked
                sys.exit() #exits game
            elif event.type == pygame.KEYDOWN: #checks for any key press
                self._check_keydown_events(event)    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT: #mages sure key press is right arrow
            self.ship.moving_right = True      
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #redrawing screen each pass of loop
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        pygame.display.flip() #Makes the most recently drawn screen visible
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()