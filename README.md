# 🕹️ Project Overview — Sprite Inheritance and Collision System (Pygame)

This project demonstrates the use of object-oriented programming with inheritance in Python, following the SOLID design principles, while integrating the Pygame library for graphical representation and collision detection.

It builds a small interactive framework where different types of game objects (sprites, collidable objects, and moving vehicles) are modeled through a class hierarchy. The program visually displays and moves objects on a Pygame window, detects collisions, and manages sprite rendering.

# 🧱 Class Architecture
1. my_sprite

Represents the most basic game object:
- Loads and stores an image (image_fname) and its position (loc).
- Provides basic getters for the sprite’s image, width, and height.
- Can optionally be scaled or rotated when loaded.
- Serves as the foundation for all drawable objects, including decorative sprites, vehicles, and obstacles.

2. colliding_object (inherits from my_sprite)

Extends my_sprite by adding collision detection capabilities:
- Creates a bounding box (pygame.Rect) based on the image’s position and size.
- Provides a method is_colliding_with() that checks whether it overlaps another colliding_object.
- Used for static or dynamic entities that interact with collisions, such as obstacles and vehicles.

3. moving_vehicle (inherits from colliding_object)

Adds full movement and gameplay functionality:
- Includes a set_location() method to update the object’s position and bounding box dynamically.
- Implements move() to respond to keyboard input for directional movement.
- Supports diagonal movement with accurate rotation based on the direction of travel.
- Prevents vehicles from leaving the screen by detecting and freezing on world boundaries.
- Can be frozen permanently when colliding with an obstacle or reaching the finish line.
- Designed for player-controlled entities that move, rotate, and interact with their surroundings.

# 🏁 Main Program (main.py)

The main.py file brings all the components together into a fully interactive racing simulation built with Pygame:
- Initializes the game window, assets, and main loop.
- Creates:
  - Two controllable vehicles (moving_vehicle objects) that can move with keyboard input (Car 1: Arrow Keys, Car 2: WASD).
  - Multiple colliding objects that serve as obstacles or other vehicles on the road.
  - Several decorative sprites that visually build the racetrack layout, including road tiles, start, and finish lines.

- Implements a 3–2–1 countdown before the race begins.
- Continuously updates movement, collision detection, and rendering in real-time.
- Detects when a car reaches the finish line or when both cars are immobilized, triggering the Game Over screen.
- Displays a race timer, showing each car’s completion time or “DNF” (Did Not Finish) if they collided.
- Provides an interactive Restart and Quit button at the end of the race.

# ⚙️ Core Features

- Object-Oriented Design: Demonstrates inheritance, specialization, and modular structure across three layered classes.
- Accurate Movement & Rotation: Vehicles rotate smoothly in all eight directions, including diagonals.
- Collision & Boundaries: Cars stop on collision with obstacles or when hitting the screen’s edges.
- Timer & Race Logic: Countdown at start, active race timer, and finish time display for both players.
- Game Over Screen: Clean summary of results, including restart and quit functionality.
