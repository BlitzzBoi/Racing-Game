import pygame

class my_sprite:
    def __init__(self, image_fname: str, loc: tuple[int, int] = (0, 0), scale: float = 1.0, angle: float = 0):
        self.image_fname = image_fname
        self.loc = loc

        self.image = pygame.image.load(image_fname)

        if scale != 1.0 or angle != 0:
            self.image = pygame.transform.rotozoom(self.image, angle, scale)

        self.x, self.y = loc
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_image(self):
        return self.image

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
