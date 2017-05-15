import csv
       

class SKObject:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
    
    # CHECK IF THE MAP SHOULD PRINT THE OBJECT AT LOCATION (x,y)
    def printer(self, x, y, chaien_x, chaien_y):
        if x == self.x and y == self.y:
            # THIS PRINTER GIVES PRIORITY FOR THE CHARACTER, BECAUSE HE CAN MOVE THROUGH SOME OBJECTS
            if (x, y) != (chaien_x, chaien_y):
                print (self.char, end="")
            if (x, y) == (chaien_x, chaien_y):
                print (" C ", end ="")
            return True
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    # GET THE NEXT POSTIION, NOT MOVE YET. USED FOR CHECKING CONDITIONS
    def next_pos(self, dx, dy):
        nextx = self.x + dx
        nexty = self.y + dy
        return (nextx, nexty)
    
    
class Map:
    def __init__(self, config_file):
        
        # SETTING UP THE PROPERTIES OF THE MAP
        self.mana = 0
        self.obstacles = []
        self.boxes = []
        self.storages = []
        self.blinks = []
        self.objects = []
        with open(config_file, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row["type"] == "height":
                    self.height = int(row["value"])
                elif row["type"] == "width":
                    self.width = int(row["value"])
                elif row["type"] == "obstacle":
                    a_obstacle = SKObject(int(row["x"]), int(row["y"]), " O ")
                    self.obstacles.append(a_obstacle)
                    self.objects.append(a_obstacle)
                elif row["type"] == "box":
                    a_box = SKObject(int(row["x"]), int(row["y"]), " B ")
                    self.boxes.append(a_box)
                    self.objects.append(a_box)
                elif row["type"] == "storage":
                    a_storage = SKObject(int(row["x"]), int(row["y"]), " S ")
                    self.storages.append(a_storage)
                    self.objects.append(a_storage)
                elif row["type"] == "character":
                    self.chaien = SKObject(int(row["x"]), int(row["y"]), " C ")
                    self.objects.append(self.chaien)
                elif row["type"] == "blink":
                    a_blink = SKObject(int(row["x"]), int(row["y"]), " - ")
                    self.blinks.append(a_blink)
                    self.objects.append(a_blink)
        
    # CHECK IF THE (x,y) LOCATION IS AT ANY MAP OBJECT
    # CHECK IF THERE IS ANY OBJECT PRINTED !!!
    def print_objects(self, x, y):
        for obj in self.objects:
            if obj.printer(x, y, self.chaien.x, self.chaien.y):
                return True
        return False
    
    # PRINT MAP
    def printer(self):        
        for y in range(self.height):
            for x in range(self.width):
                if not self.print_objects(x, y): # IF NO OJBECT IS PRINTED, THEN...
                    print (" - ", end ="")
            print()
            
    # CHECK IF THE POSTIION (x,y) IS INSIDE THE MAP
    def in_map(self, position_tuple):
        if position_tuple[1] >= 0 and position_tuple[1] < self.height and position_tuple[0] >= 0 and position_tuple[0] < self.width:
            return True
        else:
            return False
    
    # CHECK IF CHARACTER HITS AN OBJECT SERIES (SERIES OF BOXES, OBSTACLES, BLINK-POWERUPS)    
    def in_object_series(self, that_object_list, position_tuple):
        for obj in that_object_list:
            if obj.x == position_tuple[0] and obj.y == position_tuple[1]:
                return obj
        return False

    # GET A LIST BOXES TO MOVE (IN CASE CHARACTER PUSHES MULTIPLE BOXES)
    def get_boxes_to_move(self, box_pushed, dx, dy):
        boxes_to_move = [box_pushed]
        
        if dx == 1:
            for box in self.boxes:
                if box.x == boxes_to_move[-1].x + 1 and box.y == boxes_to_move[-1].y:
                    boxes_to_move.append(box)
        elif dx == -1:
            for box in reversed(self.boxes):
                if box.x == boxes_to_move[-1].x - 1 and box.y == boxes_to_move[-1].y:
                    boxes_to_move.append(box)
        elif dy == 1:
            for box in self.boxes:
                if box.y == boxes_to_move[-1].y + 1 and box.x == boxes_to_move[-1].x:
                    boxes_to_move.append(box)
        elif dy == -1:
            for box in reversed(self.boxes):
                if box.y == boxes_to_move[-1].y - 1 and box.x == boxes_to_move[-1].x:
                    boxes_to_move.append(box)
        
        return boxes_to_move        
        
    # MOVE MULTIPLE BOXES
    def move_boxes(self, boxes_to_move, dx, dy):
        for box in boxes_to_move:
            box.move(dx, dy)            
    
    # CHECK IF A BOX IS IN A STORAGE POINT
    def in_storage(self):
        for box in self.boxes:
            for storage in self.storages:
                if (box.x, box.y) == (storage.x, storage.y):
                    return box
        return False
    
    # REMOVE AN OBJECT (A BOX)
    def remover(self, that_object_list, object_to_remove):
        self.objects.remove(object_to_remove)
        that_object_list.remove(object_to_remove)
        del object_to_remove

    # CHECK IF CHARACTER BLINKED
    def check_blink(self, dx, dy):
        if (dx,dy) == (0,-3) or (dx,dy) == (0,3) or (dx,dy) == (-3,0) or (dx,dy) == (3,0):
            return True
        else:
            return False
    
    # MAIN PROGRAM    
    def process_input(self):
        move = input("Your move? ").upper()
        dx = 0
        dy = 0

        if move == "W":
            dx,dy = 0,-1
            dx_box,dy_box = dx,dy
        elif move == "S":
            dx,dy = 0,1
            dx_box,dy_box = dx,dy
        elif move == "A":
            dx,dy = -1,0
            dx_box,dy_box = dx,dy
        elif move == "D":
            dx,dy = 1,0
            dx_box,dy_box = dx,dy
        elif move == "BW":
            if self.mana > 0:
                dx,dy = 0,-3
            else:
                dx,dy = 0,-1
                print ("Not enough mana! Moved one step instead")
            dx_box,dy_box = 0,-1            
        elif move == "BS":
            if self.mana > 0:
                dx,dy = 0,3
            else:
                dx,dy = 0,1
                print ("Not enough mana!! Moved one step instead")
            dx_box,dy_box = 0,1
        elif move == "BA":
            if self.mana > 0:
                dx,dy = -3,0
            else:
                dx,dy = -1,0
                print ("Not enough mana!! Moved one step instead")
            dx_box,dy_box = -1,0
        elif move == "BD":
            if self.mana > 0:
                dx,dy = 3,0
            else:
                dx,dy = 1,0
                print ("Not enough mana!! Moved one step instead.")
            dx_box,dy_box = 1,0          
        else:
            print ("You can choose among (W,A,S,D) !")
            
        C_next = self.chaien.next_pos(dx, dy)
        
        # CHECK IF CHARACTER TRIES TO PUSH A BOX AND MOVE MULTIPLE/SINGLE BOX/BOXES
        if self.in_object_series(self.boxes,C_next) is not False:
            box_pushed = self.in_object_series(self.boxes, C_next)
            boxes_to_move = self.get_boxes_to_move(box_pushed, dx_box, dy_box)
            last_box_next = boxes_to_move[-1].next_pos(dx_box ,dy_box)
            
            # CHECK IF THE LAST BOX IN THE BOX SERIES IS IN MAP AND HITS AN OBSTACLE
            if self.in_map((last_box_next[0], last_box_next[1])) and self.in_object_series(self.obstacles, (last_box_next[0], last_box_next[1])) == False: # IF THE LAST BOX DOES NOT HIT ANYTHING, THEN...
                    self.move_boxes(boxes_to_move, dx_box, dy_box)
                    self.chaien.move(dx ,dy)
                    # CHECK IF THE MOVE WAS BLINK OR NOT
                    if self.check_blink(dx, dy):
                        self.mana -= 1
            else:
                print ("Unable to move box(es).")
        
        # CHECK IF C NEXT HITS AN OBSTACLE
        elif self.in_object_series(self.obstacles, C_next) != False:
            pass
        
        # CHECK IF CHARACTER IS IN MAP
        elif self.in_map(C_next):
            self.chaien.move(dx, dy)
            # CHECK IF THE MOVE WAS BLINK OR NOT
            if self.check_blink(dx, dy):
                self.mana -= 1
            
        else:
            print ("Can't move out of map!")
            
        # CHECK IF CHARACTER EATS BLINK
        if self.in_object_series(self.blinks, (self.chaien.x, self.chaien.y)) != False:
            self.mana = 3
            blink_to_remove = self.in_object_series(self.blinks, (self.chaien.x, self.chaien.y))
            self.remover(self.blinks, blink_to_remove)
            print ("You got a blink-powerup! 3 steps per move for 3 moves!\nPress b + a direction button to blink!")
        
        # CHECK IF A BOX IS IN THE STORAGE POINT
        if self.in_storage() != False:
            box_to_remove = self.in_storage()
            self.remover(self.boxes, box_to_remove)
        
        if self.boxes == []:
            print ("You win!")
            return False
        
        print ("Your mana:",self.mana)     

    
map1 = Map("game_cfg.csv")
while True:
    map1.printer()
    run = map1.process_input()
    if run == False:
        break