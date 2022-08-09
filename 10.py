from typing import List


OPENING = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSING_SYNTAX = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSING_AUTOCOMPLETE = {")": 1, "]": 2, "}": 3, ">": 4}


def syntax_error_score(data: List[str]) -> int:
    result = 0

    for line in data:
        opened = []

        for char in line:
            if char in OPENING:
                opened.append(OPENING[char])
            elif opened.pop() != char:
                result += CLOSING_SYNTAX[char]
                break

    return result


def autocomplete_score(opened: List[str]) -> int:
    score = 0

    for delimiter in reversed(opened):
        score *= 5
        score += CLOSING_AUTOCOMPLETE[delimiter]

    return score


def autocomplete_score_middle(data: List[str]) -> int:
    scores = []

    for line in data:
        opened = []
        incomplete = True

        for char in line:
            if char in OPENING:
                opened.append(OPENING[char])
            elif opened.pop() != char:
                incomplete = False
                break

        if incomplete:
            scores.append(autocomplete_score(opened))

    scores.sort()
    return scores[len(scores) // 2]


with open("data.txt") as f:
    data = []

    for line in f:
        data.append(line.strip())

    print(syntax_error_score(data))
    print(autocomplete_score_middle(data))
