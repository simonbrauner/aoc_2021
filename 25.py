def print_cucumbers(cucumbers: list[list[str]]) -> None:
    for y in range(len(cucumbers)):
        for x in range(len(cucumbers[0])):
            print(cucumbers[y][x], end="")
        print()


with open("data.txt") as f:
    data = []

    for line in f:
        data.append([x for x in line.strip()])

    print_cucumbers(data)
