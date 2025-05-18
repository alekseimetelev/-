from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((500, 600))
display.set_caption("гонки 2д")

class player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):

        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 450:
            self.rect.x += self.speed

        

mycar = player('car1.png', 250, 300, 2)

game = True
while game:
   
    mycar.update()
    mycar.reset()

    for e in event.get():
       if e.type == QUIT:
            game = False
 
    display.update()