#refer instructions.md for detailed instructions
from assembler import assemble
instruction_set = []
while instruction_set == []:
    filename = input("Enter the name of text file to assemble (0 to quit): ")
    instruction_set = assemble(filename)
class ALU:
    @staticmethod
    def bin_add(num1,num2):
        num1 = f"{int(num1):08b}"
        num2 = f"{int(num2):08b}"
        num3=''
        carry = 0
        for i in range(7,-1,-1):
            a = int(num1[i])
            b = int(num2[i])
            sum = (a ^ b) ^ carry
            carry = (a & b) | ((a | b) & carry)
            num3 = str(sum)+ num3
        return int(num3,base=2)
    @staticmethod
    def bin_sub(num1,num2):
        temp = f"{int(num2):08b}"
        num2 = ''
        for i in range(7,-1,-1):
            num2 = str(1-int(temp[i])) + num2
        two_comp = ALU.bin_add(1,int(num2,2)) 
        substracted = ALU.bin_add(num1,two_comp)
        return substracted
    @staticmethod
    def bin_gate(num1,num2,operator):
        num1 = f"{int(num1):08b}"
        num2 = f"{int(num2):08b}"
        num3=''
        if operator == '010':
            for i in range(7,-1,-1):
                num3 = str(int(num1[i]) & int(num2[i])) + num3
        if operator == '011':
            for i in range(7,-1,-1):
                num3 = str(1 - (int(num1[i]) & int(num2[i]))) + num3
        if operator == '100':
            for i in range(7,-1,-1):
                num3 = str(int(num1[i]) | int(num2[i])) + num3
        if operator == '101':
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
    reg = [0]*8
    debug_mode = int(input("Type 1 if you want to enable debug, 0 to only display output (reg8):"))
    alu = ALU()
    i=0
    while(i<len(instruction_set)):
        i+=1
        if debug_mode:
            print(i,end ='. ')
        byte = instruction_set[i-1]
        opcode = byte[:2]
        match opcode:
            case '00': #immediate
                reg[0]=int(byte[2:],2)
            case '01': #mov
                A = int(byte[2:5],2)
                B = int(byte[5:],2)
                reg[B] = reg[A]
                if B == 7 and not debug_mode:
                    print("output:",reg[B])
            case '10': #calculate
                operator = byte[5:]
                match operator:
                    case '000':
                        reg[3] = alu.bin_add(reg[1],reg[2])
                    case '001':
                        reg[3] = alu.bin_sub(reg[1],reg[2])
                    case '010':
                        reg[3] = alu.bin_gate(reg[1],reg[2],operator)
                    case '011':
                        reg[3] = alu.bin_gate(reg[1],reg[2],operator)
                    case '100':
                        reg[3] = alu.bin_gate(reg[1],reg[2],operator)
                    case '101':
                        reg[3] = alu.bin_gate(reg[1],reg[2],operator)
                    case _:
                        print("invalid operation")
                        break
            case '11': #conditional jump
                num = reg[3]
                overwrite = reg[0]
                operator = byte[5:]
                match operator:
                    case '000':
                        pass
                    case '001':
                        i = (overwrite if CU(num,operator) else i)
                    case '010':
                        i = (overwrite if CU(num,operator) else i)
                    case '011':
                        i = (overwrite if CU(num,operator) else i)
                    case '100':
                        i = (overwrite if CU(num,operator) else i)
                    case '101':
                        i = (overwrite if CU(num,operator) else i)
                    case '110':
                        i = (overwrite if CU(num,operator) else i)
                    case '111':
                        i = overwrite
                    case _:
                        print("invalid operation")
                        break
            case _:
                print("invalid opcode")
                break
        out = reg[7]
        if int(reg[7]) >= 128:
            out = int(reg[7]) - 256
        if debug_mode:
            print("register:",reg)

main()
