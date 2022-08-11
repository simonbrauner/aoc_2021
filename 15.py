from typing import List, Set, Union, Tuple
from heapq import heappop, heappush


def neighbors(vertex: int, row_length: int, col_length: int) -> Set[int]:
    possible_neighbors = {
        vertex + x
        for x in [-1, 1, -row_length, row_length]
        if 0 <= vertex + x < row_length * col_length
    }

    if vertex % row_length == row_length - 1:
        possible_neighbors.discard(vertex + 1)
    elif vertex % row_length == 0:
        possible_neighbors.discard(vertex - 1)

    return possible_neighbors


def relax(
    total_risks: List[Union[float, int]], risks: List[int], left: int, right: int
) -> bool:
    new_distance = total_risks[left] + risks[right]

    if new_distance < total_risks[right]:
        total_risks[right] = new_distance
        return True

    return False


def lowest_total_risk(
    risks: List[int], row_length: int, col_length: int
) -> Union[float, int]:
    total_risks = [float("inf") for _ in range(len(risks))]
    total_risks[0] = 0
    done = [False for _ in range(len(risks))]
    priority_queue: List[Tuple[Union[float, int], int]] = [(0, 0)]

    while priority_queue:
        _, current = heappop(priority_queue)

        if done[current]:
            continue

        done[current] = True

        for neighbor in neighbors(current, row_length, col_length):
            if not done[neighbor] and relax(total_risks, risks, current, neighbor):
                heappush(priority_queue, ((total_risks[neighbor], neighbor)))

    return total_risks[-1]


def new_risk(number: int, tile: int) -> int:
    added = number + tile
    if added < 10:
        return added % 10
    else:
        return (added + 1) % 10


def extended_data(risks: List[int], row_length: int, col_length: int) -> List[int]:
    result = []
    index = 0

    for col_index in range(col_length):
        row = []

        for row_index in range(row_length):
            row.append(risks[index])
            index += 1

        for tile in range(5):
            for number in row:
                result.append(new_risk(number, tile))

    for tile in range(1, 5):
        for number in result[: row_length * col_length * 5]:
            result.append(new_risk(number, tile))

    return result


with open("data.txt") as f:
    risks = []
    col_length = 0

    for line in f:
        col_length += 1
        for char in line.strip():
            risks.append(int(char))

    row_length = len(risks) // col_length
    longer_risks = extended_data(risks, row_length, col_length)

    print(lowest_total_risk(risks, row_length, col_length))
    print(lowest_total_risk(longer_risks, row_length * 5, col_length * 5))
