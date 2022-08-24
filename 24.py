from collections.abc import Callable
from collections import deque

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
        self.value = split[2]

    def __repr__(self) -> str:
        return f"{self.name} {self.variable} {self.value}"

    def evaluate(self, variables: dict[str, int]) -> None:
        value = variables[self.value] if self.value in variables else int(self.value)

        variables[self.variable] = FUNCTIONS[self.name](variables[self.variable], value)


def run_program(
    program: list[list[Instruction]], string_number: str, verbose: bool = False
) -> dict[str, int]:
    inputs = deque([int(x) for x in string_number])
    variables = {x: 0 for x in "wxyz"}

    for part in program:
        variables["w"] = inputs.popleft()
        for instruction in part:
            instruction.evaluate(variables)
            if verbose:
                print(f"{str(instruction): <12}{variables}")

    return variables


with open("data.txt") as f:
    program = []
    part: list[Instruction] = []

    assert f.readline().strip() == "inp w"

    while (line := f.readline().strip()) != "":
        if line == "inp w":
            program.append(part)
            part = []
        else:
            part.append(Instruction(line))
    program.append(part)

    print(program)
