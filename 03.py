from typing import List


def most_common_bit(data: List[str], index: int) -> str:
    if len([x for x in data if x[index] == "1"]) >= len(data) / 2:
        return "1"

    return "0"


def gamma_epsilon(data: List[str]) -> int:
    gamma = 0
    epsilon = 0

    for index in range(len(data[0])):
        mcb = most_common_bit(data, index)
        power = 2 ** (len(data[0]) - index - 1)

        if mcb == "1":
            gamma += power
        else:
            epsilon += power

    return gamma * epsilon


def oxygen_co2(data: List[str]) -> int:
    oxygen = data[:]
    co2 = data[:]

    for index in range(len(data[0])):
        mcb_oxygen = most_common_bit(oxygen, index)
        mcb_co2 = most_common_bit(co2, index)

        if len(oxygen) > 1:
            oxygen = [x for x in oxygen if x[index] == mcb_oxygen]
        if len(co2) > 1:
            co2 = [x for x in co2 if x[index] != mcb_co2]

    return int(oxygen[0], base=2) * int(co2[0], base=2)


with open("data.txt") as f:
    data = []

    for line in f:
        data.append(line.strip())

    print(gamma_epsilon(data))
    print(oxygen_co2(data))
