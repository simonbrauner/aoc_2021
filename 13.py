from typing import List, Tuple


def create_paper(dots: List[Tuple[int, int]]) -> List[List[str]]:
    paper = []

    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])

    for y in range(max_y + 1):
        paper.append(["." for x in range(max_x + 1)])

    for dot in dots:
        x, y = dot

        paper[y][x] = "#"

    return paper


def print_paper(paper: List[List[str]]) -> None:
    for line in paper:
        for char in line:
            print(char, end="")
        print()


def create_instruction(raw_instructions: str) -> Tuple[str, int]:
    pass


def fold(paper: List[List[str]], instruction: Tuple[str, int]) -> None:
    pass


def first_fold_dot_count(paper: List[List[str]], instructions: List[Tuple[str, int]]) -> int:
    result = 0

    fold(paper, instructions[-1])

    for line in paper:
        for char in line:
            if char == "#":
                result += 1

    return result


with open("data.txt") as f:
    dots = []
    instructions = []

    while True:
        line = f.readline().strip()
        if line == "":
            break
        split = line.split(",")
        dots.append((int(split[0]), int(split[1])))

    while True:
        line = f.readline().strip()
        if line == "":
            break
        instructions.append(create_instruction(line))

    # print(first_fold_dot_count(create_paper(dots), instructions))
    print_paper(create_paper(dots))
