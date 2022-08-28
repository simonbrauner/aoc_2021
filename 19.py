Coordinates = tuple[int, int, int]


def all_orientations(coordinates: Coordinates) -> set[Coordinates]:
    result = set()
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


with open("data.txt") as f:
    data: list[list[Coordinates]] = []
    scanner_index = 0

    while f.readline().strip() != "":
        data.append([])
        while (line := f.readline().strip()) != "":
            coordinates = [int(x) for x in line.split(",")]
            assert len(coordinates) == 3
            data[scanner_index].append((coordinates[0], coordinates[1], coordinates[2]))
        scanner_index += 1

    print(data)
