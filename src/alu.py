# class to arrange functions, not a functional class
class ALU: 
    @staticmethod
    # binary adder
    def bin_add(num1,num2):
        num1 = f"{int(num1):08b}" #converts string to integer, then binary. 
        num2 = f"{int(num2):08b}"
        num3=''
        carry_bit = 0
        for i in range(7,-1,-1): # loop from last digit to first digit to simulate binary full adder
            # loops through each digits of a binary number. 
            # reason for unnecessary convertion is to retain the padding 0s for logic gates
            a = int(num1[i])
            b = int(num2[i])
            # sum is 1 when either exactly one operand is 1 but carry is 0, or operands are equal and carry is 1
            sum_bit = (a ^ b) ^ carry_bit
            # carry is 1 when at least 2 numbers are 1
            carry_bit = (a & b) | ((a | b) & carry_bit)
            num3 = str(sum_bit) + num3
        #return the added bit as a binary
        return int(num3,base=2)
    
    @staticmethod
    def bin_sub(num1,num2):
        temp = f"{int(num2):08b}"
        inverted = ''
        for i in range(7,-1,-1):
            inverted = str(1-int(temp[i])) + inverted # invert all bits
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
    