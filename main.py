import pygame as pg
import time
import random as rd

# Bildschirmgröße festlegen
window_x = 720
window_y = 400

# Farbe erstellen
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
Yellow = pg.Color(255, 255, 0)

# Geschwindigkeit der Schlange
snake_speen = 15

# Pygame initialisieren
pg.init()

# Fenster erstellen
pg.display.set_caption('Snake')
window = pg.display.set_mode(window_x, window_y)

# FPS Kontrolle
fps = pg.time.Clock()

# Position der Schlange
snake_position = [100, 50]

# Teile der Schlange erstellen
snake_body = [
    [100, 50]
    [90, 50]
    [80, 50]
    [70, 50]
]

# Frucht Position festlegen
fruit_position =  [rd.randrange(1, (window_x // 10 ) * 10),
                   rd.randrange(1, (window_y // 10 ) * 10)
                    ]

fruit_spawn = True

dierection = 'RIGHT'
change_to_direction = dierection

# Startscpre festlegen
score = 0

# Scoreposition erstellen
def Showscore(color, size, font, choise):
    # Font des Scores erstellen
    score_font = pg.font.SysFont(font, size)
    score_surface = score_font.render(f"score: {score}", True, color)
    score_ract = score_surface.get_rect()
    # Text zeichnen
    window.blit(score_surface, score_ract)

def game_over():
    # Font für Game Over erstellen
    my_font = pg.font.SysFont('times new roman', 50)
    ## Getract auf dem Bildschirm erstellen
    game_over_surface = my_font.render(f"Your final score is: {score}", True, red)
    # Rechteck für den Text erstellen
    game_over_ract = game_over_surface.get_rect()
    # Position des Textes festlege
    game_over_ract.midtop = (window_x / 2, window_y / 4)

    window.blit(game_over_surface, game_over_ract)
    pg.display.flip()
    # 2 Sekunden warten
    time.sleep(2)
    # Pygame beenden
    pg.quit()
    # Programm beenden
    quit()

while True:

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                change_to = "UP"
            if event.key == pg.K_DOWN:
                change_to = "DOWN"
            if event.key == pg.K_LEFT:
                change_to = "LEFT"
            if event.key == pg.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and dierection != "DOWN":
        dierection = "UP"
    if change_to == "DOWN" and dierection != "UP":
        dierection = "DOWN"
    if change_to == "LEFT" and dierection != "RIGHT":
        dierection = "LEFT"
    if change_to == "RIGHT" and dierection != "LEFT":
        dierection = "RIGHT"


    if dierection == "UP":
        snake_position[1] -= 10
    if dierection == "DOWN":
        snake_position[1] += 10
    if dierection == "LEFT":
        snake_position[0] -= 10
    if dierection == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10 
        fruit_spawn = False