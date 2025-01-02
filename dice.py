import pygame
import random
import sys


pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Guesser Game")
font = pygame.font.Font(None, 36)

# Load the dice image
dice_image = pygame.image.load("dice.jpg")
dice_rect = dice_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


target_number = random.randint(1, 6)
guess_count = 0
message = "Click the dice to play!"
game_won = False


def roll_dice():
    return random.randint(1, 6)


# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Display dice
    screen.blit(dice_image, dice_rect)

    # Display message
    message_text = font.render(message, True, BLACK)
    screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, 50))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dice_rect.collidepoint(event.pos) and not game_won:
                rolled_number = roll_dice()
                guess_count += 1
                if rolled_number == target_number:
                    message = f"Good job! It took {guess_count} tries."
                    game_won = True
                else:
                    message = f"Try again! You rolled the number {rolled_number}."

# Exit Game
pygame.quit()
sys.exit()
