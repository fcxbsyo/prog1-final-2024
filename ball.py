import turtle
import math


class Ball:

    def __init__(self, color, size, x, y, vx, vy, i):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.i = i
        self.count = 0
        self.mass = 100 * size ** 2
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.r = 0.05 * self.canvas_width

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self, dt):
        self.x[self.i] += self.vx[self.i] * dt
        self.y[self.i] += self.vy[self.i] * dt

    def update_ball_velocity(self):
        if abs(self.x[self.i]) > (self.canvas_width - self.r):
            self.vx[self.i] = -self.vx[self.i]

        if abs(self.y[self.i]) > (self.canvas_height - self.r):
            self.vy[self.i] = -self.vy[self.i]

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx
        self.count += 1

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy
        self.count += 1

    def bounce_off(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx * dvx + dy * dvy
        dist = self.size + that.size

        magnitude = 2 * self.mass * that.mass * dvdr / ((self.mass + that.mass) * dist)
        fx = magnitude * dx / dist
        fy = magnitude * dy / dist
        that.vy -= fy / that.mass
        self.count += 1
        that.count += 1

    def distance(self, that):
        x1 = self.x
        y1 = self.y
        x2 = that.x
        y2 = that.y
        d = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return d
