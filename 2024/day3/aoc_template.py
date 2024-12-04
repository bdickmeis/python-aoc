import pathlib
import sys
import re

def parse(puzzle_input : str):
    """Parse input"""
    return [line for line in puzzle_input.splitlines(True)]

def find_instructions(data : list) -> list:
    instructions = []
    instruction_pattern = r"mul\([0-9]+,[0-9]+\)"
    for line in data:
        matches = re.findall(instruction_pattern,line)
        #print(f'{matches=}')
        instructions.extend(matches)
    return instructions

def part1(data):
    """Solve part 1"""
    instructions = find_instructions(data)
    sum = 0
    for instruction in instructions:
        numbers = instruction.split('mul')[1].replace('(','').replace(')','')
        first,second = tuple(map(int,numbers.split(',')))
        #a = first.split('(')[1]
        #b = second.split(')')[0]
        #sum += int(a) * int(b)
        sum += int(first) * int(second)
    return sum        


def part2(data):
    """Solve part 2"""
    enabled_instructions = []
    memory = "".join(data)
    memory = "".join(memory.split())
    # adding do() as start - as instructions are enabled from start
    # adding don't() at the end to make sure last do() captures till end
    memory = "do()" + memory + "don't()"

    enabled = r"do\(\)(.+?)don't\(\)"
    
    enabled_instructions = re.findall(enabled,memory)
    
    return part1(enabled_instructions)

    


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Input : {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
