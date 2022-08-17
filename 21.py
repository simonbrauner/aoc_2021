from dataclasses import dataclass


DETERMINISTIC_DICE = range(1, 101)
QUANTUM_DICE = range(1, 4)
SCORES = [10] + list(range(1, 10))


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

    return max(play_quantum_rec(active, passive))


def play_quantum_rec(active: Player, passive: Player) -> tuple[int, int]:
    if passive.score >= 21:
        return 1, 0

    active_win = 0
    passive_win = 0

    for first in QUANTUM_DICE:
        for second in QUANTUM_DICE:
            for third in QUANTUM_DICE:
                total = first + second + third

                subresult = play_quantum_rec(
                    passive,
                    Player(
                        active.space + total,
                        active.score + SCORES[(active.space + total) % len(SCORES)],
                    ),
                )
                active_win += subresult[0]
                passive_win += subresult[1]

    return passive_win, active_win


with open("data.txt") as f:
    starts = []

    for line in f:
        starts.append(int(line.split(": ")[1]))

    print(play_deterministic(starts[0], starts[1]))
    print(play_quantum(starts[0], starts[1]))
