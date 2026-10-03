# Schematic & Breadboard Guide

This guide explains how to wire the 4-Bit ALU & Comparator circuit using slide switches, 74LS series logic chips, and a 7-segment display.

## Block Diagram

```mermaid
flowchart TD
    subgraph Inputs
        SW_A[Slide Switches A \n 4 bits]
        SW_B[Slide Switches B \n 4 bits]
    end

    subgraph Logic
        Adder[74LS283 \n 4-Bit Adder]
        Comp[74LS85 \n 4-Bit Comparator]
        Decoder[74LS47 \n BCD Decoder]
        NAND[7400 NAND \n Extra Logic]
    end

    subgraph Outputs
        Display[7-Segment Display \n (Common Anode)]
        LED_G[LED: A > B]
        LED_E[LED: A = B]
        LED_L[LED: A < B]
    end

    SW_A --> |A1-A4| Adder
    SW_B --> |B1-B4| Adder
    
    SW_A --> |A1-A4| Comp
    SW_B --> |B1-B4| Comp

    Adder --> |Sum 1-4| Decoder
    Decoder --> |a-g (through 330Ω)| Display

    Comp --> |A > B| LED_G
    Comp --> |A = B| LED_E
    Comp --> |A < B| LED_L
```

## Wiring Instructions

### 1. Power & Ground
* Connect all chip `VCC` pins to the 5V rail.
* Connect all chip `GND` pins to the Ground rail.
* Ensure both power rails on the breadboard are connected.

### 2. Slide Switches (Inputs A and B)
You need 8 individual slide switches total (4 for Input A, 4 for Input B).
* Connect one side of each slide switch to `5V`.
* Connect the middle/output pin of each slide switch to the chip input pins (see below) AND to `Ground` through a 10kΩ pull-down resistor.
* When the switch is set to the 5V side, it sends Logic 1. When toggled, the resistor pulls it to `0V` (Logic 0).

### 3. The Adder (74LS283)
* **A Inputs**: Connect switches A1, A2, A3, A4 to pins 5, 3, 14, 12.
* **B Inputs**: Connect switches B1, B2, B3, B4 to pins 6, 2, 15, 11.
* **Carry-In (C0)**: Connect Pin 7 to `Ground`.
* **Sum Outputs (S1-S4)**: Connect pins 4, 1, 13, 10 to the inputs of the 74LS47.

### 4. The Comparator (74LS85)
* **A Inputs**: Connect switches A1-A4 to pins 10, 12, 13, 15.
* **B Inputs**: Connect switches B1-B4 to pins 9, 11, 14, 1.
* **Cascading Inputs**: 
  * Pin 3 (I A=B) -> `5V`
  * Pin 4 (I A<B) -> `Ground`
  * Pin 2 (I A>B) -> `Ground`
* **Outputs**: 
  * Pin 5 (A>B) -> LED with 330Ω resistor to Ground.
  * Pin 6 (A=B) -> LED with 330Ω resistor to Ground.
  * Pin 7 (A<B) -> LED with 330Ω resistor to Ground.

### 5. The Decoder (74LS47) & Display
* **Inputs (A, B, C, D)**: Connect from Adder Sum outputs to Pins 7, 1, 2, 6.
* **Outputs (a-g)**: Connect pins 13, 12, 11, 10, 9, 15, 14 to the corresponding segments on the 7-segment display.
* **Resistors**: Place a 330Ω resistor between each 74LS47 output and the display pin to prevent burning out the LEDs.
* **Display Common**: Connect the common pins of the 7-segment display to `5V` (Common Anode).

### 6. Extra Logic (7400 NAND)
If you wish to add a blink feature, a custom fault detector, or simple logic control over the display enable pins, the 7400 Quad NAND gate is available for expansion on the breadboard.
