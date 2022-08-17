from collections import defaultdict


def path_count(
    data: dict[str, list[str]], visited: set[str], current: str, one_twice: bool
) -> int:
    if current == "end":
        return 1

    should_be_discarded = current not in visited
    visited.add(current)

    found = 0

    for cave in data[current]:
        if cave.isupper() or cave not in visited:
            found += path_count(data, visited, cave, one_twice)
        elif one_twice and cave != "start":
            found += path_count(data, visited, cave, False)

    if should_be_discarded:
        visited.discard(current)

    return found


with open("data.txt") as f:
    data = defaultdict(list)

    for line in f:
        split = line.strip().split("-")
        data[split[0]].append(split[1])
        data[split[1]].append(split[0])

    print(path_count(data, set(), "start", False))
    print(path_count(data, set(), "start", True))
