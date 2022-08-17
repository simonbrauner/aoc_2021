def final_position(data: list[tuple[str, int]], with_aim: bool) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for command in data:
        direction, units = command

        if direction == "forward":
            horizontal += units

            if with_aim:
                depth += aim * units
        else:
            if direction == "up":
                units *= -1

            if with_aim:
                aim += units
            else:
                depth += units

    return horizontal * depth


with open("data.txt") as f:
    data = []

    for line in f:
        split = line.split(" ")
        data.append((split[0], int(split[1])))

    print(final_position(data, False))
    print(final_position(data, True))
