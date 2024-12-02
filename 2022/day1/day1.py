import pathlib
import sys


def calc_totals(data):
    totals = []
    snack_total = 0
    for snack in data:
        if not snack == '':
            snack_total += int(snack)
        else:
            totals.append(snack_total)
            snack_total = 0
    totals.append(snack_total)
    return totals

def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split('\n')      

def part1(data):
    """Solve part 1"""
    totals = calc_totals(data)    
    return max(totals)


def part2(data):
    """Solve part 2"""
    totals = calc_totals(data)
    print(totals)
    top_3 = sorted(totals,reverse=True)[:3]
    print(top_3	)                
    return sum(top_3)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    print(f'{data=}')
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(f'{puzzle_input}:')
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
