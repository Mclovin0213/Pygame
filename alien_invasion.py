import sys

import pygame

from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init() #Starts Pygame
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)) #Displays window 'H,W'
        
        pygame.display.set_caption('Alien Invasion') #Sets display caption
        
    def run_game(self):
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get(): #.event.get() returns a list of events that have occured within the loop
                if event.type == pygame.QUIT: #Checks if close button is clicked
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color) #redrawing screen each pass of loop
                    
            pygame.display.flip() #Makes the most recently drawn screen visible

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()