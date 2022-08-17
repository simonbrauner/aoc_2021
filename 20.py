def count_lit_pixels(image: list[list[int]]) -> int:
    return sum([x.count(1) for x in image])


with open("data.txt") as f:
    enhancement = [1 if x == "#" else 0 for x in f.readline().strip()]
    f.readline()
    image = []

    while True:
        line = f.readline().strip()
        if line == "":
            break
        image.append([1 if x == "#" else 0 for x in line.strip()])

    print(count_lit_pixels(image))
