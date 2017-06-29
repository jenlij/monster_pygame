import pygame
import random

def randomizer():
    
def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    

    class Monster(object):
        def __init__(self,name, x, y, screen_width, screen_height):
            self.name = name
            self.x = x
            self.y = y
            self.screen_width = screen_width
            self.screen_height = screen_height
        
        def move_east(self, icon, speed):
            self.x += speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width:
                self.x = 0
        def move_west(self, icon, speed):
            self.x -= speed
            screen.blit(icon, (self.x, self.y))
            if self.x <= 0:
                self.x = self.screen_width
        def move_south(self, icon, speed):
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.y >= self.screen_height:
                self.y = 0
        def move_north(self, icon, speed):
            self.y -= speed
            screen.blit(icon, (self.x, self.y))
            if self.y <= 0:
                self.y = self.screen_height
        def move_se(self, icon, speed):
            self.x += speed
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width or self.y >= self.screen_height:
                self.x = 0
                self.y = 0
        def move_sw(self, icon, speed):
            self.x -= speed
            self.y += speed
            screen.blit(icon, (self.x, self.y))
            if self.x <= 0 or self.y >= self.screen_height:
                self.x = self.screen_width
                self.y = 0
        def move_ne(self, icon, speed):
            self.x += speed
            self.y -= speed
            screen.blit(icon, (self.x, self.y))
            if self.x >= self.screen_width or self.y <= 0:
                self.x = 0
                self.y = self.screen_height
        def move_nw(self, icon, speed):
            self.x -= speed
            self.y -= speed   
            screen.blit(icon, (self.x, self.y))     
            if self.x <= 0 or self.y >= self.y <= 0:
                self.x = self.screen_width
                self.y = self.screen_height

    # Game initialization
    monster_x = 50
    monster_y = 50
    monster = Monster("Monster", monster_x, monster_y, width, height)
    stop_game = False

    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, (0, 0))
        # Game display
        screen.blit(hero_image, (510/2, 480/2))
        
        monster.move_nw(monster_image,2)
        

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
