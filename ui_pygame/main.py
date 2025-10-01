import pygame
from core.game import WIN_LINES
from button import Button

# ---------------------------- Constant Size ---------------------------- #
WIDTH, HEIGHT = 600, 600
MARGIN: int = 50
INNER = WIDTH - 2 * MARGIN  # space for header/footer
CELL: int = (WIDTH - (2 * MARGIN)) // 3  # Now each square is smaller (166 instead of 200)
FPS: int = 60
LINE_WIDTH: int = 6
# ---------------------------- Constant Space ---------------------------- #
EMPTY_SPACE: str = " "
# ---------------------------- Color ---------------------------- #
BG = (255, 255, 255)
FG: tuple[int, int, int] = (0, 0, 0)
BG_PICTURE: str = "img/GameBackground.jpg"
BG_FOREST_PICTURE: str = "img/forestBackground.jpg"


# ---------------------------- Game Board ---------------------------- #
def background(screen: pygame.Surface) -> None:
    """
    Uploading the game background
    :param screen: The argument must be pygame.Surface
    :return: None
    """

    # Load and (optionally) scale your board image to fit the window
    board_img = pygame.image.load(BG_PICTURE).convert()
    board_img = pygame.transform.smoothscale(board_img, (WIDTH, HEIGHT))
    screen.blit(board_img, (0, 0))
    pygame.display.flip()


# positions for the grid lines (robust even if INNER isn't divisible by 3)
def edge(k: int) -> int:
    """
    Compute the pixel position of a vertical or horizontal grid edge.

    The board is drawn inside an inner square (WIDTH - 2*MARGIN).
    This function divides that inner square evenly into 3 parts
    and returns the pixel coordinate of the k-th edge.

    Example:
        edge(0) → left/top margin
        edge(1) → first grid line
        edge(2) → second grid line
        edge(3) → right/bottom margin

    :param k: Index of the edge (0 through 3).
    :return: The pixel coordinate (x or y) of that edge.
    """
    # k = 0..3 → returns pixel positions of inner edges
    # round() avoids accumulating truncation when INNER % 3 != 0
    return MARGIN + round(k * INNER / 3)


def cell_rect(idx: int) -> pygame.Rect:
    """
    Compute the rectangular area of a specific cell on the board.

    The board is a 3×3 grid, stored in a flat list of 9 cells (index 0..8).
    This function converts the 1D index into a (row, col) position and
    returns a pygame.Rect describing the pixel bounds of that cell.

    Example:
        idx=0 → top-left cell
        idx=4 → center cell
        idx=8 → bottom-right cell

    :param idx: Cell index from 0 to 8.
    :return: pygame.Rect covering the cell's pixel boundaries.
    """
    
    r, c = divmod(idx, 3)
    left, right = edge(c), edge(c + 1)
    top, bottom = edge(r), edge(r + 1)
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
    radius: int = min(rect.width, rect.height) // 2 - 14  # padding from cell edges
    pygame.draw.circle(screen, FG, (cx, cy), radius, LINE_WIDTH)
    pygame.display.update(rect)  # update the screen for this draw


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
                     (rect.left + pad, rect.top + pad),
                     (rect.right - pad, rect.bottom - pad), LINE_WIDTH)
    pygame.draw.line(screen, FG,
                     (rect.left + pad, rect.bottom - pad),
                     (rect.right - pad, rect.top + pad), LINE_WIDTH)
    pygame.display.update(rect)


# ---------------------------- Game Functions & Rules ---------------------------- #
def cell_from_mouse(position: tuple[int, int]) -> int:
    """
    This function try to find the correct position of each cell from the mouse click position
    and will give a single number which from 0 to 8. This number will be the position of player choice.

    :param position: This argument will receive a tuple of x and y which is the coordination of mouse click.
    :return: It will return an integer from 0 to 8.
    """

    x, y = position
    # Use the inner square edges so clicks align with the grid
    if not (edge(0) <= x <= edge(3) and edge(0) <= y <= edge(3)):
        return -1
    col: int = min(2, ((x - edge(0)) * 3) // (edge(3) - edge(0)))
    row: int = min(2, ((y - edge(0)) * 3) // (edge(3) - edge(0)))
    return row * 3 + col


def winner(game_board: list[str]) -> str | None:
    """
    Declare the winner. This function tries to find the winning player
    by checking vertically, horizontally, and diagonally.

    :param game_board: This should be the game board
    :return: Will return string: X or O. If neither of them match with the rule, it will return none.
    """

    for a, b, c in WIN_LINES:
        if game_board[a] == game_board[b] == game_board[c] != EMPTY_SPACE:
            return game_board[a].strip()
    return None


def draw_status(screen: pygame.Surface, font: pygame.font.Font, text: str) -> None:
    # re-blit the background in the header area
    header_rect = pygame.Rect(0, 0, WIDTH, MARGIN)
    screen.blit(pygame.transform.smoothscale(
        pygame.image.load(BG_PICTURE).convert(), (WIDTH, HEIGHT)
    ), (0, 0), header_rect)

    # render text with transparent background
    text_surface = font.render(text, False, FG, None)
    screen.blit(text_surface, (MARGIN, 10))
    pygame.display.update(header_rect)


def restart_game(screen: pygame.Surface, font: pygame.font.Font) -> tuple[list[str], str, bool]:
    """
    This Function will restart the board, turn, game_over; a fresh start.

    :param screen: The argument must be pygame.Surface
    :param font: The argument must be pygame.font.Font
    :return: Will return tuple of list of strings, string, boolean values.
    """
    draw_grid(screen)
    draw_status(screen, font, "Turn: X")
    return [EMPTY_SPACE] * 9, "X", False  # board, turn, game_over


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe (Pygame)")
    clock = pygame.time.Clock()
    font = pygame.font.Font(r"font\Pixeltype.ttf", 50)

    btn_width, btn_height = 150, 40
    btn_x: int = WIDTH - btn_width - MARGIN  # push to right edge, with some margin
    btn_y: int = 8  # near the top

    btn: Button = Button(
        screen=screen,
        rect=(btn_x, btn_y, btn_width, btn_height),
        text="Restart",
        font=font,
        fill=(245, 245, 245),
        text_color=(0, 0, 0),
        border_color=(0, 0, 0),
        border_width=2,
    )

    # initial draw
    board, turn, game_over = restart_game(screen, font)

    running: bool = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            # --- Button events ---
            if btn.handle_event(event):
                # Restart clicked
                board, turn, game_over = restart_game(screen, font)

            # --- Mouse click on board ---
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                idx: int = cell_from_mouse(event.pos)
                if idx != -1 and board[idx] == " ":
                    if turn == "X":
                        draw_sign_x(screen, idx)
                        board[idx] = "X"
                        turn = "O"
                    else:
                        draw_sign_o(screen, idx)
                        board[idx] = "O"
                        turn = "X"

                    # winner / tie check immediately after move
                    w: str | None = winner(board)
                    if w:
                        draw_status(screen, font, f"Winner: {w}")
                        game_over = True
                    elif " " not in board:
                        draw_status(screen, font, "It's a tie!")
                        game_over = True
                    else:
                        draw_status(screen, font, f"Turn: {turn}")

        # Draw the button every frame so hover state is visible and it stays on top
        btn.draw()

    pygame.quit()


if __name__ == "__main__":
    main()
