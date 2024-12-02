import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [tuple(line.split(',')) for line in puzzle_input.split('\n')]
        
def convert_to_range(s) -> range:
    start,end = s.split('-')
    return range(int(start),int(end)+1)

def fully_contains(r1 : range,r2 : range) -> bool:
    return (r1.start in r2 and r1[-1] in r2) or (r2.start in r1 and r2[-1] in r1)

def range_overlaps(r1 : range,r2 : range) -> bool:
    for section in r1:
        if section in r2:
            return True
    
    for section in r2:
        if section in r1:
            return True
    
    return False

def part1(data):
    """Solve part 1"""
    fully_contains_count = 0
    for elf1,elf2 in data:
        if fully_contains(convert_to_range(elf1),convert_to_range(elf2)):
            fully_contains_count += 1
    return fully_contains_count      
        
def part2(data):
    """Solve part 2"""
    overlap_count = 0
    for elf1,elf2 in data:
        if range_overlaps(convert_to_range(elf1),convert_to_range(elf2)):
            overlap_count += 1
    return overlap_count


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
