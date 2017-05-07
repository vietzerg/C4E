# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:11:30 2017

@author: PA
"""

# 7/5/2017:
# FIXED THE BUG (1) OF check_consecutive
# (1) BUG OF check_consecutive IN CASES WHERE THERE ARE MORE THAN 3 BOXES
# UPDATED A NEW MAP GENERATOR WITH ADDITIONAL ARGUMENTS
# MAP GENERATORS DO NOT GENERATE BOXES ON THE BORDERS OF THE MAP!
# ADDED VARIOUS CASES IN-GAME


import pprint
import random


def pretty_printer(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    

# GENERATE A MAP OF SIZE (mxn) WITH n_obstacle OBSTACLES
def generate_map(m,n,n_obstacle):
    mapping = []
    special_values = set()
    
    # INITIALIZE BY CREATING THE CHARACTER'S POSITION
    C_pos = (random.randrange(m), random.randrange(n))    
    special_values.add(C_pos)
    while True:
        S_pos = (random.randrange(m), random.randrange(n))
        if S_pos != C_pos:
            special_values.add(S_pos)
            break
    while True:
        B_pos = (random.randrange(m), random.randrange(n))
        if B_pos != (0,0) and B_pos != (0,n) and B_pos != (m,n) and B_pos != (m,0) and B_pos not in special_values:
            special_values.add(B_pos)
            break
    obstacle_positions_list = []
    for i in range(n_obstacle):
        while True:
            obs_pos = (random.randrange(m), random.randrange(n))
            if obs_pos not in special_values and obs_pos not in obstacle_positions_list:
                obstacle_positions_list.append(obs_pos)
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
            elif (y,x) in obstacle_positions_list:
                row.append("O")
            else:
                row.append("-")
        mapping.append(row)
    return mapping

    
# GENERATE A MAP OF SIZE (mxn) WITH ADDITIONAL ARGUMENTS FOR NUMBER OF OBSTACLES/BOXES/STORAGE POINTS   
def generate_map_v3(m,n,n_obstacle,n_box,n_storage):
    mapping = []
    
    # CREATE A DICTIONARY TO STORE SPECIAL POSITIONS
    position_dict = {}
    
    # INITIALIZE BY CREATING THE CHARACTER'S POSITION
    C_pos = (random.randrange(m), random.randrange(n))
    position_dict[C_pos] = "C"
    for i in range(n_storage):
        while True:
            S_pos = (random.randrange(m), random.randrange(n))
            if S_pos not in position_dict.keys():
                position_dict[S_pos] = "S"
                break
    for i in range(n_box):
        while True:
            B_pos = (random.randrange(m), random.randrange(n))
            if B_pos[0] != 0 and B_pos[0] != m-1 and B_pos[1] != 0 and B_pos[1] != n-1 and B_pos not in position_dict.keys():
                position_dict[B_pos] = "B"
                break
    for i in range(n_obstacle):
        while True:
            O_pos = (random.randrange(m), random.randrange(n))
            if O_pos not in position_dict.keys():
                position_dict[O_pos] = "O"
                break
            
    for y in range(m):
        row = []
        for x in range(n):
            if (y,x) in position_dict.keys():
                row.append(position_dict[(y,x)])
            else:
                row.append("-")
        mapping.append(row)
    return mapping



map1 = generate_map(6,6,3)
#pretty_printer(map2)


# RETURNS A LIST CONTAINING THE POSITIONS OF AN OBJECT ON THE MAP
def get_char_position(matrix, objectt):
    char_positions = []
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column == objectt:
                char_positions.append((row_index,column_index))
    return char_positions
            
            
def where_char_come_from(char_pos, box_position):
    if char_pos[0] == box_position[0] and box_position[1]+1 == char_pos[1]:
        return "right"
    if char_pos[0]-1 == box_position[0] and box_position[1] == char_pos[1]:
        return "down"
    if char_pos[0] == box_position[0] and box_position[1]-1 == char_pos[1]:
        return "left"
    if char_pos[0]+1 == box_position[0] and box_position[1] == char_pos[1]:
        return "up"
    

# THE CHARACTER IS ONLY STRONG ENOUGH TO PUSH 2 CONSECUTIVE BOXES AT THE SAME TIME!
def check_consecutive(box_pos):
    if len(box_pos) < 3:
        return False
    else:
        row_coord_dict = {}
        col_coord_dict = {}
        for box_position in box_pos:
            if box_position[0] in row_coord_dict.keys():
                row_coord_dict[box_position[0]].append(box_position[1])
            else:
                row_coord_dict[box_position[0]] = [box_position[1]]
            if box_position[1] in col_coord_dict.keys():
                col_coord_dict[box_position[1]].append(box_position[0])
            else:
                col_coord_dict[box_position[1]] = [box_position[0]]
        
        #print (row_coord_dict)
        #print (col_coord_dict)        

        for col_ind_list in row_coord_dict.values():
            if len(col_ind_list) >= 3:
                for i, col_index in enumerate(sorted(col_ind_list)):
                    if col_index + 1 == sorted(col_ind_list)[i+1] and col_index + 2 == sorted(col_ind_list)[i+2]:
                        return True
                        break
                    
        for row_ind_list in col_coord_dict.values():
            if len(row_ind_list) >= 3:
                for i, row_index in enumerate(sorted(row_ind_list)):
                    if row_index + 1 == sorted(row_ind_list)[i+1] and row_index + 2 == sorted(row_ind_list)[i+2]:
                        return True
                        break
        return False

# HERE I TEST THE WORKINGS OF THE check_consecutive FUNCTION 
#test_map2 = [["-","-","-","O","-","-"],
#            ["-","B","-","B","C","-"],
#            ["-","B","-","-","-","-"],
#            ["-","B","-","-","-","-"],
#            ["-","-","-","B","-","-"]]
#print(check_consecutive(get_char_position(test_map2,"B")))


def testing_input(matrix):
    pretty_printer(matrix)
    
    # FIRST INITIALIZATION
    char_pos = get_char_position(matrix,"C")[0]
    box_pos = get_char_position(matrix,"B")
    storage_pos = get_char_position(matrix,"S")
    obstacle_pos = get_char_position(matrix,"O")
    
    while True:          
        
        user_input = input("Move? ")
        if user_input not in ["w","a","s","d","x"]:
            print ("You can only choose w,a,s,d to move or x to exit game!")
        else:
            if user_input == "d":
                new_char_pos = (char_pos[0],char_pos[1]+1)
            elif user_input == "s":
                new_char_pos = (char_pos[0]+1,char_pos[1])
            elif user_input == "a":
                new_char_pos = (char_pos[0],char_pos[1]-1)
            elif user_input == "w":
                new_char_pos = (char_pos[0]-1,char_pos[1])
            elif user_input == "x":
                break
                
                
            
            # IN CASE THE CHAR TRIES TO PUSH A BOX  
            if new_char_pos in box_pos:
                if where_char_come_from(char_pos, new_char_pos) == "up":
                    new_box_pos = (new_char_pos[0]+1,new_char_pos[1])
                elif where_char_come_from(char_pos, new_char_pos) == "down":
                    new_box_pos = (new_char_pos[0]-1,new_char_pos[1])
                elif where_char_come_from(char_pos, new_char_pos) == "left":
                    new_box_pos = (new_char_pos[0],new_char_pos[1]+1)
                elif where_char_come_from(char_pos, new_char_pos) == "right":
                    new_box_pos = (new_char_pos[0],new_char_pos[1]-1)
                    
                # IN CASE THE NEW BOX POSITION IS OUTSIDE OF THE BORDER AND BESIDE AN OBSTACLE
                if new_box_pos[0] >= len(matrix) or new_box_pos[0] < 0 or new_box_pos[1] >= len(matrix) or new_box_pos[1] < 0 or new_box_pos in obstacle_pos:
                    print ("Can't move this box!")
                    new_char_pos = char_pos
                
                # IN CASE HE PUSHES THE BOX INTO THE STORAGE POINT
                elif new_box_pos in storage_pos:
                    matrix[new_box_pos[0]][new_box_pos[1]] = "S"
                else:
                    matrix[new_box_pos[0]][new_box_pos[1]] = "B"
                    
                # IN CASE THE CHARACTER TRIES TO MOVE 2 CONSECUTIVE BOXES AT THE SAME TIME
                if new_box_pos in box_pos:
                    if where_char_come_from(new_char_pos, new_box_pos) == "up":
                        new_box_pos2 = (new_box_pos[0]+1,new_box_pos[1])
                    elif where_char_come_from(new_char_pos, new_box_pos) == "down":
                        new_box_pos2 = (new_box_pos[0]-1,new_box_pos[1])
                    elif where_char_come_from(new_char_pos, new_box_pos) == "left":
                        new_box_pos2 = (new_box_pos[0],new_box_pos[1]+1)
                    elif where_char_come_from(new_char_pos, new_box_pos) == "right":
                        new_box_pos2 = (new_box_pos[0],new_box_pos[1]-1)
                    
                    # IN CASE THE NEW BOX2 POSITION IS OUTSIDE OF THE BORDER AND BESIDE AN OBSTACLE
                    if new_box_pos2[0] >= len(matrix) or new_box_pos2[0] < 0 or new_box_pos2[1] >= len(matrix) or new_box_pos2[1] < 0 or new_box_pos2 in obstacle_pos:
                        print ("Can't move these boxes!")
                        new_char_pos = char_pos
                    
                    # IN CASE HE PUSHES THE NEW BOX2 INTO THE STORAGE POINT:
                    elif new_box_pos2 in storage_pos:
                        matrix[new_box_pos2[0]][new_box_pos2[1]] = "S"
                    else:
                        matrix[new_box_pos[0]][new_box_pos[1]] = "B"
                        matrix[new_box_pos2[0]][new_box_pos2[1]] = "B"
                
                    # IN CASE THE CHARACTER TRIES TO MOVE 3 CONSECUTIVE BOXES AT THE SAME TIME
                    if check_consecutive(box_pos) == True:
                        print ("You are not strong enough to push these boxes!")
                        new_char_pos = char_pos
                    
            
            # IN CASE CHAR MOVES ACROSS THE STORAGE POINT
            if char_pos in storage_pos:
                matrix[char_pos[0]][char_pos[1]] = "S"
            else:
                matrix[char_pos[0]][char_pos[1]] = "-"
                
            # IN CASE CHAR TRIES TO MOVE ACROSS AN OBSTACLE
            if new_char_pos in obstacle_pos:
                new_char_pos = char_pos
                
            
            # TRY TO MOVE THE CHARACTER, JUST IN CASE HE MOVES TO THE BORDER
            if new_char_pos[0] >= len(matrix) or new_char_pos[0] < 0 or new_char_pos[1] >= len(matrix[0]) or new_char_pos[1] < 0:
                print ("You can't move outside of the map!")
                new_char_pos = char_pos
                
                
            # FINALLY, AFTER ALL THE CASES, LET'S UPDATE THE NEW POSITION OF THE CHAR  
            matrix[new_char_pos[0]][new_char_pos[1]] = "C"
            
            
            # UPDATE THE POSITIONS AND REPEAT THE LOOP
            char_pos = get_char_position(matrix,"C")[0]
            box_pos = get_char_position(matrix,"B")   
            pretty_printer(matrix)
            
            
            # WINNING ANNOUCEMENT
            if box_pos == []:
                print ("YOU WIN!")
                break

# TESTING AREA
test_map = [["-","-","-","O","-","-"],
            ["-","B","B","B","C","-"],
            ["-","S","-","-","-","-"]]

map2 = generate_map_v3(10,10,3,4,3)
testing_input(map2)
