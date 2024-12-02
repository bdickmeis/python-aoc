import pathlib
import sys


# OPCODES
OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_INPUT = 3
OPCODE_OUTPUT = 4
OPCODE_JMP_TRUE = 5
OPCODE_JMP_FALSE = 6
OPCODE_LT = 7
OPCODE_EQ = 8
OPCODE_HALT = 99


def read_instruction(icode : int):
    """
    ABCDE
    01002
    01101
    """
    mode3 = False # Can never be True, as parameters that an instruction writes to will never be immediate
    mode2 = False
    mode1 = False

    if icode > 100:
        # Convert last two digits as opcode
        opcode = int(str(icode)[-2:])
        modes = [int(i) for i in str(icode)[:-2]]
        if icode > 1000: 
            # We need to extract the modes for the parameters           
            mode2 = bool(modes[0])
            mode1 = bool(modes[1])
        else:
            mode1 = bool(modes[0])

    else:
        # There is only an opcode
        opcode = icode
    
    if opcode in [OPCODE_ADD,OPCODE_MULT,OPCODE_LT,OPCODE_EQ]:
        step = 4
    elif opcode in [OPCODE_JMP_TRUE,OPCODE_JMP_FALSE]:
        step = 3
    else:
        step = 2
    
    #print(f"Instruction {icode} - Modes321: {(mode3,mode2,mode1)} - Opcode : {opcode} - Step : {step}")
    return (mode3,mode2,mode1,opcode,step)    



def run_intcode(data):    

    instruction_pointer = 0
    while instruction_pointer <= len(data):
        (mode3,mode2,mode1,opcode,step) = read_instruction(data[instruction_pointer])
        
        chunk = data[instruction_pointer:instruction_pointer+step]
        modified_instruction_pointer = False
        #print(f"I:{opcode} - M:{(mode3,mode2,mode1)} - S:{step} - C:{chunk}")
        if opcode == OPCODE_ADD:
            if mode1:
                if mode2:
                    data[chunk[3]] = chunk[1] + chunk[2]
                else:
                    data[chunk[3]] = chunk[1] + data[chunk[2]]
            else:
                if mode2:
                    data[chunk[3]] = data[chunk[1]] + chunk[2]
                else:
                    data[chunk[3]] = data[chunk[1]] + data[chunk[2]]

        elif opcode == OPCODE_MULT:
            if mode1:
                if mode2:
                    data[chunk[3]] = chunk[1] * chunk[2]
                else:
                    data[chunk[3]] = chunk[1] * data[chunk[2]]
            else:
                if mode2:
                    data[chunk[3]] = data[chunk[1]] * chunk[2]
                else:
                    data[chunk[3]] = data[chunk[1]] * data[chunk[2]]
        elif opcode == OPCODE_INPUT:
            data[chunk[1]] = int(input("ID of System under TEST:"))
        elif opcode == OPCODE_OUTPUT:
            if mode1:
                print(f'TEST OUTPUT : {chunk[1]}')
            else:
                print(f'TEST OUTPUT : {data[chunk[1]]}')
        
        elif opcode == OPCODE_JMP_TRUE:
            if mode1:
                if mode2:
                    if chunk[1] != 0:
                        modified_instruction_pointer = True
                        instruction_pointer = chunk[2]
                else:
                    if chunk[1] != 0:
                        modified_instruction_pointer = True
                        instruction_pointer = data[chunk[2]]
            else:
                if mode2:
                    if data[chunk[1]] != 0:
                        modified_instruction_pointer = True
                        instruction_pointer = chunk[2]
                else:
                    if data[chunk[1]] != 0:
                        modified_instruction_pointer = True
                        instruction_pointer = data[chunk[2]]
                    
            
        elif opcode == OPCODE_JMP_FALSE:
            if mode1:
                if mode2:
                    if chunk[1] == 0:
                        modified_instruction_pointer = True
                        instruction_pointer = chunk[2]
                else:
                    if chunk[1] == 0:
                        modified_instruction_pointer = True
                        instruction_pointer = data[chunk[2]]
            else:
                if mode2:
                    if data[chunk[1]] == 0:
                        modified_instruction_pointer = True
                        instruction_pointer = chunk[2]
                else:
                    if data[chunk[1]] == 0:
                        modified_instruction_pointer = True
                        instruction_pointer = data[chunk[2]]

            
        elif opcode == OPCODE_LT:
            result = 0
            if mode1:
                if mode2:
                    if chunk[1] < chunk[2]:
                        result = 1
                else:
                    if chunk[1] < data[chunk[2]]:
                        result = 1
            else:
                if mode2:
                    if data[chunk[1]] < chunk[2]:
                        result = 1
                else:
                    if data[chunk[1]] < data[chunk[2]]:
                        result = 1
            
            data[chunk[3]] = result
                
        elif opcode == OPCODE_EQ:
            result = 0
            
            if mode1:
                if mode2:
                    if chunk[1] == chunk[2]:
                        result = 1
                else:
                    if chunk[1] == data[chunk[2]]:
                        result = 1
            else:
                if mode2:
                    if data[chunk[1]] == chunk[2]:
                        result = 1
                else:
                    if data[chunk[1]] == data[chunk[2]]:
                        result = 1
            
            data[chunk[3]] = result    

        elif OPCODE_HALT:
            #print(f'noun {data[1]} - verb {data[2]} - Halted : {data[0]}')
            #if data[0] == TARGET_VALUE:
            #print(f'noun {data[1]} - verb {data[2]} - Halted : {data[0]}')
            print(f'--PROGRAM HALTED--')
            break
        else:
            print(f'PANIC! : Illegal opcode detected : {chunk[0]}')
            break

        if not modified_instruction_pointer: # Only increment if we didn't modify the instruction point using JMP opcodes
            instruction_pointer += step   
    return data[0]

def parse(puzzle_input):
    """Parse input"""
    return [int(code) for code in puzzle_input.split(',')]


def part1(data):
    """Solve part 1"""
    return run_intcode(data)


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
