from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pair:
    left: int | Pair
    right: int | Pair

    @classmethod
    def parse(cls, raw: str) -> int | Pair:
        if raw.isnumeric():
            return int(raw)

        depth = -1

        for index, char in enumerate(raw):
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            elif depth == 0 and char == ",":
                return cls(Pair.parse(raw[1:index]), Pair.parse(raw[index + 1 : -1]))

        assert False


with open("data.txt") as f:
    numbers = []

    for line in f:
        numbers.append(Pair.parse(line.strip()))

    print(numbers)
