'''
import turtle
t = turtle.Turtle()
turtle.title("Heart Shape")
screen = turtle.Screen()
screen.bgcolor("black")
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90,200)
t.left(120)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.hideturtle()
'''

import turtle
priya = turtle.Turtle()
turtle.title("spiral")
screen = turtle.Screen()
screen.bgcolor("black")
list = ["blue"]
for i in range(200):
    priya.color(list)
    priya.width(2)
    priya.forward(i)
    priya.left(59)
    priya.speed(200)

