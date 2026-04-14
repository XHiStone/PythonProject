# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes:
import turtle
from turtle import *
from shapes import *


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle named Tommy:to
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(7)

# Draw three circles:
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", font=("Arial", 16, "bold"))
tommy.goto(0,-80)

turtle.done()
# Try changing draw_circle to draw_square, draw_triangle, or draw_star