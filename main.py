import pygame as pg
import time
import random as rd

window_x = 200
window_y = 150
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
Yellow = pg.Color(255, 255, 0)

# Geschwindigkeit der Schlange
snake_speen = 15

pg.init()

window = pg.display().'Snake'

fps = pg.time()

snake_position = (100, 60)
snake_bode = [
    [100, 60]
    [100, 50]
    [100, 40]
    [100, 30]
]

# Frucht Position festlegen
fruit_posirion =  [(rd.randint(window_x) // 10 ) * 10, 
                   (rd.randint(window_y) // 10 ) * 10]

fruit_spawn = True

dierection = 'RIGHT'
change_to_direction = dierection

# Startscpre festlegen
score = 0

# Scoreposition erstellen
def Showscore(color, size, font, choise):

    score_font = pg.font(font, size)

    score_ract = score_surface.get_rect()

    window.blid(score_surface)
    