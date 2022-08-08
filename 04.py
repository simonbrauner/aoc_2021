from typing import Dict, List, Optional, Tuple
from collections import defaultdict


def board_sum(boards: List[List[List[int]]], index: int) -> int:
    result = 0

    for row in boards[index]:
        for number in row:
            if number > 0:
                result += number

    return result


def board_won(
    boards: List[List[List[int]]],
    board: Tuple[int, int, int],
) -> bool:
    return all([boards[board[0]][board[1]][x] < 0 for x in range(5)]) or all(
        [boards[board[0]][y][board[2]] < 0 for y in range(5)]
    )


def draw_number(
    boards: List[List[List[int]]],
    positions: Dict[int, List[Tuple[int, int, int]]],
    drawn: int,
) -> Optional[int]:
    won: Optional[int] = None

    for board in positions[drawn]:
        boards[board[0]][board[1]][board[2]] = -1

        if board_won(boards, board) and won is None:
            won = board[0]

    return won


def play(
    draws: List[int],
    boards: List[List[List[int]]],
    positions: Dict[int, List[Tuple[int, int, int]]],
) -> int:
    for drawn in draws:
        draw_result = draw_number(boards, positions, drawn)

        if draw_result is not None:
            return board_sum(boards, draw_result) * drawn

    assert False


with open("data.txt") as f:
    draws = [int(x) for x in f.readline().split(",")]
    boards: List[List[List[int]]] = []
    positions: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)

    while f.readline():
        board = []
        for y in range(5):
            row = [int(x) for x in f.readline().split()]
            for x in range(5):
                positions[row[x]].append((len(boards), y, x))
            board.append(row)
        boards.append(board)

    print(play(draws, boards, positions))
