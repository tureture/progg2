import tkinter as tk
import math
import random
import numpy as np
from ball import Ball


class Canvas:

    def __init__(self, window, size):
        self.window = window
        self.canvas_obj = self.create_canvas(window, size)
        self.balls = []
        self.size = size
        self.delete_button = None
        self.user_ball = None

    def start(self, entry_speed, entry_balls):
        '''
        Skapar bollar, en delete_ball knapp, keybindings och startar spelet
        :param entry_speed: tkinter entry knapp för snabbheten
        :param entry_balls: tkinter entry knapp för antalet bollar
        :return: None
        '''

        self.canvas_obj.delete('all')  # Rensar tidigare canvas (behövs för omstart

        # Skapar bollar
        nr_balls = int(float(entry_balls.get()))  # rounds to int
        self.create_balls(nr_balls)
        self.create_user_ball()

        # Startar spelet med tic_rate
        tic_rate = self.set_tic_rate(entry_speed)
        self.move(tic_rate)

        # Keybindings för att styra user_ball
        self.window.bind('<KeyPress-Right>', lambda event, arg=self.user_ball: speed_right(event, arg))
        self.window.bind('<KeyPress-Down>', lambda event, arg=self.user_ball: speed_down(event, arg))
        self.window.bind('<KeyPress-Up>', lambda event, arg=self.user_ball: speed_up(event, arg))
        self.window.bind('<KeyPress-Left>', lambda event, arg=self.user_ball: speed_left(event, arg))

        # Skapar delete_ball knapp
        if self.delete_button is not None:  # Undviker kopior av samma knapp
            self.delete_button.destroy()
        self.delete_button = tk.Button(self.window, text='Delete ball', name='delete_ball', command=self.remove_ball)
        self.delete_button.pack()

    def create_balls(self, nr_balls):
        '''
        Skapar lista av Ball objekt
        :param nr_balls: Antalet bollar
        :return: None
        '''
        balls_per_row = int(math.ceil(math.sqrt(nr_balls)))
        step = self.size / (balls_per_row + 1)

        if len(self.balls) != 0:
            self.balls = []

        counter = 0
        for i in range(balls_per_row):
            for j in range(balls_per_row):

                if counter < nr_balls: # Quickfix för att inte placera ut för många bollar
                    counter += 1
                else:
                    break

                if i % 3 == 0:
                    color = 'Red'
                elif i % 3 == 1:
                    color = 'Blue'
                else:
                    color = 'Green'

                self.balls.append(
                    Ball(pos=np.array([(i + 1) * step, (j + 1) * step]),
                         vel=np.array([random.uniform(-1, 1), random.uniform(-1, 1)]),
                         rad=10,
                         canvas=self.canvas_obj,
                         type=color))

    def create_user_ball(self):
        '''
        Skapar större boll som styrs av användaren
        :return:
        '''
        i = random.randint(1, 3)
        if i % 3 == 0:
            color = 'Red'
        elif i % 3 == 1:
            color = 'Blue'
        else:
            color = 'Green'

        ball = Ball(pos=np.array([self.size / 2, 30]),
                    vel=np.array([0, 1]),
                    rad=15,
                    canvas=self.canvas_obj,
                    type=color,
                    outline='Yellow',
                    dash=3)
        self.balls.append(ball)
        self.user_ball = ball

    def remove_ball(self):
        if len(self.balls) != 0:
            ball = self.balls.pop(0).ball_obj
            self.canvas_obj.delete(ball)
        return

    def move(self, tic_rate):
        '''
        Uppdaterar position för alla bollar, kollar kollisioner, uppdaterar hastighet
        :param tic_rate: Hastigheten för spelet
        :return:
        '''
        for ball in self.balls:
            ball.move()
            for other_ball in self.balls:
                if not ball == other_ball:
                    ball.check_collision_ball(other_ball)
            ball.check_collision_wall(self.size)
        self.canvas_obj.after(tic_rate, lambda: self.move(tic_rate))

    def create_canvas(self, window, size):
        '''
        Create canvas
        :param window: root tkinter window
        :param size: size in pixels
        :return: tkinter canvas object
        '''
        canvas = tk.Canvas(
            window,
            height=size,
            width=size,
            bg="#fff"
        )
        canvas.pack()
        return canvas

    def set_tic_rate(self, entry_speed):
        '''
        Set tic rate to range 1-10 from speed
        :param entry_speed: tkinter entry object
        :return: tic_rate
        '''
        speed_string = entry_speed.get()
        speed = int(float(speed_string))  # Rounds to integer

        # Sets speed between 1-10
        if speed < 1:
            tic_rate = 10
        elif speed > 9:
            tic_rate = 1
        else:
            tic_rate = 10 - speed

        return tic_rate


def create_window(size):
    size_string = str(size + 100) + 'x' + str(size + 200)
    window = tk.Tk()
    window.title('Bouncing ball game by Ture')
    window.geometry(size_string)
    window.config(bg='#345')

    return window


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

