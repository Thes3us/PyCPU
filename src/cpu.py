#refer instructions.md for detailed instructions
from assembler import assemble
from alu import ALU
from cu import CU
def cpu(filename):  
    reg = [0]*8 # initialize 8 registers with 0
    instruction_set = []
    pc=0 # program counter
    # assemble() returns [] for invalid filename
    instruction_set = assemble(filename)
    if instruction_set == []:
        print(" ERROR: Instruction set cannot be empty")
        exit()
    debug_mode = int(input("Type 1 if you want to enable debug, 0 to only display output (reg7):"))

    while(pc < len(instruction_set)):
        if debug_mode:
            print(pc + 1,end ='. ') # display line number 

        # fetch
        byte = instruction_set[pc] 

        # decode and execute
        opcode = byte[:2] 
        match opcode:
            case '00': #immediate
                reg[0]=int(byte[2:],2) # base 2 to base 10

            case '01': #mov
                A = int(byte[2:5],2) # first 3 bits after opcode is reg a
                B = int(byte[5:],2) # last 3 bits is reg b
                reg[B] = reg[A] # copy values of reg a to reg b
                if B == 7 and not debug_mode: # if moving to reg7, print reg7 as signed (output)
                    out = reg[7]
                    if int(reg[7]) >= 128:
                        out = int(reg[7]) - 256
                    print("output:",out)

            case '10': #calculate
                operator = byte[5:]
                match operator:
                    case '000': #add
                        reg[3] = ALU.bin_add(reg[1],reg[2])
                    case '001': #sub
                        reg[3] = ALU.bin_sub(reg[1],reg[2])
                    case '010' | '011' | '100' | '101': #and,nand,or,nor
                        reg[3] = ALU.bin_gate(reg[1],reg[2],operator)
                    case _:
                        raise ValueError("invalid operation")
                    
            case '11': #conditional jump
                num = reg[3] # value to check
                jump = reg[0] # address to jump to
                operator = byte[5:]
                match operator:
                    case '000':
                        pass # pc is unchanged
                    case '001' | '010' | '011' | '100' | '101' | '110': # conditional jump
                        if CU(num, operator): 
                            pc = jump
                    case '111': # unconditional jump
                        pc = jump
        if debug_mode:
            print("register:",reg)
        pc+=1 #increment program counter