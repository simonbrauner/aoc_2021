from dataclasses import dataclass


MAGIC_CONSTANT = 500


@dataclass
class Area:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def __contains__(self, item: tuple[int, int]) -> bool:
        return self.min_x <= item[0] <= self.max_x and self.min_y <= item[1] <= self.max_y


def highest_y_position(area: Area, vx: int, vy: int) -> int:
    x = 0
    y = 0
    highest_y = 0
    was_in_area = False

    while x <= area.max_x and y >= area.min_y:
        x += vx
        y += vy
        vx = max(vx - 1, 0)
        vy -= 1

        if y > highest_y:
            highest_y = y

        if (x, y) in area:
            was_in_area = True

    return highest_y if was_in_area else 0


def total_highest_y_position(area: Area) -> int:
    result = 0

    for vx in range(area.max_x + 1):
        for vy in range(MAGIC_CONSTANT):
            current = highest_y_position(area, vx, vy)
            if current > result:
                result = current

    return result


with open("data.txt") as f:
    line = f.readline().strip()
    min_x, max_x = map(int, line.split("x=")[1].split(",")[0].split(".."))
    min_y, max_y = map(int, line.split("y=")[1].split(".."))
    area = Area(min_x, max_x, min_y, max_y)

    print(total_highest_y_position(area))
