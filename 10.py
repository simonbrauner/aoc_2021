from typing import List


OPENING_DELIMITERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSING_DELIMITERS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def syntax_error_score(data: List[str]) -> int:
    result = 0

    for line in data:
        opened = []

        for char in line:
            if char in OPENING_DELIMITERS:
                opened.append(OPENING_DELIMITERS[char])
            elif opened.pop() != char:
                result += CLOSING_DELIMITERS[char]
                break

    return result


with open("data.txt") as f:
    data = []

    for line in f:
        data.append(line.strip())

    print(syntax_error_score(data))
