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
) -> List[Optional[int]]:
    won: List[Optional[int]] = [None]

    for board in positions[drawn]:
        boards[board[0]][board[1]][board[2]] = -1

        if board_won(boards, board):
            if won[0] is None:
                won[0] = board[0]
            else:
                won.append(board[0])

    return won


def play(
    draws: List[int],
    boards: List[List[List[int]]],
    positions: Dict[int, List[Tuple[int, int, int]]],
    first: bool,
) -> int:
    won_already = []

    for drawn in draws:
        draw_result = draw_number(boards, positions, drawn)

        if first and draw_result[0] is not None:
            return board_sum(boards, draw_result[0]) * drawn

        won_already.extend([x for x in draw_result if x is not None])
        for key in positions.keys():
            positions[key] = [x for x in positions[key] if x[0] not in draw_result]

        if len(won_already) == len(boards):
            return board_sum(boards, won_already[-1]) * drawn

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

    print(play(draws, boards, positions, True))
    print(play(draws, boards, positions, False))
