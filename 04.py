def remove_from_boards(number: int, boards: list[list[list[int]]]) -> None:
    for board in boards:
        for row in board:
            for x in range(5):
                if row[x] == number:
                    row[x] = -1


def board_won(board: list[list[int]]) -> bool:
    for i in range(5):
        if all([board[i][j] == -1 for j in range(5)]) or all(
            [board[j][i] == -1 for j in range(5)]
        ):
            return True

    return False


def board_sum(board: list[list[int]]) -> int:
    result = 0

    for row in board:
        for number in row:
            if number != -1:
                result += number

    return result


def play(
    draws: list[int],
    boards: list[list[list[int]]],
    first: bool,
) -> int:
    for drawn in draws:
        remove_from_boards(drawn, boards)

        won = [x for x in boards if board_won(x)]
        boards = [x for x in boards if not board_won(x)]

        if first and len(won) > 0:
            return board_sum(won[0]) * drawn

        if not first and len(boards) == 0:
            return board_sum(won[-1]) * drawn

    assert False


with open("data.txt") as f:
    draws = [int(x) for x in f.readline().split(",")]
    boards: list[list[list[int]]] = []

    while f.readline():
        board = []
        for y in range(5):
            board.append([int(x) for x in f.readline().split()])
        boards.append(board)

    print(play(draws, boards, True))
    print(play(draws, boards, False))
