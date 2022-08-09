from typing import List, Union
from collections import Counter


def fuel_consumption(first: int, second: int, constant_rate: bool) -> int:
    distance = abs(first - second)

    if constant_rate:
        return distance

    return (distance * (1 + distance)) // 2


def minimal_fuel(data: List[int], constant_rate: bool) -> Union[float, int]:
    result = float("inf")
    counter = Counter(data)

    for horizontal in range(min(data), max(data) + 1):
        consumption = sum(
            [
                counter[x] * fuel_consumption(horizontal, x, constant_rate)
                for x in counter
            ]
        )

        if consumption < result:
            result = consumption

    return result


with open("data.txt") as f:
    data = [int(x) for x in f.readline().split(",")]

    print(minimal_fuel(data, True))
    print(minimal_fuel(data, False))
