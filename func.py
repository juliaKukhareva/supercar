import time
from const import black, gameDisplay, carImg, display_width, display_height, enemyImg,fonImg
import pygame


# считаем сколько раз мы проехали мимо помехи
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


# функция для появляющихся элеметов на дороге
def things(thingx, thingy):
    gameDisplay.blit(enemyImg, [thingx, thingy] )

def fon(fonImg):
    gameDisplay.blit(fonImg, (0 , 0))

# функция для отрисовки машины, параметры = позиция
def car(img, x, y ):
    gameDisplay.blit(img, (x, y))



# функция выводит текст
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# функция, которая вызывает в себе результат 2 предыдущих функций
def crash():
    message_display('You Crashed')


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    from main import game_loop
    game_loop()