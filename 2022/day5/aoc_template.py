import pathlib
import sys
from parse import parse as pparse

def parse_line(line):
    """ Parse line of stack"""
    return [line[i] for i in range(1,len(line),4)]
        

def parse_stack(stack):
    return [parse_line(line) for line in reversed(stack)]
   

def parse_movements(movements):
    movement_list = []
    pattern = 'move {quantity:d} from {origin:d} to {destination:d}'
    for movement in movements:
        res = pparse(pattern,movement)
        movement_list.append((res['quantity'], res['origin']-1, res['destination']-1))
    return movement_list


def parse_input(puzzle_input):
    """Parse input"""
    data = {}
    stack, movements = puzzle_input.split('\n\n')
    data['stack'] = [list(''.join(crates).strip()) for (_,*crates) in list(zip(*parse_stack(stack.split('\n'))))]
    data['movements'] = parse_movements(movements.split('\n'))
    return data


def move_single_crate(stack,origin,destination):
    crate = stack[origin].pop()
    stack[destination].append(crate)
    return stack

def move_crates(stack,quantity,origin,destination):
    crates = stack[origin][-quantity:]
    
    stack[origin] = stack[origin][:-quantity]
    stack[destination].extend(crates)
   
    return stack

def part1(data):
    """Solve part 1"""
    stack = data['stack']
    for quantity,origin,destination in data['movements']:
        for _ in range(quantity):
            stack = move_single_crate(stack,origin,destination)    
    return ''.join([section[-1] for section in stack if len(section)>0])


def part2(data):
    """Solve part 2"""
    stack = data['stack']
    
    for quantity,origin,destination in data['movements']:
        stack = move_crates(stack,quantity,origin,destination)
     
    return ''.join([section[-1] for section in stack if len(section)>0])


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    #data = parse_input(puzzle_input)
    solution1 = part1(parse_input(puzzle_input))
    solution2 = part2(parse_input(puzzle_input))

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n Solutions :\n")
        print("\n".join(str(solution) for solution in solutions))
