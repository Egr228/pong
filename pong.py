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

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

x_hero = 400
y_hero = 400
speed_hero = 10

game = True

FPS = 60

clock = time.Clock()

window = display.set_mode((1000,625))
display.set_caption('JoJong’s Bizarre Adventure')
background = transform.scale(image.load('d.jpg'),(1000,625))

game_sprite = GameSprite('original-6005178dc77cc.jpg',200, 200, x_hero, y_hero, speed_hero)
game_sprite2 = GameSprite('Ha877df28b2954cb18ba0ceb42b0ff9a09.png',200, 400, x_hero, y_hero, speed_hero)

game = True
while game:
    for el in event.get():
        if el.type == QUIT:
            game = False
    window.blit(background,(0,0))
    game_sprite.reset()


    clock.tick(FPS)
    time.delay(5)

    display.update()
    clock.tick(FPS)

