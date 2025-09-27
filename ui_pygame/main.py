import pygame



# ---------------------------- Constant Size ---------------------------- #
WIDTH, HEIGHT = 600, 600
CELL: int = WIDTH // 3
FPS: int = 60
LINE_WIDTH: int = 6

# ---------------------------- Color ---------------------------- #
BG = (255, 255, 255)
FG: tuple[int, int, int] = (0, 0, 0)




# ---------------------------- Game Board ---------------------------- #
def background(screen: pygame.Surface) -> None:
    """
    Uploading the game background
    :param screen: The argument must be pygame.Surface
    :return: None
    """

    # Load and (optionally) scale your board image to fit the window
    board_img = pygame.image.load("img/GameBackground.jpg").convert()
    board_img = pygame.transform.smoothscale(board_img, (WIDTH, HEIGHT))
    screen.blit(board_img, (0, 0))
    pygame.display.flip()


def draw_grid(screen: pygame.Surface) -> None:
    """
    Drawing the lines of game; it will print a big hashtag & Uploading the game background.
    :param screen: The argument must be pygame.Surface
    :return: None
    """

    background(screen)
    # vertical
    pygame.draw.line(screen, color=FG, start_pos=(CELL, 50), end_pos=(CELL, HEIGHT - 50), width=LINE_WIDTH)
    pygame.draw.line(screen, color=FG, start_pos=(2 * CELL, 50), end_pos=(2 * CELL, HEIGHT- 50), width=LINE_WIDTH)
    # horizontal
    pygame.draw.line(screen, color=FG, start_pos=(50, CELL), end_pos=(WIDTH - 50, CELL ), width=LINE_WIDTH)
    pygame.draw.line(screen, color=FG, start_pos=(50, 2 * CELL), end_pos=(WIDTH - 50, 2 * CELL), width=LINE_WIDTH)

    pygame.display.flip()


# ---------------------------- Game piece; "O" & "X" ---------------------------- #
def draw_sign_o(screen: pygame.Surface, idx: int) -> None:
    """
    This function will draw letter O
    :param screen: The argument must be pygame.Surface
    :param idx: This argument get an integer
    :return: None
    """

    row, column = divmod(idx, 3)
    cx: int = column * CELL + CELL // 2
    cy: int = row * CELL + CELL // 2
    radius: int = CELL // 3 - 30
    pygame.draw.circle(screen, FG, (cx, cy), radius, LINE_WIDTH)
    pygame.display.update()  # update the screen for this draw


def draw_sign_x(screen: pygame.Surface, idx: int) -> None:
    """
    This function will draw letter X
    :param screen: The argument must be pygame.Surface
    :param idx: This argument get an integer
    :return: None
    """
    row, column = divmod(idx, 3)
    x0: int = column * CELL
    y0: int = row * CELL
    pad: int = 30
    # two diagonals
    pygame.draw.line(screen, FG, (x0 + pad, y0 + pad), (x0 + CELL - pad, y0 + CELL - pad), LINE_WIDTH)
    pygame.draw.line(screen, FG, (x0 + pad, y0 + CELL - pad), (x0 + CELL - pad, y0 + pad), LINE_WIDTH)
    pygame.display.update()


# ---------------------------- Game Functions ---------------------------- #
def cell_from_mouse(position: tuple[int, int]) -> int:
    """
    This Function will translate the positions, which has two integer, to one integer. The output will be the index of
    game boarder. (From 0 to 8) It won't go beyond the eight and less than the zero
    :param position: Argument should be tuple which have two integer in it.
    :return: will return an integer
    """

    x, y = position
    column: int = x // CELL
    row: int = y // CELL
    if (0 <= row < 3) and (0 <= column < 3):
        return row * 3 + column
    return -1


# ---------------------------- Executing Game Functions ---------------------------- #
def main() -> None:
    """
    Just executing all functions here.
    :return: None
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe (Pygame)")
    clock = pygame.time.Clock()

    # draw the board ONCE; do not redraw every frame
    draw_grid(screen)

    # simple game state so marks persist visually
    board: list[str] = [" "] * 9
    turn: str = "X"  # alternate between X and O

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
                if idx != -1 and board[idx] == " ":
                    # draw once, do NOT redraw the grid afterward
                    if turn == "X":
                        draw_sign_x(screen, idx)
                        board[idx] = "X"
                        turn = "O"
                    else:
                        draw_sign_o(screen, idx)
                        board[idx] = "O"
                        turn = "X"
                    print(f"Clicked cell index: {idx}")
    pygame.quit()

if __name__ == "__main__":
    main()
