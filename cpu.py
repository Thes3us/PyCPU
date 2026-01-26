#refer instructions.md for detailed instructions
from assembler import assemble
instruction_set = []
# assembler.py returns [] for invalid filename
while instruction_set == []:
    filename = input("Enter the name of text file to assemble (0 to quit): ")
    instruction_set = assemble(filename)
# class to arrange functions, not a functional class
class ALU:
    # @staticmethod because i was lazy to handle `self`
    @staticmethod
    # binary adder
    def bin_add(num1,num2):
        #converts string to integer, then binary. 
        num1 = f"{int(num1):08b}"
        num2 = f"{int(num2):08b}"
        num3=''
        carry = 0
        # loop from last digit to first digit to simulate binary full adder
        for i in range(7,-1,-1):
            # loops through each digits of a binary number. 
            # reason for unnecessary convertion is to retain the padding 0s for logic gates
            a = int(num1[i])
            b = int(num2[i])
            # sum is 1 when either exactly one operand is 1 but carry is 0, or operands are equal and carry is 1
            sum = (a ^ b) ^ carry
            # carry is 1 when at least 2 numbers are 1
            carry = (a & b) | ((a | b) & carry)
            num3 = str(sum) + num3
        #return the added bit as a binary
        return int(num3,base=2)
    @staticmethod
    def bin_sub(num1,num2):
        temp = f"{int(num2):08b}"
        inverted = ''
        for i in range(7,-1,-1):
            # invert all bits
            inverted = str(1-int(temp[i])) + inverted
        # add 1 to inverted bit
        two_comp = ALU.bin_add(1,int(inverted,2)) 
        # add num1 and two's compliment to substract two numebrs
        substracted = ALU.bin_add(num1,two_comp)
        return substracted
    @staticmethod
    def bin_gate(num1,num2,operator):
        num1 = f"{int(num1):08b}"
        num2 = f"{int(num2):08b}"
        num3=''
        if operator == '010': # and
            for i in range(7,-1,-1):
                num3 = str(int(num1[i]) & int(num2[i])) + num3
        if operator == '011': # nand
            for i in range(7,-1,-1):
                num3 = str(1 - (int(num1[i]) & int(num2[i]))) + num3
        if operator == '100': # or
            for i in range(7,-1,-1):
                num3 = str(int(num1[i]) | int(num2[i])) + num3
        if operator == '101': # nor
            for i in range(7,-1,-1):
                num3 = str(1 - (int(num1[i]) | int(num2[i]))) + num3
        return int(num3,base=2)
def CU(num,operator):
    num = f"{int(num):08b}"
    result = False
    allzero = (1-int(num[1]) and 1-int(num[2]) and 1-int(num[3]) and 1-int(num[4]) and 1-int(num[5]) 
               and 1-int(num[6]) and 1-int(num[7]))
    if operator == '001': #>0
        if (num[0] == '0') and not allzero:
            result = True
    if operator == '010': #>=0
        if (num[0] == '0'):
            result = True
    if operator == '011': #==0
        if allzero:
            result = True
    if operator == '100': #<=0
        if (num[0] == '1') or allzero:
            result = True
    if operator == '101': #<0
        if (num[0] == '1'):
            result = True
    if operator == '110': #!=0
        if not allzero:
            result = True
    return result
def main():
    reg = [0]*8 # initialize 8 registers with 0
    debug_mode = int(input("Type 1 if you want to enable debug, 0 to only display output (reg7):"))
    alu = ALU() # initialize ALU
    i=0 # program counter
    while(i<len(instruction_set)):
        if debug_mode:
            print(i+1,end ='. ')
        byte = instruction_set[i]
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
                        reg[3] = alu.bin_add(reg[1],reg[2])
                    case '001': #sub
                        reg[3] = alu.bin_sub(reg[1],reg[2])
                    case '010' | '011' | '100' | '101': #and,nand,or,nor
                        reg[3] = alu.bin_gate(reg[1],reg[2],operator)
                    case _:
                        raise ValueError("invalid operation")
            case '11': #conditional jump
                num = reg[3]
                jump = reg[0]
                operator = byte[5:]
                match operator:
                    case '000':
                        pass # i is unchanged
                    case '001' | '010' | '011' | '100' | '101' | '110': # conditional jump
                        if CU(num, operator): 
                            i = jump
                    case '111': # unconditional jump
                        i = jump
                    case _: 
                        raise ValueError("invalid operation")
            case _:
                raise ValueError("invalid operation")
        if debug_mode:
            print("register:",reg)
        i+=1 #increment program counter
main()