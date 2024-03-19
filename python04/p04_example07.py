# pip install pygame
import pygame

# Define some colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Green color for the square

# Initialize Pygame
pygame.init()

# Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("Moving Square")

# Define square properties
square_x = width // 2  # Center the square horizontally
square_y = height // 2  # Center the square vertically
square_side_length = 50  # Size of the square
square_color = GREEN

# Movement speed
movement_speed = 5

run = True
clock = pygame.time.Clock()

# Main loop
while run:
  # Set the FPS
  fps = clock.tick(60)

  # Check for events (specifically arrow keys)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        square_x -= movement_speed
      elif event.key == pygame.K_RIGHT:
        square_x += movement_speed
      elif event.key == pygame.K_UP:
        square_y -= movement_speed
      elif event.key == pygame.K_DOWN:
        square_y += movement_speed

  # Keep the square within screen boundaries
  square_x = max(0, min(square_x, width - square_side_length))  # Clamp x between 0 and width - side_length
  square_y = max(0, min(square_y, height - square_side_length))  # Clamp y between 0 and height - side_length

  # Clear the screen
  screen.fill(BLACK)

  # Draw the square
  pygame.draw.rect(screen, square_color, (square_x, square_y, square_side_length, square_side_length))

  # Update the screen
  pygame.display.flip()

# Quit Pygame
pygame.quit()
