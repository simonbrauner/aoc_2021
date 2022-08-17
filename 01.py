def times_increased_shifted(shift: int, data: list[int]) -> int:
    result = 0

    for i in range(len(data) - shift):
        if data[i + shift] > data[i]:
            result += 1

    return result


with open("data.txt") as f:
    data = []

    for line in f:
        data.append(int(line))

    print(times_increased_shifted(1, data))
    print(times_increased_shifted(3, data))
