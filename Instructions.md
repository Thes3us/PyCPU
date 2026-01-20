# INSTRUCTION SET 
## 1. Assembly
1. **imm** `<integer>`
- Example: `imm 35`
- Loads an immediate value into reg0.
- `<integer>` must be in the range 0–63.
2. **mov reg**`<a>` **reg**`<b>`
- Example: `mov reg0 reg1`
- moves the value from reg`<a>` into reg`<b>`.
- Can also be used to move a register value to the output (`out`).
- **NOTE**: range of a and b is 0 to 6.
3. **cal** `<operation>`
- Example: `cal add`
- Performs an arithmetic or logic operation on reg1 and reg2.
- Stores the result in reg3.
- Supported operations:
    - `add` – addition
    - `sub` – subtraction
    - `and` – bitwise AND
    - `nand` – bitwise NAND
    - `or` – bitwise OR
    - `nor` – bitwise NOR
4. **jmp** `<condition>`
- Example: `jmp gtz`
- Evaluates reg3 based on the specified condition.
- If the condition is satisfied, the execution jumps to the instruction address stored in reg0.
- Supported conditions:
    - `nvr` – never jump
    - `gtz` – reg3 > 0
    - `gez` – reg3 ≥ 0
    - `isz` – reg3 == 0
    - `lez` – reg3 ≤ 0
    - `ltz` – reg3 < 0
    - `noz` – reg3 ≠ 0
    - `all` – always jump
5. **;** `<comment>`
- Example: `; this is a comment`
- Any text after `;` is ignored.
## 2. Binary
**FORMAT**: `00000000`
1. **IMM**: `00 XXX XXX`
- Stores any value from 0 to 63 integers to reg 0.
2. **MOV**: `01 XXX YYY`
- Moves value from reg0-reg6 (XXX) to reg0-reg6.
- Can also move output value to register and vice verca.
    - 000 - reg0
    - 001 - reg1
    - 010 - reg2
    - 011 - reg3
    - 100 - reg4
    - 101 - reg5
    - 110 - reg6
    - 111 - output 
3. **CAL**: `10 000 XXX`
- Performs an arithmetic or logic operation on reg1 and reg2.
- Supported operations:
    - `000` - addition
    - `001` - substraction
    - `010` - bitwise AND
    - `011` - bitwise NAND
    - `100` - bitwise OR
    - `101` - bitwise NOR
4. **JMP**: `11 000 XXX` 
- Evaluates reg3 based on the specified condition.
- If the condition is satisfied, the execution jumps to the instruction address stored in reg0.
- Supported conditions: 
    - `000` – never jump
    - `001` - reg3 > 0
    - `010` - >=0
    - `011` - =0
    - `100` - <=0
    - `101` - <0
    - `110` - !=0
    - `111` - always

