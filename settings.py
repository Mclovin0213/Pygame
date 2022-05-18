class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) #setting background color
        
        # Ship settings
        self.ship_speed = 0.9 #
        
        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 15
        
        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 7
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        