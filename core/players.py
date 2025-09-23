from __future__ import annotations
from typing import List, Tuple
from random import choice
from time import sleep

EMPTY: str = "   "


class Player:
    def __init__(self, symbol: str, name: str | None = None) -> None:
        self.symbol = symbol  # "X" or "O"
        self.name = name or symbol

    def is_bot(self) -> bool:
        return False

    def move(self, board: List[str]) -> int:
        raise NotImplementedError


class HumanPlayer(Player):
    def move(self, board: List[str]) -> int | None:
        while True:
            raw: str = input(f"{self.name} ({self.symbol}) — choose a number (1-9): ").strip()
            try:
                idx: int = int(raw) - 1
            except ValueError:
                print("Please enter a number 1–9.")
                continue

            if not (0 <= idx <= 8):
                print("Choose between 1 and 9.")
                continue

            if board[idx] != EMPTY:
                print("That spot is taken. Try again.")
                continue
            return idx


class RandomBot(Player):
    def is_bot(self) -> bool:
        return True

    def move(self, board: List[str]) -> int:
        sleep(0.4)
        empty: List[int] = [i for i, v in enumerate(board) if v == EMPTY]
        return choice(empty)


class SmartBot(Player):
    """
    Simple heuristic: win if possible, block if needed,
    then prefer center, corners, sides (not full Minimax).
    """
    def is_bot(self) -> bool:
        return True

    def move(self, board: List[str]) -> int:
        sleep(0.4)
        empty: List[int] = [i for i, v in enumerate(board) if v == EMPTY]

        # Helper to simulate a move
        def would_win(sym: str, idx: int) -> bool:
            tmp: List[str] = board[:]
            tmp[idx] = f" {sym} "
            return _winner(tmp) == sym

        # 1) Win
        for i in empty:
            if would_win(self.symbol, i):
                return i

        # 2) Block
        opp: str = "O" if self.symbol == "X" else "X"
        for i in empty:
            if would_win(opp, i):
                return i

        # 3) Center -> corners -> sides
        for pref in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if pref in empty:
                return pref

        # Fallback (shouldn’t happen)
        return empty[0]


# winner helper (duplicated tiny utility so SmartBot can “peek”)
WIN_LINES: List[Tuple[int, int, int]] = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def _winner(board: List[str]) -> str | None:
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a].strip()
    return None
