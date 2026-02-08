# PyCPU
A custom 8-bit CPU emulator and Assembler written in Python. This project simulates the internal workings of a processor, including the fetch-decode-execute cycle, an ALU, and a CU. You can write programs in a custom Assembly language, compile them into machine code, and execute them on the virtual CPU. Please refer the [Instructions](Instructions.md) to learn to write your own assembly or binary code. Inspired from "OVERTURE" architecture from the game "Turing complete".
## Features
- **Assembler**: Converts human-readable Assembly instructions into 8-bit binary strings.
- **ALU**: Implements binary addition, subtraction, and logic gates (AND, OR, NAND, NOR) using bitwise operations.
- **Control Unit**: Handles conditional jumps based on flags.
- **Registers**: 8-register system (reg0 through reg7), with dedicated roles for operands and output.
- **Debug Mode**: Step-by-step execution visualization to watch register states change in real-time.
## Requirements
- Python 3.x
- Git
## Getting Started
Follow these steps to get the project running locally:
1. **Clone the repository**
    ```sh
    git clone https://github.com/Thes3us/PyCPU.git
    cd pycpu
    ```
2. **Run main.py**
    ```sh
    py src/main.py
    ```
3. **Run assembly**
- You can load your own code, or load the demo files `examples/sum.asm` or `examples/10num.asm`
## Architecture
The CPU operates on an 8-bit instruction set.
- **reg0**: General purpose & Jump Address buffer (Loaded via imm).
- **reg1 & reg2**: Input operands for ALU operations.
- **reg3**: Stores the result of ALU operations.
- **reg0 - reg6**: General purpose storage.
- **reg7 (out)**: Output register. When data is moved here, it is displayed to the console as a signed 8-bit integer.
## Additional info
in the program you may enable debug mode to see the states of all the registers in real time, or use the default mode to only see the output (register 7). You may write your own assembly as as `.txt` or `.asm` to use. There is also a demo program to print first 10 natural number in `examples/10num.asm` and a program to print the sum of first n natural number in `examples/sum.asm`
## License
This project is licensed under the MIT License.