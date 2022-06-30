from site import venv
from tkinter import font
from pygame import time, image, transform, display

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)



# display_params
display_width = 900
display_height = 700


# car_settings
crashed = False
car_width = 73
car_speed = 0

# модуль для времени, чтобы мониторить кадры в секунду
clock = time.Clock()

carImg = image.load('car1.png')  # картинка для игрока
carImg = transform.scale(carImg, (95, 85))  # задаем размер картинки, если большая
enemyImg = image.load('enemy.png') # enemy pic
enemyImg = transform.scale(enemyImg, (130, 95))
fonImg = image.load ('fon.png')
fonImg = transform.scale (fonImg, (900,700))
fongameImg = image.load ('fon2.png')
fongameImg = transform.scale (fongameImg, (900,700))
gameDisplay = display.set_mode((display_width, display_height))
display.set_caption("Supercar")  # название игры