from typing import Dict, List, Set
from collections import defaultdict


def path_count(data: Dict[str, List[str]], visited: Set[str], current: str) -> int:
    if current == "end":
        return 1

    visited.add(current)

    found = 0

    for cave in data[current]:
        if cave.isupper() or cave not in visited:
            found += path_count(data, visited, cave)

    visited.discard(current)

    return found


with open("data.txt") as f:
    data = defaultdict(list)

    for line in f:
        split = line.strip().split("-")
        data[split[0]].append(split[1])
        data[split[1]].append(split[0])

    print(path_count(data, set(), "start"))
