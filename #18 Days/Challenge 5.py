import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


t.speed("fastest")


def draw_spirograph(size_of_gab):
    for _ in range(int(360 / size_of_gab)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gab)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()