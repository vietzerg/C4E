# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:55:00 2017

@author: PA
"""
size = {
        'height' : 5,
        'width' : 4
        }

c = {
    'x' : 2,
    'y' : 1
    }

b = {
    'x' : 1,
    'y' : 3
    }

s = {
    'x' : 1,
    'y' : 1
    }

def display_map(size, c, b, s):
    for y in range(size['height']):
        for x in range(size['width']):
            if x == c['x'] and y == c['y']:
                print('C ', end ='')
            elif x == b['x'] and y == b['y']:
                print('B ', end = '')              
            elif x == s['x'] and y == s['y']:
                print('S ', end = '')
            else:
                print('- ', end ='')
        print()
    
def in_map(size, point):
    return point["x"] >= 0 and point["x"] < size["width"] and point["y"] >= 0 and point["y"] < size["height"]

def same_point(point1, point2):
    return point1["x"] == point2["x"] and point1["y"] == point2["y"]

def move_point(point, dx, dy):
    return {
            "x": point["x"] + dx,
            "y": point["y"] + dy}
        

loop = True

while(loop):
    
    #graphics
    display_map(size,c,b,s)
    
    #logic (gameplay)
    move = input("Your move? ").upper()
    
    dx = 0
    dy = 0
    
    if move == "D":
        dx=1
    elif move == "A":
        dx=-1
    elif move == "W":
        dy=-1
    elif move == "S":
        dy=1
    elif move == "X":
        break
    
    c_next = move_point(c, dx, dy)
#    c_next["x"] = c["x"] + dx
#    c_next["y"] = c["y"] + dy
    
    if in_map(size, c_next):
        if same_point(c_next, b):
            # BOX FRONT, TRY TO PUSH IT
            b_next = move_point(b, dx, dy)
            if in_map(size, b_next):
                b = b_next
                c = c_next
        else:
            # NO BOXES AHEAD
            c = c_next