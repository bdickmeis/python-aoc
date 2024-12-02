import pathlib
import sys




def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def get_common_item(rucksack):
    one = rucksack[:int(len(rucksack)/2)]
    two = rucksack[int(len(rucksack)/2):]
    return list(set([item for item in one if item in two])).pop()

def get_badges(rucksacks):
    return list(set([badge for badge in rucksacks[0] if badge in rucksacks[1] and badge in rucksacks[2]])).pop()

def calc_priority(item):
    from string import ascii_letters
    return ascii_letters.index(item) + 1

def part1(data):
    """Solve part 1"""
    rucksack_priorities = []
    for rucksack in data:
        priority = calc_priority(get_common_item(rucksack))
        rucksack_priorities.append(priority)
    return sum(rucksack_priorities)

def part2(data):
    """Solve part 2"""
    rucksack_badges = []
    for n in range(0,len(data),3):
        priority = calc_priority(get_badges(data[n:n+3]))
        rucksack_badges.append(priority)
    return sum(rucksack_badges)





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
