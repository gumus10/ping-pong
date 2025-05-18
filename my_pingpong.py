from pygame import *
from random import randint
from time import time as timer
#подгружаем отдельно функции для работы со шрифто

#фоновая м


#нам нужны такие картинки:
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE',True,(180,0,0))

font1 = font.Font(None, 35)
lose2 = font1.render('PLAYER 2 LOSE',True,(180,0,0))
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        super().__init__()
 
 
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
 
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 250:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 250:
            self.rect.y += self.speed

#класс спрайта-врага  


        
#класс спрайта-пули  

#создаём окошко
back = (0,255,255)
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
#background = transform.scale(image.load(img_back), (win_width, win_height))
window.fill(back)
#создаём ракетки
racket1 = Player('racket.png', 5, win_height - 100, 50, 100, 10)
racket2 = Player('racket.png', 645, win_height - 100, 50, 100, 10)
ball = GameSprite('tenis_ball.png',300,win_height - 50,50,50,10)


#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
clock = time.Clock()
start = timer()
Reload = False


speed_x = 3
speed_y = 3 
while run:
    #событие нажатия на кнопку Закрыть
    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    racket2.reset()

    

    ball.update()
    ball.reset()
    if finish != True:  
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1

    for e in event.get():
        if e.type == QUIT:
            run = False

    if ball.rect.x < -1:
        finish = True
        window.blit(lose1,(200,200))

    if ball.rect.x > 690:
        finish = True
        window.blit(lose2,(200,200))
        #событие нажатия на пробел - спрайт стреляет

 
    clock.tick(40)
    display.update()