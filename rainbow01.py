from turtle import *

colors = ["red", "orange", "yellow", "green", "blue", "indigo","purple"]
t = Turtle()
t.shape("turtle")
t.speed(10)
t.pensize(20)

for i in range(7):
    t.penup()
    t.goto(140-i * 20, 0)
    t.pendown()
    t.setheading(90)
    t.pencolor(colors[i])
    t.circle(140-i * 20, 180)

t.penup()
t.home()
t.setheading(90)

done()