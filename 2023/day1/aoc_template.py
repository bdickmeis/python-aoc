import pathlib
import sys


def get_digit(value : str) -> int:
    for v in value:
        try:
            digit = int(v)
            return digit
        except ValueError:
            continue


digit_words = ["one","two","three","four","five","six","seven","eight","nine"]
digit_values = ["1","2","3","4","5","6","7","8","9"]
digit_mapping = list(zip(digit_words,digit_values))

def replace_digit_words(s : str):
    forward = walk_string(s,'forward')
    return walk_string(forward,'backward')

def walk_string(s: str,direction):
    
    if direction == "forward":
        for i in range(3,len(s)+1):
            piece = s[:i]            
            for (word,value) in digit_mapping:
                if word in piece:
                    s = s.replace(word,value)
                    return s   
    
    elif direction == "backward":
        for i in range(3,len(s)+1):
            piece = s[-i:]
            for (word,value) in digit_mapping:
                if word in piece:
                    s = s.replace(word,value)
                    return s
         
    else:
        print("ILLEGAL INSTRUCTION!")
        raise ValueError("illegal instruction")
    # Nothing found to replace
    return s

def get_calibration_value(value):
    first_digit = get_digit(value)
    last_digit = get_digit(reversed(value))
    return first_digit*10+last_digit


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def part1(data):
    """Solve part 1"""
    calibration_list = []
    for value in data:
        calibration_list.append(get_calibration_value(value))
    
    return sum(calibration_list)



def part2(data):
    """Solve part 2"""
    calibration_list = []
    for value in data:
        first_val = walk_string(value,"forward")
        first_digit = get_digit(first_val)
        last_val = walk_string(value,"backward")
        last_digit = get_digit(reversed(last_val))

        calibration_list.append(first_digit*10+last_digit)
 
    return sum(calibration_list)


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
