from typing import List


def is_lowest_point(x: int, y: int, data: List[List[int]]) -> bool:
    current = data[y][x]

    return all(
        [
            x == 0 or data[y][x - 1] > current,
            x == len(data[0]) - 1 or data[y][x + 1] > current,
            y == 0 or data[y - 1][x] > current,
            y == len(data) - 1 or data[y + 1][x] > current,
        ]
    )


def risk_level(data: List[List[int]]) -> int:
    result = 0

    for x in range(len(data[0])):
        for y in range(len(data)):
            if is_lowest_point(x, y, data):
                result += data[y][x] + 1

    return result


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([int(x) for x in line.strip()])

    print(risk_level(data))
