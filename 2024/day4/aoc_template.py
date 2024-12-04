import pathlib
import sys

"""
input:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

hits:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""

word = "XMAS"


class Direction:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"index increment row+{self.x}, col+{self.y}"


def is_valid_pos(row, col, data):
    # check for boundaries
    if 0 <= row <= len(data):
        if 0 <= col <= len(data[row]):
            return True

    return False

def check_next(letter,row,col,dir):
    pass

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    directions = [
        Direction(-1, -1),
        Direction(-1, 0),
        Direction(-1, 1),
        Direction(0, -1),
        Direction(0, 0),
        Direction(0, 1),
        Direction(1, -1),
        Direction(1, 0),
        Direction(1, 1),
    ]

    for row in range(0,len(data)):
        for col in range(0,len(data[row])):
            # check if first letter or last letter of the word is found
            # string can be reversed as well
            if data[row][col] == word[0]:
                print(f'Starting letter found at {(row,col)}')
                for dir in directions:
                    if is_valid_pos(row+dir.x,col+dir.y,data):
                        check_next(word[1],row+dir.x,col+dir.y,dir)
            if data[row][col] == word[-1]:
                print(f'Ending letter found at {(row,col)}')

    return None


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
