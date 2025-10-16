from colliding_object import colliding_object
import pygame
import math

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1600

class moving_vehicle(colliding_object):
    def __init__(self, image_fname: str, loc: tuple[int, int] = (0, 0)):
        super().__init__(image_fname, loc)
        self.angle = 0
        self.original_image = self.image
        self.speed = 5
        self.movable = True
        self.finished = False

    def set_location(self, loc: tuple[int, int]):
        self.loc = loc
        self.x, self.y = loc
        self.bounding_box.topleft = loc

    def move(self, keys, controls):
        if not self.movable or self.finished:
            return
        dx, dy = 0, 0
        if keys[controls["up"]]: dy -= 1
        if keys[controls["down"]]: dy += 1
        if keys[controls["left"]]: dx -= 1
        if keys[controls["right"]]: dx += 1

        if dx != 0 and dy != 0:
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)
            
        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        if new_x < 0 or new_x > SCREEN_WIDTH - self.get_width() or new_y < 0 or new_y > SCREEN_HEIGHT - self.get_height():
            self.movable = False
            return
        if dx == 0 and dy == 0:
            angle = self.angle
        else:
            angle = math.degrees(math.atan2(-dy, dx))

        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.set_location((new_x, new_y))
