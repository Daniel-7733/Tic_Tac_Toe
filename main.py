# Imports like pygame

# Global variable
winning: bool = True

# TODO One: Make the Game Board
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

# TODO Two: Rules -> Suggestion: make three functions
    # TODO 1.1: (Win) Horizontally
def check_horizontally(game_board: list[str]) -> str:
    for row in range(0, 9, 3):  # Loop over 0, 3, 6 (start indices of rows)
        if game_board[row] == game_board[row + 1] == game_board[row + 2] != "   ":
            return f"Player {game_board[row].strip()} is the winner" # Return the winner (either 'X' or 'O')
    return "Tie"

    # TODO 1.1: (Win) Vertically
    # TODO 1.1: (Win) Diagonally

# TODO Three: function for player -> I need input ("X" and "O")
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


# TODO Four: Computer can play against human - Bot that randomly choose from 0 to 8 to fill the empty space
# TODO Five: Game function -> def game():
# TODO Six: Use pygame to make the graphic

def game()-> None:

    print("\nWelcome to Tic Tac Toe")

    game_board: list[str] = ["   ", "   ", "   ",
                             "   ", "   ", "   ",
                             "   ", "   ", "   "]

    game_board_maker(game_board)

    while True:
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
        check_horizontally(game_board)

    # add a part that ask if they want to continue the game after the game is finished
    # if game_over():
    #     print("Game Over! Restarting...")
    #     game_board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    #     game_board_maker(game_board)


if __name__ == "__main__":
    game()