from math import prod
from collections.abc import Callable


class Cuboid:
    def __init__(
        self,
        on: bool,
        min_x: float,
        max_x: float,
        min_y: float,
        max_y: float,
        min_z: float,
        max_z: float,
    ) -> None:
        self.on = on
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.min_z = min_z
        self.max_z = max_z

        for min_c, max_c in [(min_x, max_x), (min_y, max_y), (min_z, max_z)]:
            assert min_c <= max_c

    def __repr__(self) -> str:
        return (
            f'{"on" if self.on else "off"}'
            + f" x={self.min_x}..{self.max_x}"
            + f" y={self.min_y}..{self.max_y}"
            + f" z={self.min_z}..{self.max_z}"
        )

    def __hash__(self) -> int:
        return hash(
            (self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z)
        )

    @classmethod
    def universe(cls) -> "Cuboid":
        return cls(
            False,
            float("-inf"),
            float("inf"),
            float("-inf"),
            float("inf"),
            float("-inf"),
            float("inf"),
        )

    def cube_count(self) -> int:
        count = prod(
            [
                self.max_x - self.min_x + 1,
                self.max_y - self.min_y + 1,
                self.max_z - self.min_z + 1,
            ]
        )

        assert abs(count) != float("inf")
        return int(count)


def read_range(line: str, coordinate: str) -> tuple[int, int]:
    split = line.split(f"{coordinate}=")[1].split(",")[0]
    left, right = split.split("..")

    return int(left), int(right)


def in_initialization_procedure(step: Cuboid) -> bool:
    return all(
        [
            abs(x) <= 50
            for x in [
                step.min_x,
                step.max_x,
                step.min_y,
                step.max_y,
                step.min_z,
                step.max_z,
            ]
        ]
    )


def cubes_on_count(
    steps: list[Cuboid], step_filter: None | Callable[[Cuboid], bool] = None
) -> int:
    cuboids: set[Cuboid] = {Cuboid.universe()}
    print(cuboids)

    for step in filter(step_filter, steps):
        cuboids.add(step)

    return sum([x.cube_count() for x in cuboids if x.on])


with open("data.txt") as f:
    steps = []

    for line in f:
        line = line.replace("\n", ",")
        x = read_range(line, "x")
        y = read_range(line, "y")
        z = read_range(line, "z")
        steps.append(
            Cuboid(line.split(" ")[0] == "on", x[0], x[1], y[0], y[1], z[0], z[1])
        )

    print(cubes_on_count(steps, in_initialization_procedure))
