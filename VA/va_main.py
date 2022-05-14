import tkinter as tk
import numpy as np
from ball import Ball
from canvas_stuff import *
import random

'''
Voluntary Assignment Progg2
Av Ture Hassler, Maj 13 2022
'''

size = 400
nr_balls = 16
tic_rate = 5

window = create_window(size)
canvas = create_canvas(window, size)
balls = create_balls(size, nr_balls, canvas)
user_ball = create_user_ball(size, canvas)
balls.append(user_ball)

button = tk.Button(window, text='Delete ball', command=lambda: remove_ball(balls, canvas))
button.pack()

button2 = tk.Button(window, text='Start', command=lambda: remove_ball(balls, canvas))
button2.pack()

button3 = tk.Button(window, text='Stop', command=lambda: remove_ball(balls, canvas))
button3.pack()

#fixa textruta, oklart om funkar
entry1 = tk.Entry(window)
entry1.pack()







window.bind('<KeyPress-Right>', lambda event, arg=user_ball: speed_right(event, arg))
window.bind('<KeyPress-Down>', lambda event, arg=user_ball: speed_down(event, arg))
window.bind('<KeyPress-Up>', lambda event, arg=user_ball: speed_up(event, arg))
window.bind('<KeyPress-Left>', lambda event, arg=user_ball: speed_left(event, arg))
canvas.after(1, lambda: move(balls, canvas, size, tic_rate))


window.mainloop()
