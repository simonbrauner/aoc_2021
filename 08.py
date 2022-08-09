from typing import Dict, List, Tuple


EASY_DIGITS = {2: 1, 4: 4, 3: 7, 7: 8}

INTERSECTION_LENGTHS_FIVE = {(1, 2): 2, (2, 3): 3, (1, 3): 5}
INTERSECTION_LENGTHS_SIX = {(2, 3): 0, (1, 3): 6, (2, 4): 9}


def intersection_lengths(
    pattern: str, digit_to_pattern: Dict[int, str]
) -> Tuple[int, int]:
    return (
        len(set(pattern) & set(digit_to_pattern[1])),
        len(set(pattern) & set(digit_to_pattern[4])),
    )


def digit_translator(patterns: List[str]) -> Dict[str, int]:
    pattern_to_digit = dict()

    for pattern in patterns:
        if len(pattern) in EASY_DIGITS:
            pattern_to_digit[pattern] = EASY_DIGITS[len(pattern)]

    digit_to_pattern = {v: k for k, v in pattern_to_digit.items()}

    for pattern in patterns:
        if len(pattern) not in EASY_DIGITS:
            if len(pattern) == 5:
                pattern_to_digit[pattern] = INTERSECTION_LENGTHS_FIVE[
                    (intersection_lengths(pattern, digit_to_pattern))
                ]
            else:
                pattern_to_digit[pattern] = INTERSECTION_LENGTHS_SIX[
                    (intersection_lengths(pattern, digit_to_pattern))
                ]

    return pattern_to_digit


def output_value(output: List[str], translator: Dict[str, int]) -> int:
    result = 0

    for pattern in output:
        result *= 10
        result += translator[pattern]

    return result


def decode_output(
    pattern_groups: List[List[str]], outputs: List[List[str]], easy_only: bool
) -> int:
    result = 0

    for index in range(len(pattern_groups)):
        if easy_only:
            for digit in outputs[index]:
                if len(digit) in EASY_DIGITS:
                    result += 1
        else:
            result += output_value(
                outputs[index], digit_translator(pattern_groups[index])
            )

    return result


with open("data.txt") as f:
    pattern_groups = []
    outputs = []

    for line in f:
        split = line.split("|")
        pattern_groups.append(["".join(sorted(x)) for x in split[0].split()])
        outputs.append(["".join(sorted(x)) for x in split[1].split()])

    print(decode_output(pattern_groups, outputs, True))
    print(decode_output(pattern_groups, outputs, False))
