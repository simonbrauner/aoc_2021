Image = list[list[int]]


def count_lit_pixels(image: list[list[int]]) -> int:
    return sum([x.count(1) for x in image])


def print_image(image: Image) -> None:
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def pixel_at_index(image: Image, x: int, y: int, default: int) -> int:
    if 0 <= x < len(image[0]) and 0 <= y < len(image):
        return image[y][x]

    return default


def enhanced_pixel(
    enhancement: list[int], image: Image, x: int, y: int, default: int
) -> int:
    index = 0

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            index *= 2
            index += pixel_at_index(image, x + dx, y + dy, default)

    return enhancement[index]


def enhance(enhancement: list[int], image: Image, times: int) -> Image:
    default = 0
    default_transformator = {0: enhancement[0], 1: enhancement[-1]}

    for _ in range(times):
        new_image = []

        for y in range(-1, len(image) + 1):
            new_row = []

            for x in range(-1, len(image[0]) + 1):
                new_row.append(enhanced_pixel(enhancement, image, x, y, default))

            new_image.append(new_row)

        image = new_image
        default = default_transformator[default]

    return image


with open("data.txt") as f:
    enhancement = []
    image = []

    while True:
        line = f.readline().strip()
        if line == "":
            break
        enhancement.extend([1 if x == "#" else 0 for x in line])

    while True:
        line = f.readline().strip()
        if line == "":
            break
        image.append([1 if x == "#" else 0 for x in line.strip()])

    print(count_lit_pixels(enhance(enhancement, image, 2)))
