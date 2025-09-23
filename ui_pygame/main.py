import pygame
from typing import Tuple

WIDTH, HEIGHT = 600, 600
CELL: int = WIDTH // 3
FPS: int = 60

def cell_from_mouse(pos: Tuple[int, int]) -> int:
    x, y = pos
    c = x // CELL
    r = y // CELL
    if 0 <= r < 3 and 0 <= c < 3:
        return r * 3 + c
    return -1

def draw_board(screen: pygame.Surface) -> None:
    # Load and (optionally) scale your board image to fit the window
    board_img = pygame.image.load("img/board.png").convert()
    board_img = pygame.transform.smoothscale(board_img, (WIDTH, HEIGHT))
    screen.blit(board_img, (0, 0))
    pygame.display.flip()

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe (Pygame)")
    clock = pygame.time.Clock()

    draw_board(screen)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                idx = cell_from_mouse(event.pos)
                if idx != -1:
                    print(f"Clicked cell index: {idx}")  # 0..8

        # No need to redraw every frame yet; board is static for now.

    pygame.quit()

if __name__ == "__main__":
    main()
