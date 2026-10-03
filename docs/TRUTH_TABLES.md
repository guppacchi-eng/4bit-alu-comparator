# Truth Tables

This document outlines the logic behavior for the core components of the 4-Bit ALU and Comparator project.

## 1. 4-Bit Adder (74LS283)

The 74LS283 adds two 4-bit binary words (A and B) plus a Carry-In (C0).
Since we are only doing basic addition, **C0 is tied to Ground (0)**.

| Input A (A4 A3 A2 A1) | Input B (B4 B3 B2 B1) | Sum (S4 S3 S2 S1) | Carry Out (C4) | Decimal Equivalent |
| :--- | :--- | :--- | :--- | :--- |
| 0000 | 0000 | 0000 | 0 | 0 + 0 = 0 |
| 0001 | 0001 | 0010 | 0 | 1 + 1 = 2 |
| 0011 | 0010 | 0101 | 0 | 3 + 2 = 5 |
| 0100 | 0101 | 1001 | 0 | 4 + 5 = 9 |
| 1111 | 1111 | 1110 | 1 | 15 + 15 = 30 |

## 2. 4-Bit Magnitude Comparator (74LS85)

The 74LS85 compares two 4-bit binary words (A and B) and sets one of three outputs high: A > B, A = B, or A < B.
To work correctly, the cascading inputs must be set as follows: `I(A=B) = High (5V)`, `I(A<B) = Low (GND)`, `I(A>B) = Low (GND)`.

| Input A | Input B | A > B Output | A = B Output | A < B Output |
| :--- | :--- | :---: | :---: | :---: |
| A > B | Any | **1** | 0 | 0 |
| A < B | Any | 0 | 0 | **1** |
| A = B | Any | 0 | **1** | 0 |

*Example values:*
* A=0100 (4), B=0011 (3) -> A > B is High.
* A=0101 (5), B=0101 (5) -> A = B is High.

## 3. BCD to 7-Segment Decoder (74LS47)

The 74LS47 translates a 4-bit Binary Coded Decimal (BCD) input into the 7 logic states required to illuminate a Common Anode 7-segment display. Since it is active-low, a `0` turns the segment ON.

| Decimal | BCD Input (D C B A) | a | b | c | d | e | f | g |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0000 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0001 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 2 | 0010 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 3 | 0011 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 9 | 1001 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

*(Inputs > 9 will result in invalid symbols, so restrict A + B <= 9).*
