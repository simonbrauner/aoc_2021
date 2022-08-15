from typing import Iterator


class Player:
    def __init__(self, starting_space: int, die: Iterator[int]):
        self.space = starting_space
        self.die = die
        self.score = 0

    def play_turn(self) -> None:
        for _ in range(3):
            self.space += next(self.die)

        self.space %= 10
        if self.space == 0:
            self.space += 10

        self.score += self.space

    def won(self) -> bool:
        return self.score >= 1000


def roll_dice() -> Iterator[int]:
    while True:
        for side in range(1, 101):
            yield side


def play(players: list[Player]) -> int:
    rolls = 0

    while True:
        for player in players:
            player.play_turn()
            rolls += 3

            if player.won():
                losers = [x for x in players if x is not player]
                return losers[0].score * rolls


with open("data.txt") as f:
    players = []
    die = roll_dice()

    for line in f:
        players.append(Player(int(line.split(": ")[1]), die))

    print(play(players))
