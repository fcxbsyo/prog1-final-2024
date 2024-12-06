import turtle
from ball import Ball
import random
import seven_segments_proc
import heapq


class RunBall:
    def __init__(self, num_ball):
        self.num_ball = num_ball
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        print(self.canvas_width, self.canvas_height)

        tom = turtle.Turtle()
        self.my_seven_segments = seven_segments_proc.SevenSegments(tom, (255, 0, 0))

        self.screen = turtle.Screen()

# create random number of balls, num_balls, located at random positions within the canvas; each ball has a random
# velocity value in the x and y direction and is painted with a random color

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)
        # move_left and move_right handlers update paddle positions

    def __run(self):
        for i in range(self.num_ball):
            self.xpos.append(random.uniform(-1 * self.canvas_width + self.ball_radius,
                                            self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1 * self.canvas_height + self.ball_radius,
                                            self.canvas_height - self.ball_radius))
            self.vx.append(10 * random.uniform(-1.0, 1.0))
            self.vy.append(10 * random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step
        while (True):
            turtle.clear()
            self.draw_border()
            ball = Ball
            for i in range(self.num_ball):
                ball.draw_ball(self.ball_color[i], self.ball_radius, self.xpos[i], self.ypos[i])
                ball.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, dt)
                ball.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width,
                                          self.canvas_height, self.ball_radius)
            turtle.update()

    turtle.done()
