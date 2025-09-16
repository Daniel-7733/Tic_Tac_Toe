# Imports like pygame

# Global variable
winning: bool = True

# TODO One: Make the Game Board
def gameboard() -> None:
    game_board: list[str] = ["_", "_", "_",
                             "_", "_", "_",
                             "_", "_", "_",]

    count: int = 3
    for i in game_board:
        if count % 3 == 0:
            print()
        print(i, end="  ")
        count += 1
    print()

# TODO Two: Rules -> Suggestion: make three functions
    # TODO 1.1: (Win) Horizontally
    # TODO 1.1: (Win) Vertically
    # TODO 1.1: (Win) Diagonally

# TODO Three: function for player -> I need input ("X" and "O")
# TODO Four: Computer can play against human - Bot that randomly choose from 0 to 8 to fill the empty space
# TODO Five: Game function -> def game():
# TODO Six: Use pygame to make the graphic

def main()-> None:
    gameboard()

if __name__ == "__main__":
    main()