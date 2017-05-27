import pygame

def createImagePath(object_string, kind):
    return "resources/sprites/{0}/{0}_{1}.png".format(object_string, kind)

def loadImages(object_string, kind_list):
    image_package = {}
    for kind in kind_list:
        image_package[kind] = pygame.image.load(createImagePath(object_string, kind))
    return image_package

# HARD-CODE THIS TIME
def extract_animations(image, frames):
    step = image.get_width() / 6
    result = []
    for i in range(1, 7):
        frame = image.subsurface((step*(i-1) + 1, 1, 32, 32))
        frame.set_colorkey((255,255,255))
        result.append(frame)
    return result


class SpriteRenderer:
    def __init__(self, an_object, object_string, kind_list):
        self.images = loadImages(object_string, kind_list)
        self.width = self.images["main"].get_width()
        self.height = self.images["main"].get_height()
        self.alive = an_object.alive
        if an_object.death_ticker is not None:
            self.death_ticker = an_object.death_ticker

    def draw_alive(self, screen, position):
        screen.blit(self.images["main"], (position.x, position.y))

    def draw_death(self, screen, position):
        death_frames = extract_animations(self.images["explosion"], 6)
        if self.death_ticker % 6 == 0:
            print (self.death_ticker)
            screen.blit(death_frames[int(self.death_ticker / 6) - 1], (position.x, position.y))

    def draw(self, screen, position):
        if self.alive == True:
            self.draw_alive(screen, position)
        if self.alive == False:
            self.draw_death(screen, position)

# Load, for example
#print (loadImages("player", ["main", "bullet", "explosion"]))