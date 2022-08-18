from dataclasses import dataclass


MAGIC_CONSTANT = 500


@dataclass
class Area:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def __contains__(self, item: tuple[int, int]) -> bool:
        return (
            self.min_x <= item[0] <= self.max_x and self.min_y <= item[1] <= self.max_y
        )


def reaches_area(area: Area, vx: int, vy: int) -> bool:
    x = 0
    y = 0

    while x <= area.max_x and y >= area.min_y:
        x += vx
        y += vy
        vx = max(vx - 1, 0)
        vy -= 1

        if (x, y) in area:
            return True

    return False


def positions_to_reach_area(area: Area) -> list[tuple[int, int]]:
    positions = []

    for vx in range(area.max_x + 1):
        for vy in range(area.min_y, MAGIC_CONSTANT):
            if reaches_area(area, vx, vy):
                positions.append((vx, vy))

    return positions


def probe_calculations(area: Area) -> None:
    positions = positions_to_reach_area(area)
    print(sum(range(max(positions, key=lambda x: x[1])[1] + 1)))
    print(len(positions))


with open("data.txt") as f:
    line = f.readline().strip()
    min_x, max_x = map(int, line.split("x=")[1].split(",")[0].split(".."))
    min_y, max_y = map(int, line.split("y=")[1].split(".."))

    area = Area(min_x, max_x, min_y, max_y)
    probe_calculations(area)
