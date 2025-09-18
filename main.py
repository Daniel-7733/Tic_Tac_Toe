from players import HumanPlayer, RandomBot, SmartBot
from game import Game

def choose_symbol_once() -> str:
    while True:
        s = input("Choose your symbol (X/O): ").strip().upper()
        if s in ("X", "O"):
            return s
        print("Please type X or O.")

def choose_bot() -> str:
    while True:
        s = input("Choose bot: 1) Random  2) Smart → ").strip()
        if s in ("1", "2"):
            return s
        print("Please type 1 or 2.")

def main() -> None:
    print("1) Play vs Bot\n2) Two Players")
    mode = input("Select mode (1 or 2): ").strip()

    if mode == "1":
        human_symbol = choose_symbol_once()
        bot_type = choose_bot()
        bot_cls = SmartBot if bot_type == "2" else RandomBot

        if human_symbol == "X":
            game = Game(HumanPlayer("X", name="You"), bot_cls("O", name="Bot"))
        else:
            game = Game(bot_cls("X", name="Bot"), HumanPlayer("O", name="You"))

        print("\nBot will play when it's their turn.\n")
        game.play()

    else:
        print("\nTwo-player mode. X goes first.\n")
        game = Game(HumanPlayer("X", name="Player 1"),
                    HumanPlayer("O", name="Player 2"))
        game.play()

if __name__ == "__main__":
    main()
