from turtle import *
from time import sleep

bgcolor('black')

setpos(-150.00, 107.00)
pos()

pencolor('red')
pensize(10)
penup()
pendown()

for i in range(5):
    forward(300)
    right(144)

penup()
goto(0.00, -106.00)
pendown()
r = 160
circle(r)

for i in range(6):
    print('You are now possessed by our Loard Satan!!!')
    sleep(1)

mainloop()
