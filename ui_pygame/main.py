import pygame
from typing import Tuple

from pygame.examples.cursors import image

WIDTH, HEIGHT = 600, 600
CELL: int = WIDTH // 3
FPS: int = 60

SIGN_SHAPE_SIZE: tuple[int, int] = (90, 90)

FG: tuple[int, int, int] = (0, 0, 0)
LINE_WIDTH: int = 6

def cell_from_mouse(position: Tuple[int, int]) -> int:
    x, y = position
    column: int = x // CELL
    row: int = y // CELL
    if (0 <= row < 3) and (0 <= column < 3):
        return row * 3 + column
    return -1

def draw_board(screen: pygame.Surface) -> None:
    # Load and (optionally) scale your board image to fit the window
    board_img = pygame.image.load("img/GameBackground.jpg").convert()
    board_img = pygame.transform.smoothscale(board_img, (WIDTH, HEIGHT))
    screen.blit(board_img, (0, 0))
    pygame.display.flip()


def draw_sign(screen: pygame.Surface) -> None:
    # Load and (optionally) scale your board image to fit the window
    x_img = pygame.image.load("img/png_OShapeEarth.png").convert_alpha()
    x_img.set_colorkey((255, 255, 255))  # doesn't remove the white space around the picture
    x_img = pygame.transform.smoothscale(x_img, size=SIGN_SHAPE_SIZE)

    screen.blit(x_img, (0, 0))

    o_img = pygame.image.load("img/XShapeTree.png").convert()
    o_img = pygame.transform.smoothscale(o_img, size=SIGN_SHAPE_SIZE)
    screen.blit(o_img, (500, 200))

    pygame.display.flip()


def draw_line(screen: pygame.Surface) -> None:
    # pygame.draw.lines(screen, "black", False, (0.0, 200.0), 1)
    pygame.draw.line(screen, color=FG, start_pos=(CELL, 0), end_pos=(CELL, HEIGHT), width=LINE_WIDTH)
    pygame.draw.line(screen, color=FG, start_pos=(2 * CELL, 0), end_pos=(2 * CELL, HEIGHT), width=LINE_WIDTH)
    pygame.draw.line(screen, color=FG, start_pos=(0, CELL), end_pos=(WIDTH, CELL), width=LINE_WIDTH)
    pygame.draw.line(screen, color=FG, start_pos=(0, 2 * CELL), end_pos=(WIDTH, 2 * CELL), width=LINE_WIDTH)

    pygame.display.flip()


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe (Pygame)")
    clock = pygame.time.Clock()


    draw_board(screen)
    draw_sign(screen)
    draw_line(screen)

    running: bool = True
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
