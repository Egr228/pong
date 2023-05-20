from pygame import *
muda = 0
whry = 0

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


x_hero = 760
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
background = transform.scale(image.load('background.jpg'),(1000,625))
mixer.init()
mixer.music.load('JOSTARS_Tommy_Tominaga_Coda_Jin_Hashimoto_-_End_of_THE_WORLD_Sono_Chi_no_Kioku_66172193.ogg')
mixer.music.play()

game_sprite = GameSprite('Без названия144_20230518212223.png', 100, 250, x_hero, y_hero, speed_herox, speed_heroy)
game_sprite2 = GameSprite('Без названия143_20230518182259.png', 100, 250, x_hero2, y_hero2, speed_herox, speed_heroy)
ball = GameSprite('Без названия140_20230517190736.png', 100, 100, x_ball, y_ball, speed_ballx, speed_bally)

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

    if ball.rect.x > 625-50 or ball.rect.y < 0:
        speed_bally *= -1
    
    if sprite.collide_rect(game_sprite, ball):
        speed_ballx *= -1

    if sprite.collide_rect(game_sprite2, ball):
        speed_ballx *= -1
            
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

