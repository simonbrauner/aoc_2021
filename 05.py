from collections import defaultdict


def pick_increment(left: int, right: int) -> int:
    if left == right:
        return 0
    elif left < right:
        return 1

    return -1


def overlapping_points(data: list[list[int]], horizontal_vertical: bool) -> int:
    vents: dict[tuple[int, int], int] = defaultdict(int)

    for point in data:
        left_x, left_y, right_x, right_y = point
        inc_x = pick_increment(left_x, right_x)
        inc_y = pick_increment(left_y, right_y)

        if horizontal_vertical and (inc_x != 0 and inc_y != 0):
            continue

        x = left_x
        y = left_y

        while True:
            vents[(x, y)] += 1

            if x == right_x and y == right_y:
                break

            x += inc_x
            y += inc_y

    return len([x for x in vents.values() if x >= 2])


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([int(x) for x in line.strip().replace(" -> ", ",").split(",")])

    print(overlapping_points(data, True))
    print(overlapping_points(data, False))
