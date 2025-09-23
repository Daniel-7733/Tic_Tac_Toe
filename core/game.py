from __future__ import annotations
from typing import List, Tuple, Optional
from core.players import Player, EMPTY

WIN_LINES: List[Tuple[int, int, int]] = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


class Game:
    def __init__(self, player_x: Player, player_o: Player) -> None:
        self.board: List[str] = [EMPTY] * 9
        self.player_x = player_x
        self.player_o = player_o
        self.current: Player = player_x  # X always starts

    # ---------- Rules ----------
    def winner(self) -> Optional[str]:
        for a, b, c in WIN_LINES:
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a].strip()
        return None

    def full(self) -> bool:
        return EMPTY not in self.board

    # ---------- UI ----------
    def render(self) -> None:
        for i in range(9):
            end: str = " | " if (i % 3) != 2 else " \n"
            print(self.board[i], end=end)
            if (i % 3) == 2 and i != 8:
                print("--- | --- | ---")
        print()

    # ---------- Loop ----------
    def play(self) -> None:
        print("\nWelcome to Tic Tac Toe")
        self.render()
        while True:
            idx: int = self.current.move(self.board)
            self.board[idx] = f" {self.current.symbol} "

            if self.current.is_bot():
                print(f"{self.current.name} plays at {idx + 1}")

            self.render()

            win: str = self.winner()
            if win:
                print(f"Player {win} wins!")
                break
            if self.full():
                print("It's a tie!")
                break

            self.current: Player = self.player_o if self.current is self.player_x else self.player_x
