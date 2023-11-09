import pygame as pg
import time
import random as rd

# Bildschirmgröße festlegen
window_x = 720
window_y = 480

# Farbe erstellen
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
blue = pg.Color(0, 0, 255)
Yellow = pg.Color(255, 255, 0)
black = pg.Color(0,0,0)
white = pg.Color(255,255,255)

# Geschwindigkeit der Schlange
snake_speed = 15

# Pygame initialisieren
pg.init()

# Fenster erstellen
pg.display.set_caption('Snake')
window = pg.display.set_mode((window_x, window_y))

# FPS Kontrolle
fps = pg.time.Clock()

# Position der Schlange
snake_position = [100, 50]


# Teile der Schlange erstellen
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Frucht Position festlegen
fruit_position =  [rd.randrange(1, (window_x // 10 )) * 10,
                   rd.randrange(1, (window_y // 10 )) * 10
                    ]

fruit_spawn = True

direction = 'RIGHT'
change_to_direction = direction

# Startscpre festlegen
score = 0

# Scoreposition erstellen
def Showscore(choice,color, font, size):

    # Font des Scores erstellen
    score_font = pg.font.SysFont(font, size)
    # Objekt auf dem Bildschirm erstellen
    score_surface = score_font.render(f"score: {score}", True, color)
    # Rechteck für den Text erstellen
    score_ract = score_surface.get_rect()
    # Text zeichnen
    window.blit(score_surface, score_ract)

def game_over():
    # Font für Game Over erstellen
    my_font = pg.font.SysFont('times new roman', 50)
    # Getract auf dem Bildschirm erstellen
    game_over_surface = my_font.render(f"Your final score is: {score}", True, red)
    # Rechteck für den Text erstellen
    game_over_ract = game_over_surface.get_rect()
    # Position des Textes festlege
    game_over_ract.midtop = (window_x // 2, window_y // 4)
    # Text zeichnen
    window.blit(game_over_surface, game_over_ract)
    pg.display.flip()
    # 2 Sekunden warten
    time.sleep(2)
    # Pygame beenden
    pg.quit()
    # Programm beenden
    quit()

while True:

    # Keyeingaben festlegen
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                change_to_direction = "UP"
            if event.key == pg.K_DOWN:
                change_to_direction = "DOWN"
            if event.key == pg.K_LEFT:
                change_to_direction = "LEFT"
            if event.key == pg.K_RIGHT:
                change_to_direction = "RIGHT"

    # Schlange soll sich nicht in engegengesetzte Bewegungsrichtung drehen
    if change_to_direction == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to_direction == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to_direction == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to_direction == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Schlange bewegen
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    # Schlange verlängern, wenn die Schlange auf die Frucht trifft
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position [0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [rd.randrange(1, (window_x//10))*10,
                          rd.randrange(1, (window_y//10))*10]

    fruit_spawn = True
    window.fill(black)

    for pos in snake_body:
        pg.draw.rect(window, Yellow,pg.Rect(pos[0], pos[1], 10, 10))
    pg.draw.rect(window, red, pg.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    Showscore(1, green, 'times new roman', 20)

    pg.display.update()

    fps.tick(snake_speed)