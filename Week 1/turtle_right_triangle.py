from turtle import *

color("green","yellow")
a = int(input("Length of the adjacent side? "))
b = int(input("Length of the opposite side? "))

begin_fill()
forward(a)
left(90)
forward(b)
goto(0,0)
right(90)
end_fill()
