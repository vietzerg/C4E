import csv
class Map:
    def __init__(self, config_file):
        
        # SETTING UP THE PROPERTIES OF THE MAP
        self.obstacles = []
        self.boxes = []
        self.storages = []
        self.objects = []
        #self.objects_dict = {"chaien": 0, "obstacles": [], "boxes": [], "storages": []}
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
    
    # CHECK IF THE CHARACTER'S NEXT POSITION IS AT A BOX (CHARACTER TRIES TO MOVE A BOX)
    def in_boxes(self, position_tuple):
        for box in self.boxes:
            if box.x == position_tuple[0] and box.y == position_tuple[1]:
                return box
        return False
    
    # CHECK IF THE CHARACTER HITS AN OBSTACLE
    def in_obstacles(self, position_tuple):
        
    
    # MAIN PROGRAM    
    def process_input(self):
        move = input("Your move? ").upper()
        dx = 0
        dy = 0

        if move == "W":
            dx = 0
            dy = -1           
        elif move == "S":
            dx = 0
            dy = 1
        elif move == "A":
            dx = -1
            dy = 0
        elif move == "D":
            dx = 1
            dy = 0
        
        C_next = self.chaien.next_pos(dx, dy)
        
        if self.in_boxes(C_next) is not False:
            box_pushed = self.in_boxes(C_next)
            B_next = box_pushed.next_pos(dx, dy)
            
            # CHECK IF B NEXT IS IN MAP
            if self.in_map(B_next):
                box_pushed.move(dx ,dy)
                self.chaien.move(dx ,dy)
            else:
                print ("Can't push box out of map!")
        
        # CHECK IF CHARACTER IS IN MAP
        elif self.in_map(C_next):
            self.chaien.move(dx, dy)
            
        else:
            print ("Can't move out of map")


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
    
    
    
        
map1 = Map("game_cfg.csv")
while True:
    map1.printer()
    map1.process_input()
    
#while True:
#    inp = input("Run?").upper()
#    if inp != "X":       
#        map1.printer()
#        map1.process_input()
#    else:
#        break