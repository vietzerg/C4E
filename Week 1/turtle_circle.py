from turtle import *

pencolor("green")
speed(60)

n = int(input("Number of circles? "))
for i in range(0,n):
    circle(100)
    left(360/n)
