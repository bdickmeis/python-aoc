import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    instructions = []
    instruction_pattern = r"mul\([0-9]+,[0-9]+\)"
    for line in data:
        matches = re.findall(instruction_pattern,line)
        instructions.extend(matches)
    
    sum = 0
    for instruction in instructions:
        first,second = instruction.split(',')
        a = first.split('(')[1]
        b = second.split(')')[0]
        sum += int(a) * int(b)
    return sum
        


def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
