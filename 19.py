from collections import defaultdict


Coordinates = tuple[int, ...]


def all_orientations(coordinates: Coordinates) -> set[Coordinates]:
    result: set[Coordinates] = set()
    x, y, z = coordinates

    for _ in range(3):
        result.add((x, y, z))
        result.add((x, z, -y))
        result.add((x, -y, -z))
        result.add((x, -z, y))
        result.add((-x, -y, z))
        result.add((-x, z, y))
        result.add((-x, y, -z))
        result.add((-x, -z, -y))

        x, y, z = y, z, x

    return result


def position_second_scanner_relative_to_first(
    first_beacon: Coordinates, second_beacon: Coordinates
) -> Coordinates:
    return tuple([first_beacon[x] - second_beacon[x] for x in range(len(first_beacon))])


def second_scanner_position(
    first_scanner: list[Coordinates], second_scanner: list[Coordinates]
) -> None | Coordinates:
    second_positions: defaultdict[Coordinates, int] = defaultdict(int)

    for first_beacon in first_scanner:
        for second_beacon in second_scanner:
            for second_oriented in all_orientations(second_beacon):
                second_positions[
                    position_second_scanner_relative_to_first(
                        first_beacon, second_oriented
                    )
                ] += 1

    with_enough_beacons = [x for x in second_positions if second_positions[x] >= 12]
    assert len(with_enough_beacons) <= 1

    if len(with_enough_beacons) == 1:
        return with_enough_beacons[0]

    return None


with open("data.txt") as f:
    data: list[list[Coordinates]] = []
    scanner_index = 0

    while f.readline().strip() != "":
        data.append([])
        while (line := f.readline().strip()) != "":
            coordinates = [int(x) for x in line.split(",")]
            assert len(coordinates) == 3
            data[scanner_index].append(tuple(coordinates))
        scanner_index += 1

    print(second_scanner_position(data[0], data[1]))
