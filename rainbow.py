from turtle import *

t = Turtle()
t.speed(9)
t.pensize(20)

t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.pencolor("red")
t.circle(100,180)

t.penup()
t.goto(80,0)
t.pendown()
t.left(180)
t.pencolor("orange")
t.circle(80,180)

t.penup()
t.goto(60,0)
t.pendown()
t.left(180)
t.pencolor("yellow")
t.circle(60,180)

t.penup()
t.goto(40,0)
t.pendown()
t.left(180)
t.pencolor("green")
t.circle(40,180)

t.penup()
t.goto(20,0)
t.pendown()
t.left(180)
t.pencolor("blue")
t.circle(20,180)

done()