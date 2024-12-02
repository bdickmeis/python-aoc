import pathlib
import sys



"""
https://adventofcode.com/2019/day/2

An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). 
To run one, start by looking at the first integer (called position 0). 
Here, you will find an opcode - either 1, 2, or 99.
The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. 
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. 
The three integers immediately after the opcode tell you these three positions 
- the first two indicate the positions from which you should read the input values,
and the third indicates the position at which the output should be stored.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

"""

OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_HALT = 99
#TARGET_VALUE = 3058646
TARGET_VALUE = 19690720

def parse(puzzle_input):
    """Parse input"""
    return [int(code) for code in puzzle_input.split(',')]

def run_intcode(data):    
    start = 0
    end = len(data)
    step = 4

    for index in range(start,end,step):
        
        chunk = data[index:index+step]
        
        if chunk[0] == OPCODE_ADD:
            data[chunk[3]] = data[chunk[1]] + data[chunk[2]]
        elif chunk[0] == OPCODE_MULT:
            data[chunk[3]] = data[chunk[1]] * data[chunk[2]]
        elif OPCODE_HALT:
            #print(f'noun {data[1]} - verb {data[2]} - Halted : {data[0]}')
            if data[0] == TARGET_VALUE:
                print(f'noun {data[1]} - verb {data[2]} - Halted : {data[0]}')
            break
        else:
            print(f'PANIC! : Illegal opcode detected : {chunk[0]}')
            break   
    return data[0]

def part1(data):
    """Solve part 1"""
    data[1] = 12
    data[2] = 2
    return run_intcode(data)



def part2(data):
    """Solve part 2"""
    
    init = data[:]
    
    for noun in range(100):
        for verb in range(100):
            data = init[:]
            data[1] = noun
            data[2] = verb
            if run_intcode(data) == TARGET_VALUE:
                print(f'{noun=} - {verb=}')
                break
        else:            
            continue
        break
     
    return 100 * noun + verb


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
