from random import choice
from time import sleep

def game_board_maker(game_board: list[str]) -> None:
    count: int = 1
    for i in game_board:
        if count % 3 == 0:
            print(i, end=" \n")
            if count != 9:
                print("--- | --- | ---")
        else:
            print(i, end=" | ")
        count += 1
    print()


def check_winner(board: list[str]) -> str | None:
    lines: list[tuple[int, int, int]] = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),      # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),      # cols
        (0, 4, 8), (2, 4, 6)                  # diagonals
    ]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] != "   ":
            return board[a].strip()  # "X" or "O"
    return None


def user() -> tuple[str,int] | None:
    """
    Prompts the user to choose a move for Tic Tac Toe by entering a number (1-9)
    and a symbol ('X' or 'O'). Validates the input and returns the symbol
    and the index in a tuple.

    Returns:
        tuple: A tuple containing the player's symbol ('X' or 'O')
               and the chosen index (0-8) for the move.
    """

    while True:
        x_player: str = input("Choose a number (1-9) then 'X' or 'O': (e.g. '1 X') --> ").strip()
        whole_part: list[str] = x_player.split()

        if len(whole_part) != 2:
            print("Invalid input. Please enter the move in the format: <number> <X or O>")
            continue  # Loop back to prompt the user again

        try:
            player_index: int = int(whole_part[0]) - 1
            player_sign: str = whole_part[1].upper()
        except ValueError:
            print("Invalid input. The first part must be a number between 1 and 9.")
            continue

        if player_sign not in ("X", "O"):
            print("Invalid symbol. Please choose either 'X' or 'O'.")
            continue

        if not (0 <= player_index <= 8):
            print("Invalid number. Please choose a number between 1 and 9.")
            continue

        return player_sign, player_index


def bot(board: list[str], user_choice: str) -> tuple[str, int] | None:
    """
    Pick a random empty index and return (bot_sign, bot_index).
    Returns None if there is no legal move.
    """
    empty_idxs: list[int] = [i for i, v in enumerate(board) if v == "   "]

    if not empty_idxs:
        return None

    bot_sign: str = "O" if user_choice == "X" else "X"
    bot_index:int = choice(empty_idxs)

    return bot_sign, bot_index



def game(game_board: list[str])-> None:

    game_board_maker(game_board)

    game_limit: int = 1
    while game_limit <= 9:
        full_info: tuple[str, int] = user()
        player_sign: str = full_info[0]
        player_index: int = full_info[1]

        # Ensure the position is empty before placing the mark
        if game_board[player_index] != "   ":
            print("That spot is already taken. Try again.")
            continue

        game_board[player_index] = f" {player_sign} "
        game_board_maker(game_board)

        # Add win check or tie check here
        winner = check_winner(game_board)
        if winner:
            print(f"Player {winner} is the winner!")
            break

        if "   " not in game_board:
            print("It's a tie!")
            break

    # add a part that ask if they want to continue the game after the game is finished
    # if game_over():
    #     print("Game Over! Restarting...")
    #     game_board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    #     game_board_maker(game_board)


def game_with_bot(game_board: list[str]) -> None:
    print("\nBot will play after you!\n")
    game_board_maker(game_board)

    while True:
        # --- Human move ---
        player_sign, player_index = user()

        if game_board[player_index] != "   ":
            print("That spot is already taken. Try again.")
            continue

        game_board[player_index] = f" {player_sign} "
        game_board_maker(game_board)

        # Check win/tie after human move
        winner: str | None = check_winner(game_board)
        if winner:
            print(f"Player {winner} is the winner!")
            break
        if "   " not in game_board:
            print("It's a tie!")
            break

        # --- Bot move ---
        bot_move = bot(game_board, player_sign)
        if bot_move is None:
            print("It's a tie!")
            break

        bot_sign, bot_index = bot_move
        game_board[bot_index] = f" {bot_sign} "

        sleep(0.5) #delay to answer

        print(f"Bot plays at {bot_index + 1} as {bot_sign}")
        game_board_maker(game_board)

        # Check win/tie after bot move
        winner: str | None  = check_winner(game_board)
        if winner:
            print(f"Player {winner} is the winner!")
            break
        if "   " not in game_board:
            print("It's a tie!")
            break

def main() -> None:
    print("\nWelcome to Tic Tac Toe")

    game_board: list[str] = ["   "] * 9


    try:
        user_choice: int = int(input("Write 1 if you want to play with bot otherwise 2: "))
    except ValueError:
        raise "Add number"
    if user_choice not in [1, 2]:
        print("write 1 or 2")

    if user_choice == 1:
        game_with_bot(game_board)
    else:
        game(game_board)

# TODO Six: Use pygame to make the graphic
if __name__ == "__main__":
    main()
