from core.players import Player, HumanPlayer, RandomBot, SmartBot, EMPTY
from typing import List, Tuple
from core.game import Game
import pygame


# --- Drawing constants ---
WIDTH, HEIGHT = 600, 600
CELL: int = WIDTH // 3
LINE_WIDTH: int = 6
FPS: int = 60

BG: tuple[int, int, int] = (255, 255, 255)
FG: tuple[int, int, int] = (0, 0, 0)

# ------------ listen to mouse ------------ #

# ------------ drow the lines ------------ #

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG)

        # RENDER YOUR GAME HERE

        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()