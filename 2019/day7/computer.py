from enum import Enum

class Opcode(Enum):    
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JMP_TRUE = 5
    JMP_FALSE = 6
    LT = 7
    EQ = 8
    HALT = 99

class ComputerKernelPanic(Exception):

    def __init__(self, *args) -> None:
        super().__init__(*args)

class Computer:
   

    def __init__(self,program) -> None:
        self.program = program

    def parse_instruction(self,instruction : int):
        str_instr = str(instruction)
        opcode = int(str_instr[-1])
        mode1 = bool(int(str_instr[-3])) if len(str_instr) > 2 else False
        mode2 = bool(int(str_instr[-4])) if len(str_instr) > 3 else False

        return opcode,mode1,mode2
    
    def get_value(self,operation : int,address_mode : bool):
        if address_mode:
            return self.program[operation]
        else:
            return operation
        
    def run(self):
        """
        ip : instruction pointer
        instruction contains opcode + parameter modes
        opcode : see Enum class
        mode1 & mode2 : True - immediate mode - use value directly
                        False - position mode - use value as an adress in the program

        """
        ip = 0
        

        while self.program[ip] != Opcode.HALT:
            try:

                opcode, mode1, mode2 = self.parse_instruction(self.program[ip])

                match opcode:
                    case Opcode.ADD:
                        op1,op2,op3 = self.program[ip+1],self.program[ip+2],self.program[ip+3]
                        self.program[op3] = self.get_value(op1,mode1) + self.get_value(op2,mode2)
                        ip += 4

                    case Opcode.MULT:
                        op1,op2,op3 = self.program[ip+1],self.program[ip+2],self.program[ip+3]
                        self.program[op3] = self.get_value(op1,mode1) * self.get_value(op2,mode2)
                        ip += 4

                    case Opcode.INPUT:
                        op1 = self.program[ip+1]
                        self.program[op1] = int(input("Input: "))
                        ip +=2

                    case Opcode.OUTPUT:
                        op1 = self.get_value(self.program[ip+1],mode1)
                        print(f"OUTPUT: {op1}")
                        ip +=2

                    case Opcode.JMP_TRUE:
                        op1,op2 = self.program[ip+1],self.program[ip+2]
                        jump_trigger_value = self.get_value(op1,mode1)                        

                        if jump_trigger_value != 0:
                            # Jump to new instruction - no need to increment instruction pointer
                            ip = self.get_value(op2,mode2)
                        else:
                            ip += 3

                    case Opcode.JMP_FALSE:
                        op1,op2 = self.program[ip+1],self.program[ip+2]
                        jump_trigger_value = self.get_value(op1,mode1)                        

                        if jump_trigger_value == 0:
                            # Jump to new instruction - no need to increment instruction pointer
                            ip = self.get_value(op2,mode2)
                        else:
                            ip += 3

                    case Opcode.LT:
                        op1,op2,op3 = self.program[ip+1],self.program[ip+2],self.program[ip+3]
                        self.program[op3] = int(self.get_value(op1,mode1) < self.get_value(op2,mode2))
                        ip += 4

                    case Opcode.EQ:
                        op1,op2,op3 = self.program[ip+1],self.program[ip+2],self.program[ip+3]
                        self.program[op3] = int(self.get_value(op1,mode1) == self.get_value(op2,mode2))
                        ip += 4    

                    case _ :
                        raise ComputerKernelPanic(opcode,ip,self.program[ip])
            
            except ComputerKernelPanic:
                break
