from dataclasses import dataclass
from collections import Counter


DETERMINISTIC_DICE = range(1, 101)
SCORES = [10] + list(range(1, 10))

QUANTUM_DICE = range(1, 4)
QUANTUM_ROLLS = Counter(
    [x + y + z for x in QUANTUM_DICE for y in QUANTUM_DICE for z in QUANTUM_DICE]
)


@dataclass
class Player:
    space: int
    score: int = 0


def play_deterministic(first_start: int, second_start: int) -> int:
    active = Player(first_start)
    passive = Player(second_start)
    rolls = 0

    while True:
        for _ in range(3):
            active.space += DETERMINISTIC_DICE[rolls % len(DETERMINISTIC_DICE)]
            rolls += 1

        active.score += SCORES[active.space % len(SCORES)]
        if active.score >= 1000:
            return passive.score * rolls

        active, passive = passive, active


def play_quantum(first_start: int, second_start: int) -> int:
    active = Player(first_start)
    passive = Player(second_start)

    return max(play_quantum_rec(active, passive, {}))


def play_quantum_rec(
    active: Player,
    passive: Player,
    subresults: dict[tuple[int, int, int, int], tuple[int, int]],
) -> tuple[int, int]:
    if passive.score >= 21:
        return 1, 0

    state = active.space, active.score, passive.space, passive.score

    if state not in subresults:
        active_win = 0
        passive_win = 0

        for value, quantity in QUANTUM_ROLLS.items():
            subresult = play_quantum_rec(
                passive,
                Player(
                    active.space + value,
                    active.score + SCORES[(active.space + value) % len(SCORES)],
                ),
                subresults,
            )
            active_win += subresult[0] * quantity
            passive_win += subresult[1] * quantity

        subresults[state] = passive_win, active_win

    return subresults[state]


with open("data.txt") as f:
    starts = []

    for line in f:
        starts.append(int(line.split(": ")[1]))

    print(play_deterministic(starts[0], starts[1]))
    print(play_quantum(starts[0], starts[1]))
