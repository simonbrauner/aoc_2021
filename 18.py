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
        while True:
            if not self.explode():
                break

    def explode(self, depth: int = 1) -> bool:
        if depth == 5:
            assert (
                isinstance(self.left, int)
                and isinstance(self.right, int)
                and self.parent is not None
            )

            self.increment_left(self.left)
            self.increment_left(self.right)
            if self.is_left:
                self.parent.left = 0
            else:
                self.parent.right = 0

            return True

        return (isinstance(self.left, Pair) and self.left.explode(depth + 1)) or (
            isinstance(self.right, Pair) and self.right.explode(depth + 1)
        )

    def increment_left(self, value: int) -> None:
        pass

    def increment_right(self, value: int) -> None:
        pass

    def __add__(self, other: Pair) -> Pair:
        added = Pair(self, other)
        added.reduce()
        return added

    @staticmethod
    def add_all(pairs: list[Pair]) -> Pair:
        current = pairs[0]

        for other in pairs[1:]:
            current += other

        return current


with open("data.txt") as f:
    numbers = []

    for line in f:
        number = Pair.parse(line.strip())
        assert isinstance(number, Pair)
        numbers.append(number)

    print(Pair.add_all(numbers))
