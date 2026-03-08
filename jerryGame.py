from turtle import *
from gamebase import line
from random import randrange, choice
from time import time

balloons = []
explosions = []

colors = ['red', 'blue', 'yellow','light green', 'purple', 'violet', 'light blue', 'orange', 'dark green','pink']
size = 50

score = 0
lives = 5
game_time = 60
start_time = time()

def distance(x, y, a, b):
    return ((x - a) ** 2+ (y - b) ** 2) ** 0.5

def click(x, y):
    global score
    for n in range(len(balloons)-1, -1, -1):
        if distance(x, y, balloons[n][0], balloons[n][1]) < size / 2:
            score += 10
            explosions.append([balloons[n][0], balloons[n][1],10])
            balloons.pop(n)
            draw() 
            return

def spawn_balloon():
    x = randrange(-200 + size, 200 - size)
    c = choice(colors)
    speed = randrange(1, 5)
    balloons.append([x, -200 - size, c, speed])

def draw_balloons():
    global lives
    for n in range(len(balloons) - 1, -1, -1):
        x, y, c, v = balloons[n]
        line(x, y, x, y - size, 1, 'black')
        up()
        goto(x, y)
        dot(size, c)
        balloons[n][1] += v
        if balloons[n][1] > 210:
            balloons.pop(n)
            lives -= 1

def draw_ui():
    up()
    goto(-200, 180)
    color('black')
    write(f"Score: {score}", font=('Arial', 14, 'normal'))
    up()
    goto(80, 180)
    write(f"Lives: {lives}", font=('Arial', 14, 'normal'))

    remaining = int(game_time - (time() - start_time))
    up()
    goto(-40, 180)
    write(f"Time: {remaining}", font=('Arial', 14, 'normal'))

def draw_explosion():
    for n in range(len(explosions)-1,-1,-1):
        x, y, r = explosions[n]
        up()
        goto(x, y)
        dot(r, 'yellow')
        dot(r*0.6, 'orange')
        dot(r*0.3, 'red')
        explosions[n][2] += 5
        
        if explosions[n][2] > 60:
            explosions.pop(n)

def draw():
    clear()
    draw_balloons()
    draw_explosion()
    draw_ui()
    update()
    
def game_over(text):
    clear()
    up()
    goto(0, 20)
    write(text, align="center", font=('Arial', 30, 'bold'))
    goto(0, -20)
    write(f"Final Score: {score}", align="center", font=('Arial', 30, 'bold'))
    update()

def gameLoop():
    if lives <= 0:
        game_over("Game Over")
        return
    
    if game_time - (time() - start_time) < 0:
        game_over("Time Up")
        return
    
    if randrange(0, 40) == 1:
        spawn_balloon()
    draw()
    ontimer(gameLoop, 15)

setup(420, 420, 0, 0)
hideturtle()
tracer(0)
listen()
onscreenclick(click)
gameLoop()
done()