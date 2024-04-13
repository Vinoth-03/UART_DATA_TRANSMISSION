# UART Data Transmission Firmware

Welcome to the UART Data Transmission repository! This project is all about seamless and efficient communication between a personal computer (PC) and an Arduino UNO microcontroller. Using the Universal Asynchronous Receiver-Transmitter (UART) protocol, this firmware facilitates not just the transfer of text data but also measures the speed of data flow in real-time.

## Project Structure

### `FinalPC.py`
A Python script that takes the lead in sending text data to the Arduino, character by character. It's smart enough to calculate and display the data transmission and reception rates in bits per second.

### `FinalMCU.ino`
An Arduino sketch that plays a crucial role in receiving data from the PC, safeguarding it within the EEPROM, and echoing it back when asked.

## Directory Contents

- **FinalPC**: This directory is the command center for the PC-side operations, housing the `FinalPC.py` script.

- **FinalMCU**: Consider this the brain of the microcontroller unit, containing the `FinalMCU.ino` sketch written in Embedded C/C++.

## Getting Started

### Prerequisites
- Python 3.x installed on your PC.
- An Arduino Uno or a compatible microcontroller board.
- A standard USB cable to establish a connection with the PC.
- A USB to UART bridge for smooth communication.

### Installation and Operation
1. Begin by connecting the Arduino Uno to your PC using the USB cable.
2. Flash the `FinalMCU.ino` onto your Arduino to breathe life into it.
3. Fire up the `FinalPC.py` script on your PC to start the conversation.
4. Double-check that you've selected the right COM port in the script for your Arduino.

## A Note to the Users
We've taken a minimalist approach here, avoiding the use of any pre-cooked libraries like `EEPROM.h`. Every function related to EEPROM operations is crafted from scratch, giving you a lean and mean codebase.



## Acknowledgments
A shoutout to all UART enthusiasts and the open-source community for the inspiration and support.



