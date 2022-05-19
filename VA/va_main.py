import tkinter as tk
import numpy as np
from ball import Ball
from canvas_stuff import *
import random

'''
Voluntary Assignment Progg2
Av Ture Hassler, Maj 13 2022
'''


size = 400  # Storlek på fönstret

# Skapar window och canvas (utökat canvas object)
window = create_window(size)
canvas = Canvas(window, size)

# Skapar knappar
button_start = tk.Button(window, text='Start', command=lambda: canvas.start(entry_speed=entry_speed, entry_balls=entry_balls))
button_start.pack()

button_quit = tk.Button(window, text='Quit', command=window.destroy)
button_quit.pack()

# Skapar input-rutor
string_var = tk.StringVar(window, '2')
entry_speed = tk.Entry(window, textvariable=string_var, width=40)
frame_speed = tk.Label(window, text='Game speed (between 1-10)', width=40)


string_var_2 = tk.StringVar(window, '9')
entry_balls = tk.Entry(window, textvariable=string_var_2, width=40)
frame_balls = tk.Label(window, text='Nr Balls', width=40)

frame_speed.pack()
entry_speed.pack()
frame_balls.pack()
entry_balls.pack()

# Mainloop
window.mainloop()
