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