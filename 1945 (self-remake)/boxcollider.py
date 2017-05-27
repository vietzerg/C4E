from pygame import Rect
import point

class BoxCollider:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def check_collide(self, other_box_collider):
        rect0 = Rect(self.position.x, self.position.y, self.width, self.height)
        rect1 = Rect(other_box_collider.position.x, other_box_collider.position.y, other_box_collider.width, other_box_collider.height)
        return rect0.colliderect(rect1)