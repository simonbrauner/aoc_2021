from collections.abc import Callable
from collections import deque
from random import randrange

MIN_MODEL_NUMBER = 11111111111111
MAX_MODEL_NUMBER = 99999999999999

FUNCTIONS: dict[str, Callable[[int, int], int]] = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: int(x / y),
    "mod": lambda x, y: x % y,
    "eql": lambda x, y: 1 if x == y else 0,
}


class Instruction:
    def __init__(self, raw: str):
        split = raw.split()
        self.name = split[0]
        self.variable = split[1]
        self.value = split[2] if len(split) == 3 else None

    def evaluate(self, inputs: deque[int], variables: dict[str, int]) -> None:
        if self.name == "inp":
            variables[self.variable] = inputs.popleft()
            return

        assert self.value is not None
        value = variables[self.value] if self.value in variables else int(self.value)

        variables[self.variable] = FUNCTIONS[self.name](variables[self.variable], value)


def run_program(
    program: list[Instruction], string_number: str, verbose: bool = False
) -> dict[str, int]:
    inputs = deque([int(x) for x in string_number])
    variables = {x: 0 for x in "wxyz"}

    for instruction in program:
        if verbose:
            print(variables)
        instruction.evaluate(inputs, variables)

    if verbose:
        print(variables)
    return variables


def find_minimal_random_z_value(program: list[Instruction]) -> None:
    min_z = float("inf")

    while True:
        current = str(randrange(MIN_MODEL_NUMBER, MAX_MODEL_NUMBER + 1))
        if "0" in current:
            continue

        variables = run_program(program, str(current))
        if variables["z"] < min_z:
            min_z = variables["z"]
            print(f"{current}: {min_z}")


with open("data.txt") as f:
    program = []

    for line in f:
        program.append(Instruction(line.strip()))

    find_minimal_random_z_value(program)
