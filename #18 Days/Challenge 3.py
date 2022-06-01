'''
I am
import turtle as t
tim = Turtle()
contador = 3

while contador < 10:
   rotation = 360 / contador
   for _ in range(contador):
       tim.forward(100)
       tim.right(rotation)
   contador += 1
'''
'''
Exemplo
import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
'''

