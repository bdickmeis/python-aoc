import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    
    def convert_item(item):
        return int(item)
    
    return [convert_item(line) for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    def fuel_formula(mass):
        return int(mass / 3) - 2
    
    return sum([mass // 3 - 2 for mass in data])


def all_fuel(mass):
    """Calculate fuel while taking mass of the fuel into account. """

    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + all_fuel(mass=fuel)

def part2(data):
    """Solve part 2"""    
    return sum([all_fuel(mass) for mass in data])


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
