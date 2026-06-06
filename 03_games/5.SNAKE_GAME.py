import pygame
import random
import sys

# --- GLOBAL CONSTANTS ---
# Using uppercase for constants to follow PEP 8 styling rules
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20  # Each grid square is 20x20 pixels

# Color Palettes (RGB Tuples)
COLOR_BG = (30, 30, 40)       # Dark Slate Blue
COLOR_SNAKE = (46, 204, 113)  # Emerald Green
COLOR_FOOD = (231, 76, 60)    # Alizarin Red
COLOR_TEXT = (255, 255, 255)  # White

# Movement Vector Directions
UP = (0, -GRID_SIZE)
DOWN = (0, GRID_SIZE)
LEFT = (-GRID_SIZE, 0)
RIGHT = (GRID_SIZE, 0)


class Snake:
    """Handles the snake's state, position updates, and growth logic."""
    def __init__(self):
        self.reset()

    def reset(self):
        # Start in the middle of the screen
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow_status = False

    def update_position(self):
        # Calculate new head position using the current direction vector
        current_head = self.body[0]
        new_head = (current_head[0] + self.direction[0], current_head[1] + self.direction[1])
        
        # Insert the new head position at the front of the list
        self.body.insert(0, new_head)
        
        # If the snake didn't eat food, pop the tail to simulate movement
        if not self.grow_status:
            self.body.pop()
        else:
            # If it ate food, retain the tail segment to grow, then reset flag
            self.grow_status = False

    def change_direction(self, new_dir):
        # Block 180-degree instant self-collision turns
        if (new_dir[0] + self.direction[0] == 0) and (new_dir[1] + self.direction[1] == 0):
            return
        self.direction = new_dir

    def check_collision(self):
        head = self.body[0]
        # Wall Collisions
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        # Self Collisions (checking if head coordinates overlap any body block)
        if head in self.body[1:]:
            return True
        return False

    def draw(self, surface):
        # Render each block of the snake's body as a rectangle
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, COLOR_SNAKE, rect)


class Food:
    """Manages the spawning and rendering of the target food item."""
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position([])

    def randomize_position(self, snake_body):
        # Ensure the food spawns perfectly snapped inside our grid system
        while True:
            x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
            self.position = (x, y)
            # Prevent spawning food directly on top of the snake's body
            if self.position not in snake_body:
                break

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, COLOR_FOOD, rect)


class GameManager:
    """Main execution orchestrator regulating mechanics, rendering, and scores."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Master System")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.food.randomize_position(self.snake.body)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)

    def run(self):
        # Main Game loop execution
        while True:
            self.process_events()
            
            # Physics/Mechanics Update
            self.snake.update_position()
            
            # Check if snake reached the food coordinates
            if self.snake.body[0] == self.food.position:
                self.snake.grow_status = True
                self.score += 10
                self.food.randomize_position(self.snake.body)
            
            # Check failure thresholds
            if self.snake.check_collision():
                # On death, reset states
                self.snake.reset()
                self.food.randomize_position(self.snake.body)
                self.score = 0

            # Graphical Rendering Stage
            self.screen.fill(COLOR_BG)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            
            # Draw Score Interface
            score_surf = self.font.render(f"Score: {self.score}", True, COLOR_TEXT)
            self.screen.blit(score_surf, (10, 10))
            
            pygame.display.update()
            
            # Framerate cap sets the tick speed of the physics calculations
            self.clock.tick(10)  # 10 frames per second controls the game speed


if __name__ == "__main__":
    game = GameManager()
    game.run()