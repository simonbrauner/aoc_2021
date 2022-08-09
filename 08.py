from typing import Dict, List


EASY_DIGITS = {2: 1, 4: 4, 3: 7, 7: 8}


def digit_translator(patterns: List[str]) -> Dict[str, int]:
    translator = dict()

    for pattern in patterns:
        if len(pattern) in EASY_DIGITS:
            translator[pattern] = EASY_DIGITS[len(pattern)]

    return translator


def count_easy_digits(pattern_groups: List[List[str]], outputs: List[List[str]]) -> int:
    result = 0

    for index in range(len(pattern_groups)):
        translator = digit_translator(pattern_groups[index])

        for digit in outputs[index]:
            if digit in translator:
                result += 1

    return result


with open("data.txt") as f:
    pattern_groups = []
    outputs = []

    for line in f:
        split = line.split("|")
        pattern_groups.append(["".join(sorted(x)) for x in split[0].split()])
        outputs.append(["".join(sorted(x)) for x in split[1].split()])

    print(count_easy_digits(pattern_groups, outputs))
