from typing import List


def hex_to_bin_digits(letter: str) -> List[int]:
    result = []
    hexadecimal = int(letter, base=16)

    for possible_divisor in [8, 4, 2, 1]:
        if hexadecimal >= possible_divisor:
            hexadecimal -= possible_divisor
            result.append(1)
        else:
            result.append(0)

    return result


with open("data.txt") as f:
    bits = []

    for letter in f.readline().strip():
        bits.extend(hex_to_bin_digits(letter))

    print(bits)
