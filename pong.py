from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def move_hero(self):
        if keypressed[K_w] and self.rect.y <= 1000:
            self.rect.x += self.speed
        if keypressed[K_s] and self.rect.y >= 0:
            self.rect.x -= self.speed

x_hero = 400
y_hero = 400
speed_hero = 10

game = True

FPS = 60

clock = time.Clock()

window = display.set_mode((1000,625))
display.set_caption('Just_pong')
background = transform.scale(image.load('d.jpg'),(1000,625))

game = True
while game:
    for el in event.get():
        if el.type == QUIT:
            game = False
    window.blit(background,(0,0))

    clock.tick(FPS)
    time.delay(5)

    display.update()
    clock.tick(FPS)

