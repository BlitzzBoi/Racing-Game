import pygame
import sys
import time

from my_sprite import my_sprite
from colliding_object import colliding_object
from moving_vehicle import moving_vehicle

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1600
FPS = 60

def draw_text(screen, text, size, color, pos):

    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=pos)
    screen.blit(surface, rect)

def button(screen, text, pos, size=(300, 100), color=(100, 100, 255)):

    rect = pygame.Rect(pos[0]-size[0]//2, pos[1]-size[1]//2, size[0], size[1])
    pygame.draw.rect(screen, color, rect)
    draw_text(screen, text, 60, (255, 255, 255), rect.center)

    return rect

def countdown(screen):

    for i in range(3, 0, -1):

        screen.fill((0, 0, 0))
        draw_text(screen, str(i), 200, (255, 255, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        time.sleep(1)

    screen.fill((0, 0, 0))
    draw_text(screen, "GO!", 200, (0, 255, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    time.sleep(1)

def game_over_screen(screen, car1_time, car2_time):

    while True:

        screen.fill((30, 30, 30))
        draw_text(screen, "GAME OVER", 100, (255, 255, 0), (SCREEN_WIDTH//2, 400))
        draw_text(screen, f"Car 1: {car1_time}", 70, (255, 255, 255), (SCREEN_WIDTH//2, 600))
        draw_text(screen, f"Car 2: {car2_time}", 70, (255, 255, 255), (SCREEN_WIDTH//2, 700))
        restart_btn = button(screen, "Restart", (SCREEN_WIDTH//2 - 250, 1000))
        quit_btn = button(screen, "Quit", (SCREEN_WIDTH//2 + 250, 1000))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if restart_btn.collidepoint(event.pos):

                    main()
                elif quit_btn.collidepoint(event.pos):

                    pygame.quit()
                    sys.exit()

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    car1 = moving_vehicle("Project 3/red_car.png", (430, 1070))
    car2 = moving_vehicle("Project 3/yellow_convertible.png", (430, 1200))
    vehicles = [car1, car2]
    car1.original_image = pygame.transform.rotozoom(car1.original_image, 0, 0.8)
    car2.original_image = pygame.transform.rotozoom(car2.original_image, 0, 0.8)
    car1.image = car1.original_image
    car2.image = car2.original_image

    obstacles = [
        colliding_object("Project 3/tree.png", (1660, 860), scale=0.8),
        colliding_object("Project 3/green_car.png", (1810, 300), scale=0.8, angle=90),
        colliding_object("Project 3/blueish_van.png", (1930, 300), scale=0.8, angle=90),
        colliding_object("Project 3/orange_truck.png", (2060, 525)),
        colliding_object("Project 3/orange_truck.png", (2060, 645)),
    ]
    
    decorations = [
        my_sprite("Project 3/road_straight.png", (400, 990), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (650, 990), scale=0.5),
        my_sprite("Project 3/road_straight.png", (900, 990), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (1150, 990), scale=0.5),
        my_sprite("Project 3/road_straight.png", (1300, 990), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (1550, 990), scale=0.5),
        my_sprite("Project 3/road_turn_up.png", (1720, 977), scale=0.52, angle=180),
        my_sprite("Project 3/road_straight.png", (1733, 747), scale=0.5, angle=90),
        my_sprite("Project 3/road_intersection.png", (1777, 497), scale=0.5),
        my_sprite("Project 3/road_straight.png", (2030, 453), scale=0.5),
        my_sprite("Project 3/road_straight.png", (1733, 241), scale=0.5, angle=90),
        my_sprite("Project 3/road_straight.png", (1530, 453), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (1280, 453), scale=0.5),
        my_sprite("Project 3/road_straight.png", (1030, 453), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (780, 453), scale=0.5),
        my_sprite("Project 3/road_straight.png", (530, 453), scale=0.5),
        my_sprite("Project 3/road_straight_alt.png", (380, 453), scale=0.5),
        my_sprite("Project 3/Start.png", (600, 1050), scale=0.15, angle=-90),
        my_sprite("Project 3/Finish.png", (490, 519), scale=0.15, angle=90),
    ]
    
    finish_line = pygame.Rect(490, 519, 200, 100)
    countdown(screen)
    start_time = time.time()
    
    controls = [
        {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT},
        {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d}
    ]
    
    running = True

    while running:
        screen.fill((60, 150, 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        for i, car in enumerate(vehicles):
            car.move(keys, controls[i])
            for obs in obstacles:
                if car.is_colliding_with(obs):
                    car.movable = False
            if finish_line.colliderect(car.get_bounding_box()):

                car.finished = True
                car.movable = False

        for deco in decorations:
            screen.blit(deco.get_image(), (deco.x, deco.y))
        for obs in obstacles:
            screen.blit(obs.get_image(), (obs.x, obs.y))
        for car in vehicles:
            screen.blit(car.get_image(), (car.x, car.y))

        elapsed = round(time.time() - start_time, 2)
        draw_text(screen, f"Time: {elapsed}s", 60, (255, 255, 255), (200, 50))
        pygame.display.flip()
        clock.tick(FPS)
        all_done = all([not c.movable for c in vehicles])

        if all_done or any([c.finished for c in vehicles]):
            car1_time = f"{round(time.time() - start_time, 2)}s" if car1.finished else "DNF"
            car2_time = f"{round(time.time() - start_time, 2)}s" if car2.finished else "DNF"
            game_over_screen(screen, car1_time, car2_time)

if __name__ == "__main__":
    main()
