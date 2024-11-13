import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

class Player:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.position = 0
        self.safe_positions = [1, 9, 25, 36, 49]

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, roll):
        self.position += roll
        if self.position > 52:
            self.position -= roll
            print("Cannot move forward. You need to roll exact number to reach home.")
            return

        if self.position in self.safe_positions:
            print(f"{self.name} moved to safe position {self.position}.")
        else:
            print(f"{self.name} moved to position {self.position}.")


class LudoGame:
    def __init__(self):
        self.players = []
        self.current_player = 0

    def add_player(self, name, color, x, y):
        self.players.append(Player(name, color, x, y))

    def start_game(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        roll = self.players[self.current_player].roll_dice()
                        print(f"{self.players[self.current_player].name} rolled a {roll}.")
                        self.players[self.current_player].move(roll)

                        if self.players[self.current_player].position == 52:
                            print(f"\n{self.players[self.current_player].name} wins!")
                            running = False

                        self.current_player = (self.current_player + 1) % len(self.players)

            screen.fill(WHITE)

            # Draw game board
            pygame.draw.rect(screen, (0, 0, 0), (100, 100, 600, 400), 1)

            # Draw player tokens
            for player in self.players:
                pygame.draw.circle(screen, player.color, (player.x + player.position * 10, player.y), 20)

            # Draw safe positions
            for pos in player.safe_positions:
                pygame.draw.rect(screen, (0, 255, 0), (100 + pos * 10 - 5, 100 - 20, 10, 20))

            pygame.display.flip()
            clock.tick(60)


        pygame.quit()
        sys.exit()


game = LudoGame()

game.add_player("Player 1", RED, 150, 150)
game.add_player("Player 2", GREEN, 150, 450)
game.add_player("Player 3", BLUE, 550, 150)
game.add_player("Player 4", YELLOW, 550, 450)

game.start_game()