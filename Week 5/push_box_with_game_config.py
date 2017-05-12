# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:03:46 2017

@author: PA
"""

import random
from itertools import groupby
from operator import itemgetter
import csv


def pretty_printer(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    

def get_char_position(matrix, objectt):
    char_positions = []
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column == objectt:
                char_positions.append((row_index,column_index))
    return char_positions


def generate_powerups(matrix, excluded_positions_list):
    while True:
        powerup_pos = random.randrange(len(matrix)), random.randrange(len(matrix[0]))
        if powerup_pos not in excluded_positions_list:
            return powerup_pos
        
        
def where_char_come_from(char_pos, box_position):
    if char_pos[0] == box_position[0] and box_position[1]+1 == char_pos[1]:
        return "right"
    if char_pos[0]-1 == box_position[0] and box_position[1] == char_pos[1]:
        return "down"
    if char_pos[0] == box_position[0] and box_position[1]-1 == char_pos[1]:
        return "left"
    if char_pos[0]+1 == box_position[0] and box_position[1] == char_pos[1]:
        return "up"


# GET SERIES OF AT LEAST 3 CONSECUTIVE NUMBERS IN A LIST
def get_consecutive(num_list):
    big_result = []
    for k, g in groupby(enumerate(num_list), lambda ix : ix[0] - ix[1]):
        conse_list = list(map(itemgetter(1), g))
        if len(conse_list) >= 3:
            big_result.append(conse_list)
    return big_result


# THE CHARACTER IS ONLY STRONG ENOUGH TO PUSH 2 CONSECUTIVE BOXES AT THE SAME TIME!
def check_consecutive(box_pos):
    if len(box_pos) < 3:
        return ()
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
        
        real_row_consecutive = {}
        real_col_consecutive = {}        

        for row, col_ind_list in row_coord_dict.items():
            if len(col_ind_list) >= 3:
                consecutive_list = get_consecutive(col_ind_list)
                if consecutive_list != []:
                    real_row_consecutive[row] = consecutive_list
                    
        for col, row_ind_list in col_coord_dict.items():
            if len(row_ind_list) >= 3:
                consecutive_list = get_consecutive(row_ind_list)
                if consecutive_list != []:
                    real_col_consecutive[col] = consecutive_list
                    
        return (real_row_consecutive, real_col_consecutive)
    

def generate_map(config_file):
    
    mapping = []
    with open(config_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        position_dict = {}
        for row in csvreader:
            if row['type'] == 'height':
                height = int(row['value'])
            elif row['type'] == 'width':
                width = int(row['value'])
            elif row['type'] == 'box':
                position_dict[(int(row['x']),int(row['y']))] = "B"
            elif row['type'] == 'storage':
                position_dict[(int(row['x']),int(row['y']))] = "S"
            elif row['type'] == 'obstacle':
                position_dict[(int(row['x']),int(row['y']))] = "O"
            elif row['type'] == 'character':
                position_dict[(int(row['x']),int(row['y']))] = "C"
        
        for y in range(height):
            row = []
            for x in range(width):
                if (y,x) in position_dict.keys():
                    row.append(position_dict[(y,x)])
                else:
                    row.append("-")
            mapping.append(row)
        return mapping          
#pretty_printer(generate_map("game_cfg.csv"))


def testing_input(matrix):
    
    pretty_printer(matrix)
    
    # FIRST INITIALIZATION
    char_pos = get_char_position(matrix,"C")[0]
    box_pos = get_char_position(matrix,"B")
    storage_pos = get_char_position(matrix,"S")
    obstacle_pos = get_char_position(matrix,"O")
    powerup = generate_powerups(matrix, obstacle_pos)
    print ("Power-up generated! Get the power-up and remove a random box on the map!")
    
    while True:          
        
        consecutive_positions = check_consecutive(box_pos)
        user_input = input("Move? ").lower()
        if user_input not in ["w","a","s","d","x"]:
            print ("You can only choose w,a,s,d to move or x to exit game!")
            pretty_printer(matrix)
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
                        # CHECKING ROW
                    if consecutive_positions != ():
                        if new_box_pos[0] in consecutive_positions[0].keys():
                            for consecutive_list in consecutive_positions[0][new_box_pos[0]]:
                                if new_box_pos[1] in consecutive_list:
                                    print ("You are not strong enough to push these boxes!")
                                    new_char_pos = char_pos
                            # CHECKING COLUMN
                        if new_box_pos[1] in consecutive_positions[1].keys():
                            for consecutive_list in consecutive_positions[1][new_box_pos[1]]:
                                if new_box_pos[0] in consecutive_list:
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
            
            # PLAYER EATS POWERUP:
            if new_char_pos == powerup:
                # DELETE A RANDOM BOX
                popped = box_pos.pop(random.randrange(len(box_pos)))
                matrix[popped[0]][popped[1]] = "-"
                powerup = ()
                
            pretty_printer(matrix)
            
            
            # WINNING ANNOUCEMENT
            if box_pos == []:
                print ("YOU WIN!")
                break
testing_input(generate_map("game_cfg.csv"))
