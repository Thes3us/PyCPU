; assembly instruction to print first 10 natural numbers.
imm 10          ; init limit
mov reg0 reg4   ; store limit in reg4 for later use
imm 1           ; init increment
mov reg0 reg1   ; move increment to first operand
cal add         ; add increment + n to get counter
mov reg3 out    ; output n
mov reg3 reg2   ; move counter to second operant
mov reg4 reg1   ; mov limit to second operant
cal sub         ; sub to check if counter exceeds limit
imm 2           ; init jump position
jmp gtz         ; jump to instruction 1 if >0