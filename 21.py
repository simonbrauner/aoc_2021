from dataclasses import dataclass


DETERMINISTIC_DICE = range(1, 101)
SCORES = [10] + list(range(1, 10))


@dataclass
class Player:
    space: int
    score = 0


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


with open("data.txt") as f:
    starts = []

    for line in f:
        starts.append(int(line.split(": ")[1]))

    print(play_deterministic(starts[0], starts[1]))
