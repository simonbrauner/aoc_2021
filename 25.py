Cucumbers = list[list[str]]


def print_cucumbers(cucumbers: Cucumbers) -> None:
    for y in range(len(cucumbers)):
        for x in range(len(cucumbers[0])):
            print(cucumbers[y][x], end="")
        print()
    print()


def do_step(cucumbers: Cucumbers) -> bool:
    moved = False
    newly_occupied = set()

    first_col = [x[0] for x in cucumbers]
    for y in range(len(cucumbers)):
        for x in range(len(cucumbers[0])):
            next_x = (x + 1) % len(cucumbers[0])
            if (cucumbers[y][x] == ">" and cucumbers[y][next_x] == ".") and (
                (x, y) not in newly_occupied and (next_x != 0 or first_col[y] == ".")
            ):
                cucumbers[y][x], cucumbers[y][next_x] = (
                    cucumbers[y][next_x],
                    cucumbers[y][x],
                )
                newly_occupied.add((next_x, y))
                moved = True

    first_row = cucumbers[0].copy()
    for y in range(len(cucumbers)):
        for x in range(len(cucumbers[0])):
            next_y = (y + 1) % len(cucumbers)
            if (cucumbers[y][x] == "v" and cucumbers[next_y][x] == ".") and (
                (x, y) not in newly_occupied and (next_y != 0 or first_row[x] == ".")
            ):
                cucumbers[y][x], cucumbers[next_y][x] = (
                    cucumbers[next_y][x],
                    cucumbers[y][x],
                )
                newly_occupied.add((x, next_y))
                moved = True

    return moved


def stop_moving_step(cucumbers: Cucumbers) -> int:
    step_number = 1

    while do_step(cucumbers):
        step_number += 1

    return step_number


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([x for x in line.strip()])

    print(stop_moving_step(data))
