import tkinter as tk
import math
import random
import numpy as np
from ball import Ball

def create_window(size):
    size_string = str(size+100) + 'x' + str(size+100)
    window = tk.Tk()
    window.title('Bouncing ball game by Ture')
    window.geometry(size_string)
    window.config(bg='#345')

    return window


def create_canvas(window, size):
    canvas = tk.Canvas(
        window,
        height=size,
        width=size,
        bg="#fff"
    )
    canvas.pack()
    return canvas

def create_balls(size, nr_balls, canvas):
    balls_per_row = int(math.sqrt(nr_balls))
    step = size / (balls_per_row +1)

    balls = []

    for i in range(balls_per_row):
        for j in range(balls_per_row):
            if i % 3 == 0:
                color = 'Red'
            elif i % 3 == 1:
                color = 'Blue'
            else:
                color = 'Green'

            balls.append(
                Ball(pos=np.array([(i + 1) * step, (j + 1) * step]),
                     vel=np.array([random.uniform(-1, 1), random.uniform(-1, 1)]),
                     rad=10,
                     canvas=canvas,
                     type=color))
    return balls

def create_user_ball(size, canvas):
    i = random.randint(1, 3)
    if i % 3 == 0:
        color = 'Red'
    elif i % 3 == 1:
        color = 'Blue'
    else:
        color = 'Green'


    ball = Ball(pos=np.array([size/2, 30]),
                     vel=np.array([0, 1]),
                     rad=15,
                     canvas=canvas,
                     type=color,
                outline='Yellow',
                dash=3,
                remove_others=True)
    return ball

# Används ej än?
def move_balls(balls, canvas):
    for ball in balls:
        ball.move()
        # print(canvas.coords(ball.ball_obj))
        for other_ball in balls:
            if not ball == other_ball:
                ball.check_collision_ball(other_ball)
        ball.check_collision_wall(size)
    canvas.update()
    canvas.after(10, move_balls(balls,canvas))

# Event-metoder för att ändra hastigheten
def speed_down(event, user_ball):
    user_ball.vel += [0, 1]
    return

def speed_up(event, user_ball):
    user_ball.vel += [0, -1]
    return

def speed_right(event, user_ball):
    user_ball.vel += [1, 0]
    return

def speed_left(event, user_ball):
    user_ball.vel += [-1, 0]
    return

def remove_ball(ball_list, canvas):
    if len(ball_list) != 0:
        ball = ball_list.pop(0).ball_obj
        canvas.delete(ball)
    return

def move(balls, canvas, size, tic_rate):
    for ball in balls:
        ball.move()
        # print(canvas.coords(ball.ball_obj))
        for other_ball in balls:
            if not ball == other_ball:
                ball.check_collision_ball(other_ball)
        ball.check_collision_wall(size)
    canvas.after(tic_rate, lambda: move(balls, canvas, size, tic_rate))




