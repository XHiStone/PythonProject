from time import sleep
from turtle import Turtle, done
from turtle import mainloop



t = Turtle()
t.shape('turtle')
# t.speed(0)
t.color('red')

# screen = t.getscreen()
# screen.tracer(1)

num = 360 // 15
print(f'num = {num}')
for i in range(num):
    t.setheading(i * 15)
    t.forward(100)
    t.stamp()
    t.home()

# screen.update()
done()
