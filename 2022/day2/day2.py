import pathlib
import sys
"""
A = Rock, B = Paper, C = Scissors
1 = Rock, 2 = Paper, 3 = Scissors
X = loss = 0, Y = draw = 3, Z = win = 6

"""

score_matrix = {
    "A X" : 3, 
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7 
}

def parse(puzzle_input):
    """Parse input"""
    tournament = []
    for line in puzzle_input.split("\n"):
        tournament.append(line)
    return tournament



def part1(data):
    """Solve part 1"""
    total = 0
    for move in data:
        total += score_matrix[move]    
    return total



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
