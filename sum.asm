; to print sum of n natural numbers
imm 12          ; <-- SET N FOR LIMIT
mov reg0 reg5   ; store limit in reg5 
imm 1           ; init increment
mov reg0 reg1   ; move increment to first operand
cal add         ; add 1 and second operand
mov reg3 reg4   ; store counter to reg 4
mov reg3 reg2   ; move counter to second operand added with sum
mov reg6 reg1   ; move sum from reg 6 to first operant
cal add         ; add
mov reg3 reg6   ; store sum to reg 6 to be used in the next loop
mov reg5 reg1   ; move limit to first operand to check if >0
cal sub         ; sub limit and counter
imm 1           ; init jump position
jmp gtz         ; jump to instruction 2 if >0
mov reg6 out    ; after reaching limit, print sum 