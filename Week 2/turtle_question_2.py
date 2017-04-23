from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(4,-1,-1):
    color(colors[i],colors[i])
    begin_fill()
    for n in range(2):
        forward(50*(i+1))
        right(90)
        forward(100)
        right(90)
    end_fill()
