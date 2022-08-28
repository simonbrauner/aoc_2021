from collections.abc import Callable
from collections import defaultdict


Coordinates = tuple[int, ...]


ORIENTATIONS: list[Callable[[Coordinates], Coordinates]] = [
    (lambda x: (x[0], x[1], x[2])),
    (lambda x: (x[0], x[2], -x[1])),
    (lambda x: (x[0], -x[1], -x[2])),
    (lambda x: (x[0], -x[2], x[1])),
    (lambda x: (-x[0], -x[1], x[2])),
    (lambda x: (-x[0], x[2], x[1])),
    (lambda x: (-x[0], x[1], -x[2])),
    (lambda x: (-x[0], -x[2], -x[1])),
    (lambda x: (x[1], x[2], x[0])),
    (lambda x: (x[1], x[0], -x[2])),
    (lambda x: (x[1], -x[2], -x[0])),
    (lambda x: (x[1], -x[0], x[2])),
    (lambda x: (-x[1], -x[2], x[0])),
    (lambda x: (-x[1], x[0], x[2])),
    (lambda x: (-x[1], x[2], -x[0])),
    (lambda x: (-x[1], -x[0], -x[2])),
    (lambda x: (x[2], x[0], x[1])),
    (lambda x: (x[2], x[1], -x[0])),
    (lambda x: (x[2], -x[0], -x[1])),
    (lambda x: (x[2], -x[1], x[0])),
    (lambda x: (-x[2], -x[0], x[1])),
    (lambda x: (-x[2], x[1], x[0])),
    (lambda x: (-x[2], x[0], -x[1])),
    (lambda x: (-x[2], -x[1], -x[0])),
]


def position_second_scanner_relative_to_first(
    first_beacon: Coordinates, second_beacon: Coordinates
) -> Coordinates:
    return tuple([first_beacon[x] - second_beacon[x] for x in range(len(first_beacon))])


def second_scanner_position(
    first_scanner: list[Coordinates], second_scanner: list[Coordinates]
) -> None | Coordinates:
    for orientation_index in range(len(ORIENTATIONS)):
        second_positions: defaultdict[Coordinates, int] = defaultdict(int)

        for first_beacon in first_scanner:
            for second_beacon in second_scanner:
                second_positions[
                    position_second_scanner_relative_to_first(
                        first_beacon, ORIENTATIONS[orientation_index](second_beacon)
                    )
                ] += 1

        with_enough_beacons = [x for x in second_positions if second_positions[x] >= 12]
        assert len(with_enough_beacons) <= 1

        if len(with_enough_beacons) == 1:
            return with_enough_beacons[0]

    return None


def scanner_positions(data: list[list[Coordinates]]) -> dict[int, Coordinates]:
    positions: dict[int, Coordinates] = {0: (0, 0, 0)}
    unprocessed = {0}

    while len(data) != len(positions):
        first_scanner = unprocessed.pop()
        for second_scanner in range(len(data)):
            if second_scanner not in positions:
                computed_position = second_scanner_position(
                    data[first_scanner], data[second_scanner]
                )
                if computed_position is not None:
                    positions[second_scanner] = computed_position
                    unprocessed.add(second_scanner)

    return positions


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

    print(scanner_positions(data))
