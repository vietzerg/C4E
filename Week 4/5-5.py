# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:11:30 2017

@author: PA
"""

# 6/5/2017 BUGS:
# BUG WHEN TRYING TO MOVE CHARACTER TO THE SIDES OF THE MAP (THE SAME BEHAVIOR AS THE PREVIOUS BOX-SIDES BUG)
# BUG WHEN MOVING THE CHARACTER ACROSS THE S POINT, AFTER WHICH THE S POINT BECOMES "-"


import pprint
import random
import itertools

#matrix = [[0,1,2,3],
#          [4,5,6,7],
#          [8,9,10,11],
#          [12,13,14,15]]

#mapping = [["-","-","-","-"],
#           ["-","C","-","-"],
#           ["-","-","B","-"],
#           ["-","S","-","-"]]

def pretty_printer(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

def generate_map(m,n):
    mapping = []
    C_pos = (random.randrange(m), random.randrange(n))
    while True:
        S_pos = (random.randrange(m), random.randrange(n))
        if S_pos != C_pos:
            break
    while True:
        B_pos = (random.randrange(m), random.randrange(n))
        if B_pos != (0,0) and B_pos != (0,n) and B_pos != (m,n) and B_pos != (m,0) and B_pos != C_pos and B_pos != S_pos:
            break
    for y in range(m):
        row = []
        for x in range(n):
            if (y,x) == C_pos:
                row.append("C")
            elif (y,x) == S_pos:
                row.append("S")
            elif (y,x) == B_pos:
                row.append("B")
            else:
                row.append("-")
        mapping.append(row)
    return mapping
    #C_pos, S_pos, B_pos


map1 = generate_map(6,6)


def get_char_position(matrix, key):
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column == key:
                return (row_index,column_index)
            
#def get_box_position(matrix):
#    for row_index, row in enumerate(matrix):
#        for column_index, column in enumerate(row):
#            if column == "B":
#                return (row_index,column_index)
            
def where_char_come_from(char_pos, box_pos):
    if char_pos[0] == box_pos[0] and box_pos[1]+1 == char_pos[1]:
        return "right"
    if char_pos[0]-1 == box_pos[0] and box_pos[1] == char_pos[1]:
        return "down"
    if char_pos[0] == box_pos[0] and box_pos[1]-1 == char_pos[1]:
        return "left"
    if char_pos[0]+1 == box_pos[0] and box_pos[1] == char_pos[1]:
        return "up"
            
#print (get_char_position(mapping))
#print (get_box_position(mapping))
#user_input

def testing_input(matrix):
    pretty_printer(matrix)
    char_pos = get_char_position(matrix,"C")
    box_pos = get_char_position(matrix,"B")
    storage_pos = get_char_position(matrix,"S")
    
    while True:
        user_input = input("Move? ")
        if user_input == "d":
            new_char_pos = (char_pos[0],char_pos[1]+1)
        if user_input == "s":
            new_char_pos = (char_pos[0]+1,char_pos[1])
        if user_input == "a":
            new_char_pos = (char_pos[0],char_pos[1]-1)
        if user_input == "w":
            new_char_pos = (char_pos[0]-1,char_pos[1])
            
        
        # IN CASE THE NEW CHAR POSITION IS EQUAL TO THE BOX POSITION
        # 5/5/2017: I'M TRYING TO FIX THE BUG. PUSHING THE BOX TO THE LEFTMOST MAKES THE BOX APPEAR ON THE RIGHTMOST SIDE!
        if new_char_pos == box_pos:
            if where_char_come_from(char_pos, box_pos) == "up":
                new_box_pos = (box_pos[0]+1,box_pos[1])
            elif where_char_come_from(char_pos, box_pos) == "down":
                new_box_pos = (box_pos[0]-1,box_pos[1])
            elif where_char_come_from(char_pos, box_pos) == "left":
                new_box_pos = (box_pos[0],box_pos[1]+1)
            elif where_char_come_from(char_pos, box_pos) == "right":
                new_box_pos = (box_pos[0],box_pos[1]-1)
            if new_box_pos[0] >= len(matrix) or new_box_pos[0] < 0 or new_box_pos[1] >= len(matrix) or new_box_pos[1] < 0:
                print ("Can't move this box!")
                new_char_pos = char_pos
            else:
                matrix[new_box_pos[0]][new_box_pos[1]] = "B"
        
        
        # TRY TO MOVE THE CHARACTER, JUST IN CASE HE MOVES TO THE BORDER        
        try:
            matrix[char_pos[0]][char_pos[1]] = "-"                       #replacing the old char position with "-"
            matrix[new_char_pos[0]][new_char_pos[1]] = "C"
        except Exception:
            new_char_pos = char_pos
          
        #matrix[new_char_pos[0]][new_char_pos[1]] = "C"
        
        # UPDATE THE POSITIONS AND REPEAT THE LOOP
        char_pos = get_char_position(matrix, "C")
        box_pos = get_char_position(matrix, "B")
        pretty_printer(matrix)
        
        
        #WINNING ANNOUCEMENT
        if box_pos == storage_pos:
            print ("YOU WIN!")
            break
    #return matrix

testing_input(map1)

#pretty_printer(generate_map(5,4))