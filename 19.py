def all_orientations(x: int, y: int, z: int) -> set[tuple[int, int, int]]:
    result = set()

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
