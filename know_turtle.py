from time import sleep
from turtle import Turtle
from turtle import mainloop


t = Turtle()
t.shape('turtle')
t.color('red')

# print(t.screen.getshapes())
# # sleep(1)
# t.hideturtle()

t.setheading(0)
t.forward(100)
t.stamp()
t.home()

t.setheading(15)
t.forward(100)
t.stamp()
t.home()

mainloop()
