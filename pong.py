from pygame import *

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, player_x, player_y, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = speed_x
        self.speed = speed_y
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def move_hero(self):
        if keypressed[K_DOWN] and self.rect.y <= 1000:
            self.rect.y += self.speed
        if keypressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed

    def move_hero2(self):
        if keypressed[K_s] and self.rect.y <= 1000:
            self.rect.y += self.speed
        if keypressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

x_hero = 650
y_hero = 200

x_hero2 = 100
y_hero2 = 200

x_ball = 450
y_ball = 290

speed_herox = 10
speed_heroy = 10
speed_ballx = 10
speed_bally = 10

game = True

FPS = 60

clock = time.Clock()

window = display.set_mode((1000,625))
display.set_caption('JoJong’s Bizarre Adventure')
background = transform.scale(image.load('d.jpg'),(1000,625))

game_sprite = GameSprite('original-6005178dc77cc.jpg', 200, 250, x_hero, y_hero, speed_herox, speed_heroy)
game_sprite2 = GameSprite('Ha877df28b2954cb18ba0ceb42b0ff9a09.png', 250, 250, x_hero2, y_hero2, speed_herox, speed_heroy)
ball = GameSprite('original-5deec80967329.jpeg', 100, 100, x_ball, y_ball, speed_ballx, speed_bally)

game = True
while game:
    for el in event.get():
        if el.type == QUIT:
            game = False 
        
    if finish != True:
       ball.rect.x += speed_ballx
       ball.rect.y += speed_bally

    if ball.rect.y > 625-50 or ball.rect.y < 0:
        speed_bally *= -1
            
    window.blit(background,(0,0))
    game_sprite.reset()
    game_sprite2.reset()
    ball.reset()

    keypressed = key.get_pressed()
    game_sprite.move_hero()
    game_sprite2.move_hero2()



    clock.tick(FPS)
    time.delay(5)

    display.update()
    clock.tick(FPS)

