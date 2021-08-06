def bar_graph(priya,value):
    priya.begin_fill()
    priya.left(90)
    priya.forward(value)
    priya.write(" "+str(value))
    priya.right(90)
    priya.forward(40)
    priya.right(90)
    priya.forward(value)
    priya.left(90)
    priya.end_fill()
    priya.forward(10)

import turtle
t = turtle.Turtle()
a = turtle.Screen()
a.bgcolor("lightgreen")
t.color("blue" , "red")
t.pensize(3)
measureheight=[37,40,50,75,100]
for i in measureheight:
    bar_graph(t,i)

