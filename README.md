# Pure Digital Logic 4-Bit ALU & Comparator

This project is a hardware calculator built strictly on a breadboard using pure digital logic (no Microcontroller/MCU). It takes two 4-bit binary inputs via slide switches and outputs the decimal sum on a 7-segment display, along with LED status flags for Greater, Equal, and Less-than conditions.

## Hardware Required

* **74LS283**: 4-Bit Binary Full Adder
* **74LS85**: 4-Bit Magnitude Comparator
* **74LS47**: BCD to 7-Segment Decoder/Driver
* **7400**: Quad 2-Input NAND Gate (used for supplementary logic)
* **7-Segment Display**: Common Anode (compatible with 74LS47)
* **Slide Switches**: 8x individual slide switches (for Input A and Input B)
* **LEDs**: 3x LEDs for Comparator outputs (A > B, A = B, A < B)
* Resistors: 330Ω for LEDs/Display, 10kΩ pull-downs for slide switches
* Breadboard and Jumper Wires

## Features

1. **4-Bit Binary Addition**: Adds two 4-bit numbers (Input A and Input B). 
   > **Note on Display Limitation**: The 74LS47 decoder is designed for Binary Coded Decimal (BCD, 0-9). To display properly on a single 7-segment display with this hardware, inputs should be restricted so that the maximum sum is 9 (e.g., A=4, B=5). Sums 10-15 will result in non-alphanumeric characters.
2. **Magnitude Comparison**: Simultaneously compares the two 4-bit numbers and lights up the respective LED (A > B, A = B, or A < B).
3. **No MCU**: 100% pure hardware logic.

## Documentation

* [Truth Tables](docs/TRUTH_TABLES.md): Detailed logic tables for the Adder, Comparator, and Decoder.
* [Schematic Guide](docs/SCHEMATIC_GUIDE.md): Breadboard wiring instructions and block diagrams.
