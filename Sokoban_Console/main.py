class Map:
    def  __init__(self):
        self.width = 5
        self.height = 5
        self.chaien = SKObject(2, 3, " C ")
        self.box = SKObject(3, 3, " B ")
        self.objects = [self.chaien, self.box]
        
    def print_objects(self, x, y):
        for object in self.objects:
            if object.print(x, y):
                return True
        return False
        
    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if  self.print_objects(x, y):
                    pass
                else:
                    print (" - ", end = "")                    
            print ()
            
    def process_input(self):
        move = input("Your move? ").upper()
        dx = 0
        dy = 0
        
        if move == "D":
            dx = 1
        # TODO: MOVE UP LEFT DOWN
        
        [next_x, next_y] = self.chaien.calculate_next(dx, dy)
        
class SKObject:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.character = char
    
    def print (self, x, y):
        if self.x == x and self.y == y:
            print (self.character, end = "")
            return True
        return False
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def calculate_next(self, dx, dy):
        return (self.x + dx, self.y + dy)
    
            
sokoban_map = Map()
while True:
    sokoban_map.print()
    sokoban_map.process_input()
#print (sokoban_map.z)