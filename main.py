import pygame
from my_sprite import my_sprite
from colliding_object import colliding_object
from moving_vehicle import moving_vehicle

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    car1 = moving_vehicle("Project 3/red_car.png", (430, 1070))
    car2 = moving_vehicle("Project 3/yellow_convertible.png", (430, 1200))
    vehicles = [car1, car2]

    car1.image = pygame.transform.rotozoom(car1.image, 0, 0.8)
    car2.image = pygame.transform.rotozoom(car2.image, 0, 0.8)

    obstacles = [
        colliding_object("Project 3/tree.png", (1660, 860), scale = 0.8),
        colliding_object("Project 3/green_car.png", (1810, 300), scale = 0.8, angle = 90),
        colliding_object("Project 3/blueish_van.png", (1930, 300), scale = 0.8, angle = 90),
        colliding_object("Project 3/orange_truck.png", (2060, 525)),
        colliding_object("Project 3/orange_truck.png", (2060, 645)),

    ]

    decorations = [
        my_sprite("Project 3/road_straight.png", (400, 990), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (650, 990), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (900, 990), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (1150, 990), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (1300, 990), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (1550, 990), scale = 0.5),
        
        my_sprite("Project 3/road_turn_up.png", (1720, 977), scale = 0.52, angle = 180),
        my_sprite("Project 3/road_straight.png", (1733, 747), scale = 0.5, angle = 90),
        my_sprite("Project 3/road_intersection.png", (1777, 497), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (2030, 453), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (1733, 241), scale = 0.5, angle = 90),

        my_sprite("Project 3/road_straight.png", (1530, 453), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (1280, 453), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (1030, 453), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (780, 453), scale = 0.5),
        my_sprite("Project 3/road_straight.png", (530, 453), scale = 0.5),
        my_sprite("Project 3/road_straight_alt.png", (380, 453), scale = 0.5),

        my_sprite("Project 3/Start.png", (600, 1050), scale = 0.15, angle = -90),
        my_sprite("Project 3/Finish.png", (490, 519), scale = 0.15, angle = 90),
    ]

    speed = 8
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        x, y = car1.x, car1.y
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        car1.set_location((x, y))

        x, y = car2.x, car2.y
        if keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_d]:
            x += speed
        if keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_s]:
            y += speed
        car2.set_location((x, y))

        for vehicle in vehicles:
            for obstacle in obstacles:
                if vehicle.is_colliding_with(obstacle):
                    print(f"{vehicle} collided with {obstacle}")

        screen.fill((135, 206, 235))

        for deco in decorations:
            screen.blit(deco.get_image(), (deco.x, deco.y))

        for obs in obstacles:
            screen.blit(obs.get_image(), (obs.x, obs.y))

        for vehicle in vehicles:
            screen.blit(vehicle.get_image(), (vehicle.x, vehicle.y))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
