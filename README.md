# 🕹️ Project Overview — Sprite Inheritance and Collision System (Pygame)

This project demonstrates the use of object-oriented programming with inheritance in Python, following the SOLID design principles, while integrating the Pygame library for graphical representation and collision detection.

It builds a small interactive framework where different types of game objects (sprites, collidable objects, and moving vehicles) are modeled through a class hierarchy. The program visually displays and moves objects on a Pygame window, detects collisions, and manages sprite rendering.

# 🧱 Class Architecture
1. my_sprite

Represents the most basic game object:
  - Loads and stores an image (image_fname) and its position (loc).
  - Provides basic getters for the sprite’s image, width, and height.
  - Can optionally be scaled or rotated when loaded.

2. colliding_object (inherits from my_sprite)

Extends my_sprite by adding collision detection:
  - Creates a bounding box (pygame.Rect) based on the image size and position.
  - Provides a method is_colliding_with() that checks whether it overlaps another colliding object.

3. moving_vehicle (inherits from colliding_object)

Adds movement capabilities:
  - Includes a set_location() method to update the object’s position and bounding box dynamically.
  - Used for player-controlled vehicles that can move around the screen.

# 🏁 Main Program (main.py)

The main.py file creates an interactive Pygame simulation that demonstrates how these classes work together:
- Initializes the Pygame window and main loop.
- Creates:
  - Two controllable vehicles (moving_vehicle objects) that can move with keyboard input.
  - Five colliding objects that act as obstacles.
  - Five decorative sprites for visual background elements.
- Continuously updates the screen, handles movement, checks for collisions, and displays all sprites.

# ⚙️ Core Features

- Object hierarchy demonstrates inheritance and specialization.
- Each class fulfills a single responsibility (display, collision, movement).
- Vehicles can move and detect when they collide with obstacles.
- Code follows SOLID design principles for clarity and maintainability.
