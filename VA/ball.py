import math
import numpy as np


class Ball:
    def __init__(self, pos, vel, rad, canvas, type, outline='#000', dash=1):

        self.vel = np.array(vel, dtype=np.float)
        self.canvas = canvas
        self.rad = rad
        self.type = type
        self.ball_obj = canvas.create_oval(pos[0] - rad,
                                           pos[1] - rad,
                                           pos[0] + rad,
                                           pos[1] + rad,
                                           outline=outline,
                                           fill=type,
                                           dash=dash)
        coords = canvas.coords(self.ball_obj)
        self.center = np.array([coords[0] + self.rad, coords[1] + self.rad])

    def check_collision_ball(self, other_ball):
        diff = other_ball.center - self.center
        dist = np.linalg.norm(diff)
        if dist < self.rad + other_ball.rad:
            self.bounce(other_ball, diff)
            self._check_color(other_ball)
            return True
        else:
            return False

    def _check_color(self, other_ball):
        # Change color if different types, for simple color based rock paper scissor
        if self.type != other_ball.type:
            if self.type == 'Green':  # Case if green
                if other_ball.type == 'Blue':  # Green beats blue
                    other_ball.type = self.type
                else:
                    self.type = other_ball.type  # Red beats green
            elif self.type == 'Blue':  # Case if blue
                if other_ball.type == 'Red':  # Blue beats red
                    other_ball.type = self.type
                else:
                    self.type = other_ball.type  # Green beats blue
            else:  # Case if red
                if other_ball.type == 'Green':  # Red beats green
                    other_ball.type = self.type
                else:
                    self.type = other_ball.type  # Blue beats red
            self._set_color()
            other_ball._set_color()

    def _set_color(self):
        self.canvas.itemconfig(self.ball_obj, fill=self.type)



    def check_collision_wall(self, size):
        coord = self.canvas.coords(self.ball_obj)
        # Kollar x koordinaterna
        if coord[0] - self.rad < 0:
            self.vel[0] = -1 * self.vel[0]
        elif coord[0] + self.rad > size:
            self.vel[0] = -1 * self.vel[0]

        # Kollar y koordinaterna
        if coord[1] - self.rad < 0:
            self.vel[1] = -1 * self.vel[1]
        elif coord[1] + self.rad > size:
            self.vel[1] = -1 * self.vel[1]

    def bounce(self, other_ball, diff):
        dot_prod = (other_ball.vel - self.vel) @ diff
        scaling = dot_prod / np.linalg.norm(diff) ** 2
        added_vel = scaling * diff
        self.vel += added_vel
        other_ball.vel += added_vel * -1
        return

    def move(self):
        self.canvas.move(self.ball_obj, self.vel[0], self.vel[1])  # Move
        coords = self.canvas.coords(self.ball_obj)
        self.center = np.array([coords[0] + self.rad, coords[1] + self.rad])  # Update center

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


