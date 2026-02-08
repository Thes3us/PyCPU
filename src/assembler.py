#assembler
def assemble(file_name):
    import re
    CAL_OPS = {
        "add": "10000000",
        "sub": "10000001",
        "and": "10000010",
        "nand": "10000011",
        "or": "10000100",
        "nor": "10000101",
    }
    JMP_OPS = {
        "nvr": "11000000",
        "gtz": "11000001",
        "gez": "11000010",
        "isz": "11000011",
        "lez": "11000100",
        "ltz": "11000101",
        "noz": "11000110",
        "all": "11000111",
    }
    instruction_set = []
    try:
        with open(file_name) as f:
            lines = f.readlines()
    except:
        if file_name == '0': quit() #hardcode a way to quit cpu.py
        print(f"Invalid file name '{file_name}', is the extension correct?")
        return [] # return [] to continue asking for file
    for line in lines:
        line = line.split(';')[0].strip() # to ignore comment after instructions
        if not line or line.startswith(";"): # to ignore single line comment or empty line
            continue
        instr = line.split()
        binary = ''

        if instr[0] == "imm" and len(instr) == 2:
            if not (0 <= int(instr[1]) < 64): # only allow immediate from 0 to 63
                raise ValueError("Immediate out of range (0-63)")
            binary = f"00{int(instr[1]):06b}" # convert str to int to binary with padding

        elif instr[0] == "mov" and len(instr) == 3:
            try:
                if re.match(r"^reg[0-6]$",instr[1]): # if rega is in range 0 to 6
                    reg_a = f"{int(instr[1][-1]):03b}"
                elif instr[1] == "out": # reg7 is represented as out
                    reg_a = '111' 
                if re.match(r"^reg[0-6]$",instr[2]): # if regb is in range 0 to 6
                    reg_b = f"{int(instr[2][-1]):03b}"
                elif instr[2] == "out":
                    reg_b = '111'
            except:
                print(f"Invalid instruction: {line}")
            binary = "01"+reg_a+reg_b

        elif instr[0] == "cal" and len(instr) == 2:
            binary = CAL_OPS[instr[1]] 

        elif instr[0] == "jmp" and len(instr) == 2:
            binary = JMP_OPS[instr[1]]

        else:
            raise ValueError(f"Unknown instruction: {line}")
        instruction_set.append(binary)
    return instruction_set
    
