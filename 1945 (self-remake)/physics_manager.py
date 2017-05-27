# THIS MODULE IS USED FOR PROCESSING IN-GAME PHYSICAL COLLISION
import boxcollider

class PhysicsManager:
    def __init__(self):
        self.game_objects = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def check_collision(self, other_box_collider):
        for game_object in self.game_objects:
            box_collider0 = other_box_collider
            box_collider1 = game_object.box_collider
            if box_collider0.check_collide(box_collider1):
                return game_object

physicsmanager = PhysicsManager()