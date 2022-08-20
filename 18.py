from __future__ import annotations


class Pair:
    def __init__(self, left: int | Pair, right: int | Pair):
        self.left = left
        self.right = right
        self.parent = None
        self.is_left = True

        if isinstance(self.left, Pair):
            self.left.parent = self
        if isinstance(self.right, Pair):
            self.right.parent = self
            self.right.is_left = False

    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"

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

    def reduce(self) -> None:
        pass

    @staticmethod
    def add(pairs: list[Pair]) -> Pair:
        current = pairs[0]

        for other in pairs[1:]:
            current = Pair(current, other)
            current.reduce()

        return current


with open("data.txt") as f:
    numbers = []

    for line in f:
        number = Pair.parse(line.strip())
        assert isinstance(number, Pair)
        numbers.append(number)

    print(Pair.add(numbers[:2]))
