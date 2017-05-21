import pygame
import enemy
import bullet
import time

# HANDLE THE RUNNING AND DRAWING OF ALL GAME OBJECTS
class GameManager:
    def __init__(self):
        self.game_objects = []
        self.planes = []
        self.bullets = []

    def add_plane(self, plane):
        self.planes.append(plane)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def add(self, game_object):
        self.game_objects.append(game_object)
        if game_object.type == "plane":
            self.planes.append(game_object)
        elif game_object.type == "bullet":
            self.bullets.append(game_object)
        else:
            pass

    def remover(self, game_object):
        try:
            if game_object in self.planes:
                self.planes.remove(game_object)
            elif game_object in self.bullets:
                self.bullets.remove(game_object)
            self.game_objects.remove(game_object)
        except Exception:
            pass

    def run(self):
        for game_object in self.game_objects:
            game_object.run()

    def draw(self, screen):
        for game_object in self.game_objects:
            game_object.draw(screen)



# HANDLE THE CREATION OF ALL OBJECTS, LEVELS
class LevelManager:
    def __init__(self):
        self.level = 0

    def generate_enemies(self, screen, n):
        first_enemy = enemy.Enemy(screen.get_width() / 2, -5)
        gamemanager.add(first_enemy)
        for i in range(1, n):
            left_enemy = enemy.Enemy(screen.get_width () / 2 - i*first_enemy.image.get_width(), -5)
            gamemanager.add(left_enemy)
        for i in range(1, n):
            right_enemy = enemy.Enemy(screen.get_width () / 2 + i*first_enemy.image.get_width(), -5)
            gamemanager.add(right_enemy)

    # CHECK IF BULLET HITS A PLANE
    def check_hit(self):
        for bullet in gamemanager.bullets:
            for plane in gamemanager.planes:
                if bullet.x >= plane.x and bullet.x <= plane.x + plane.image.get_width() and bullet.y >= plane.y and bullet.y <= plane.y + plane.image.get_height():
                    gamemanager.remover(bullet)
                    plane.alive = False

    def cleanup(self):
        for plane in gamemanager.planes:
            if plane.dead_ticker == 5 and plane.alive == False:
                gamemanager.remover(plane)


gamemanager = GameManager()
levelmanager = LevelManager()