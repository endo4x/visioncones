import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FOV = 90
RANGE = 800  # Shorter vision cone range
SPEED = 5
TURN_SPEED = 5
LINE_STEP = 6  # Increase this value to make the lines less frequent

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dual Vision Cone Simulation")
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.angle = 0
        self.radius = 20
        self.speed = SPEED
        self.color = color
        self.vel_x = 0
        self.vel_y = 0

    def move(self, dx, dy):
        self.vel_x = dx
        self.vel_y = dy

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def rotate(self, direction):
        self.angle += direction * TURN_SPEED

def line_rect_collision(line_start, line_end, rect):
    # Simplified collision check: check if the line intersects with the rectangle
    line = pygame.draw.line(screen, (255, 255, 255), line_start, line_end, 1)
    return rect.collidepoint(line_end[0], line_end[1])

def cast_vision_cone(player, target, color, center_block):
    for angle in range(int(player.angle - FOV / 2), int(player.angle + FOV / 2)):
        for distance in range(0, RANGE, LINE_STEP):  # Increase distance step here
            # Calculate the position of the end of the vision cone line
            x = player.x + math.cos(math.radians(angle)) * distance
            y = player.y + math.sin(math.radians(angle)) * distance

            # Check if the vision cone hits the center block
            if center_block.collidepoint(x, y):
                pygame.draw.line(screen, color, (player.x, player.y), (x, y), 1)
                break  # Stop drawing vision cone after hitting the block

            # Check if the vision cone hits the target
            if math.dist((x, y), (target.x, target.y)) < target.radius:
                pygame.draw.line(screen, RED, (player.x, player.y), (x, y), 1)
                break  # Stop drawing vision cone after hitting the target

            # Draw the vision cone in the original color if not obstructed
            pygame.draw.line(screen, color, (player.x, player.y), (x, y), 1)

def game_loop():
    player1 = Player(150, HEIGHT // 2, BLUE)
    player2 = Player(WIDTH - 150, HEIGHT // 2, WHITE)
    center_block = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 - 150, 50, 300)  # Thinner vertical block

    # Set player2 to initially face player1
    player2.angle = math.degrees(math.atan2(player1.y - player2.y, player1.x - player2.x))

    running = True
    while running:
        screen.fill(BLACK)

        # Draw the vertical center block (GREY)
        pygame.draw.rect(screen, GREY, center_block)  # Draw the solid block
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        # Reset velocities when no keys are pressed
        player1.vel_x = 0
        player1.vel_y = 0
        player2.vel_x = 0
        player2.vel_y = 0

        # Player 1 (WASD and Q/E for rotation)
        if keys[pygame.K_w]: player1.move(0, -SPEED)
        if keys[pygame.K_s]: player1.move(0, SPEED)
        if keys[pygame.K_a]: player1.move(-SPEED, 0)
        if keys[pygame.K_d]: player1.move(SPEED, 0)
        if keys[pygame.K_q]: player1.rotate(-1)  # Rotate left
        if keys[pygame.K_e]: player1.rotate(1)   # Rotate right

        # Player 2 (Arrow keys and ,/. for rotation)
        if keys[pygame.K_UP]: player2.move(0, -SPEED)
        if keys[pygame.K_DOWN]: player2.move(0, SPEED)
        if keys[pygame.K_LEFT]: player2.move(-SPEED, 0)
        if keys[pygame.K_RIGHT]: player2.move(SPEED, 0)
        if keys[pygame.K_COMMA]: player2.rotate(-1)  # Rotate left
        if keys[pygame.K_PERIOD]: player2.rotate(1)  # Rotate right

        player1.update()
        player2.update()

        pygame.draw.circle(screen, player1.color, (player1.x, player1.y), player1.radius)
        pygame.draw.circle(screen, player2.color, (player2.x, player2.y), player2.radius)

        # Cast vision cones
        cast_vision_cone(player1, player2, BLUE, center_block)
        cast_vision_cone(player2, player1, WHITE, center_block)

        pygame.display.flip()
        clock.tick(60)  # Lock to 60 FPS for smooth performance

    pygame.quit()

game_loop()
