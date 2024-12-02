import pathlib
import sys



def parse(puzzle_input):
    """Parse input"""
    return range(206938,679128)

def convert_from_int_to_list_digits(number) -> list[int]:
    return [int(digit) for digit in str(number)]

def convert_from_list_digits_to_int(digits : list[int]) -> int:
    return sum(d * 10 **i for i,d in enumerate(digits[::-1]))

def check_number(number:int) -> bool:
    digits = convert_from_int_to_list_digits(number)
    digits_sorted = convert_from_int_to_list_digits(number)
    digits_sorted.sort()

    if len(digits) != 6:
        return False

    if number != convert_from_list_digits_to_int(digits_sorted):
        return False
    
    if len(set(digits)) == len(digits):
        return False
    
    return True

def part1(data):
    """Solve part 1"""
    check_list = []
    for number in data:
        check_list.append(check_number(number))
    return sum(check_list)


def part2(data):
    """Solve part 2"""
    check_list = []
    for number in data:
        if 2 in map(str(number).count, str(number)):
            check_list.append(check_number(number))
    return sum(check_list)


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
