import pygame
import random

def main():
    width = 700
    height = 700
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    
    KEY_UP = 273
    KEY_DOWN = 274
    KEY_LEFT = 276
    KEY_RIGHT = 275

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
     
    class Hero(object):
        def __init__(self,name, x, y, play_area_width, play_area_height):
            self.name = name
            self.x = x
            self.y = y
            self.play_area_width = play_area_width
            self.play_area_height = play_area_height


    # Game initialization
    monster_x = 50
    monster_y = 50
    monster = Monster("Monster", monster_x, monster_y, width, height)
    random_num = 3
    change_dir_countdown = 120
    stop_game = False
    
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(pygame.transform.scale(background_image,(700,700)), (0, 0))
        # Game display
        screen.blit(hero_image, (510/2, 480/2))
        
        #move the monster random directions
        
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            random_num = random.randint(1,8)

        if random_num == 1:     
            monster.move_east(monster_image, 2)
        elif random_num == 2:
            monster.move_west(monster_image, 2)
        elif random_num == 3:
            monster.move_north(monster_image, 2)          
        elif random_num == 4:
            monster.move_south(monster_image, 2)
        elif random_num == 5:
            monster.move_ne(monster_image, 2)
        elif random_num == 6:
            monster.move_nw(monster_image, 2)
        elif random_num == 7:
            monster.move_se(monster_image, 2)   
        elif random_num == 8:
            monster.move_sw(monster_image, 2)                   


        change_dir_countdown -= 1    


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
