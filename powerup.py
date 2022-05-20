import pygame

class Power_Up():
    def __init__(self, _alien_, ai_game):
        #Initializing things
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Making rect and adjusting its position
        self.rect = pygame.Rect(0, 0, 10, 10)
        
        