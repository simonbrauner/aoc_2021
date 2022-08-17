def increment_all(data: list[list[int]]) -> None:
    for line in data:
        for x in range(len(line)):
            line[x] += 1


def increment_neighbors(x: int, y: int, data: list[list[int]]) -> None:
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            if (
                0 <= x + dx < len(data[0])
                and 0 <= y + dy < len(data)
                and data[y + dy][x + dx] != 0
            ):
                data[y + dy][x + dx] += 1


def flash(data: list[list[int]]) -> int:
    flashes = 0
    someone_flashed = True

    while someone_flashed:
        someone_flashed = False

        for x in range(len(data[0])):
            for y in range(len(data)):
                if data[y][x] > 9:
                    flashes += 1
                    someone_flashed = True
                    data[y][x] = 0
                    increment_neighbors(x, y, data)

    return flashes


def count_flashes(data: list[list[int]]) -> int:
    total_flashes = 0

    for step in range(100):
        increment_all(data)
        total_flashes += flash(data)

    return total_flashes


def all_flashes_turn(data: list[list[int]]) -> int:
    turn = 0

    while True:
        turn += 1

        increment_all(data)
        if flash(data) == len(data) * len(data[0]):
            return turn


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([int(x) for x in line.strip()])

    print(count_flashes([x[:] for x in data]))
    print(all_flashes_turn(data))
