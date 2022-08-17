from math import prod


def is_lowest_point(x: int, y: int, data: list[list[int]]) -> bool:
    current = data[y][x]

    return all(
        [
            x == 0 or data[y][x - 1] > current,
            x == len(data[0]) - 1 or data[y][x + 1] > current,
            y == 0 or data[y - 1][x] > current,
            y == len(data) - 1 or data[y + 1][x] > current,
        ]
    )


def risk_level(data: list[list[int]]) -> int:
    result = 0

    for x in range(len(data[0])):
        for y in range(len(data)):
            if is_lowest_point(x, y, data):
                result += data[y][x] + 1

    return result


def basin_size(x: int, y: int, data: list[list[int]]) -> int:
    result = 1
    data[y][x] = 9

    if x != 0 and data[y][x - 1] != 9:
        result += basin_size(x - 1, y, data)
    if x != len(data[0]) - 1 and data[y][x + 1] != 9:
        result += basin_size(x + 1, y, data)
    if y != 0 and data[y - 1][x] != 9:
        result += basin_size(x, y - 1, data)
    if y != len(data) - 1 and data[y + 1][x] != 9:
        result += basin_size(x, y + 1, data)

    return result


def basin_size_product(data: list[list[int]]) -> int:
    sizes = []

    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] != 9:
                sizes.append(basin_size(x, y, data))

    sizes.sort()
    return prod(sizes[-3:])


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([int(x) for x in line.strip()])

    print(risk_level(data))
    print(basin_size_product(data))
