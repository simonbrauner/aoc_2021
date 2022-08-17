from collections import Counter


def next_fish(fish: list[int]) -> list[int]:
    result = [0 for _ in range(9)]

    for index in range(8):
        result[index] = fish[index + 1]

    result[6] += fish[0]
    result[8] += fish[0]

    return result


def fish_after_days(data: list[int], days: int) -> int:
    counter = Counter(data)
    fish = [counter[x] for x in range(9)]

    for _ in range(days):
        fish = next_fish(fish)

    return sum(fish)


with open("data.txt") as f:
    data = [int(x) for x in f.readline().split(",")]

    print(fish_after_days(data, 80))
    print(fish_after_days(data, 256))
