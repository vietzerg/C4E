from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(10)
                
for i in range(3,8):
    color(colors[i-3])
    for ind in range(i):
        forward(100)
        left(360/i)
