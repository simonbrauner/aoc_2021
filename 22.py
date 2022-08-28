from dataclasses import dataclass


@dataclass
class Step:
    on: bool
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int

    def in_initialization_procedure(self) -> bool:
        return all(
            [
                abs(x) <= 50
                for x in [
                    self.min_x,
                    self.max_x,
                    self.min_y,
                    self.max_y,
                    self.min_z,
                    self.max_z,
                ]
            ]
        )


def read_range(line: str, coordinate: str) -> tuple[int, int]:
    split = line.split(f"{coordinate}=")[1].split(",")[0]
    left, right = split.split("..")

    return int(left), int(right)


with open("data.txt") as f:
    steps = []

    for line in f:
        line = line.replace("\n", ",")
        x = read_range(line, "x")
        y = read_range(line, "y")
        z = read_range(line, "z")
        steps.append(
            Step(line.split(" ")[0] == "on", x[0], x[1], y[0], y[1], z[0], z[1])
        )

    print([x for x in steps if x.in_initialization_procedure()])
