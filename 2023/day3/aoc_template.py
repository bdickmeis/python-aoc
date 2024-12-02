import pathlib
import sys


def parse(puzzle_input) -> list[list[str]]:
    """Parse input"""
    return [[c for c in line] for line in puzzle_input.split('\n')]


def get_digit(value : str) -> int:
    for v in value:
        try:
            digit = int(v)
            return digit
        except ValueError:
            continue

def detect_symbols(data) -> list[(int,int)]:
    symbols = []
    for row,line in enumerate(data):
        for col,char in enumerate(line):
            if not char.isdigit() and char != '.':
                symbols.append((row,col))
    
    return symbols


def find_adjacent_digits(data,symbols) -> list[(int,int)]:
    adj_digit = []

    for x,y in symbols:
        for xloc in range(-1,2,1):
            for yloc in range(-1,2,1):
                if data[x+xloc][y+yloc].isdigit():
                    adj_digit.append((x+xloc,y+yloc))
    
    # Sort on x (row) number
    adj_digit.sort()
    return adj_digit
            

def get_part_numbers(location_list):
    # go through grid and parse as int?
    # combine afterwards?
    
    pass


def part1(data):
    """Solve part 1"""
    symbols = detect_symbols(data)
    #print(symbols)
    adj_digits = find_adjacent_digits(data,symbols)
    #print(adj_digits)

                
    


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
