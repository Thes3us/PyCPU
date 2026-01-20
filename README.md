# PyCPU
An (almost) turing complete CPU that can interpret assembly. It is purposefully made to mimick the low level interactions in a real CPU. It Has an ALU, CU, 7 registers of 1 byte, an output. Please refer the [Instructions](Instructions.md) to learn to write your own assembly or binary. Heavily inspired from OVERTURE architechture from the game "Turing complete"
## Requirements
- Python 3.x
- Git
## Getting Started
Follow these steps to get the project running locally:

1. **Clone the repository**
    ```sh
    git clone https://github.com/Thes3us/PyCPU.git
    cd PyCPU
    ```
2. **Run cpu.py**
    ```sh
    python cpu.py
    ```
3. **Run assembly**
- You can either write your own assembly, or load the demo file `print10num.asm`
## Additional info

in `cpu.py` you can choose to only display output register or see all of the registers at once. You may write your own assembly as a text file or `.asm` and save it in the same directory to use. There is also a demo program to print first 10 natural number in `print10num.asm`
## License
This project is licensed under the MIT License.



