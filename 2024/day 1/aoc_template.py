import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    first = []
    second = []
    for line in puzzle_input.split('\n'):
        first.append(int(line.split('   ')[0]))
        second.append(int(line.split('   ')[1]))
    return first,second
        


def part1(data):
    """Solve part 1"""
    first, second = data
    #print(f'{sorted(first)=}')
    #print(f'{sorted(second)=}')
    total_distance = 0
    for f,s in zip(sorted(first),sorted(second)):
        total_distance += abs(f - s)

    return total_distance


def part2(data):
    """Solve part 2"""
    first, second = data
    similarity_score = 0
    for n in first:
        if n in second:
            count = second.count(n)
        else:
            count = 0
        similarity_score += n * count
    return similarity_score


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
