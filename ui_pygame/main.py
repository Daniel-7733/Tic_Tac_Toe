import pygame
from core.game import WIN_LINES



# ---------------------------- Constant Size ---------------------------- #
WIDTH, HEIGHT = 600, 600
MARGIN: int = 50
INNER = WIDTH - 2 * MARGIN  # space for header/footer
CELL: int = (WIDTH - (2 * MARGIN)) // 3 # Now each square is smaller (166 instead of 200)
FPS: int = 60
LINE_WIDTH: int = 6
# ---------------------------- Constant Space ---------------------------- #
EMPTY_SPACE: str = " "
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

# positions for the grid lines (robust even if INNER isn't divisible by 3)
def edge(k: int) -> int:
    # k = 0..3 → returns pixel positions of inner edges
    # round() avoids accumulating truncation when INNER % 3 != 0
    return MARGIN + round(k * INNER / 3)

def cell_rect(idx: int) -> pygame.Rect:
    r, c = divmod(idx, 3)
    left, right = edge(c), edge(c + 1)
    top,  bottom = edge(r), edge(r + 1)
    return pygame.Rect(left, top, right - left, bottom - top)


def draw_grid(screen: pygame.Surface) -> None:
    """
    Drawing the lines of game; it will print a big hashtag & Uploading the game background.
    :param screen: The argument must be pygame.Surface
    :return: None
    """

    background(screen)
    # vertical
    # background first (if any), then the grid
    # verticals
    pygame.draw.line(screen, FG, (edge(1), edge(0)), (edge(1), edge(3)), LINE_WIDTH)
    pygame.draw.line(screen, FG, (edge(2), edge(0)), (edge(2), edge(3)), LINE_WIDTH)
    # horizontals
    pygame.draw.line(screen, FG, (edge(0), edge(1)), (edge(3), edge(1)), LINE_WIDTH)
    pygame.draw.line(screen, FG, (edge(0), edge(2)), (edge(3), edge(2)), LINE_WIDTH)
    pygame.display.flip()


# ---------------------------- Game piece; "O" & "X" ---------------------------- #
def draw_sign_o(screen: pygame.Surface, idx: int) -> None:
    """
    This function will draw letter O
    :param screen: The argument must be pygame.Surface
    :param idx: This argument get an integer
    :return: None
    """

    rect = cell_rect(idx)
    cx, cy = rect.center
    radius: int = min(rect.width, rect.height) // 2 - 14   # padding from cell edges
    pygame.draw.circle(screen, FG, (cx, cy), radius, LINE_WIDTH)
    pygame.display.update(rect) # update the screen for this draw


def draw_sign_x(screen: pygame.Surface, idx: int) -> None:
    """
    This function will draw letter X
    :param screen: The argument must be pygame.Surface
    :param idx: This argument get an integer
    :return: None
    """

    rect = cell_rect(idx)
    pad: int = 18  # padding so lines don’t touch the borders
    pygame.draw.line(screen, FG,
                     (rect.left + pad,  rect.top + pad),
                     (rect.right - pad, rect.bottom - pad), LINE_WIDTH)
    pygame.draw.line(screen, FG,
                     (rect.left + pad,  rect.bottom - pad),
                     (rect.right - pad, rect.top + pad), LINE_WIDTH)
    pygame.display.update(rect)


# ---------------------------- Game Functions & Rules ---------------------------- #
def cell_from_mouse(position: tuple[int, int]) -> int:
    """
    This Function will translate the positions, which has two integer, to one integer. The output will be the index of
    game boarder. (From 0 to 8) It won't go beyond the eight and less than the zero
    :param position: Argument should be tuple which have two integer in it.
    :return: will return an integer
    """

    x, y = position
    if not (MARGIN <= x <= WIDTH - MARGIN) and (MARGIN <= y <= HEIGHT - MARGIN):
        return -1

    column: int = min(2, ((x - edge(0)) * 3) // (edge(3) - edge(0)))
    row: int = min(2, ((y - edge(0)) * 3) // (edge(3) - edge(0)))
    return row * 3 + column

def winner(game_board: list[str]) -> str | None: # It doesn't work
    for a, b, c in WIN_LINES:
        if game_board[a] == game_board[b] == game_board[c] != EMPTY_SPACE:
            return game_board[a].strip()
    return None

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
    board: list[str] = [EMPTY_SPACE] * 9
    turn: str = "X"  # alternate between X and O

    running: bool = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                idx: int = cell_from_mouse(event.pos)
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

                # ---------- Check the winner or tie ---------- #
                win: str | None = winner(board)
                if win: # this one declare winner: X or O
                    print(f"{win} win!")
                    running = False

                if EMPTY_SPACE not in board: # This one declare tie
                    print("It's a tie!")
                    running = False
                    continue

    pygame.quit()

if __name__ == "__main__":
    main()
