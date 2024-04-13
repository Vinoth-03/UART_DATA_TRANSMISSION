# UART Data Transmission 

Welcome to the UART Data Transmission repository! This project is dedicated to enabling bidirectional data communication between a PC and an Arduino UNO using the UART protocol. It's designed to not only transfer text data efficiently but also to measure the data transmission speed in real-time.

## Project Structure

### `TransmissionPC.py`
A Python script that is responsible for sending text data to the Arduino, one character at a time. It also measures and displays the data transmission and reception speeds in bits per second.

### `TransmissionMCU.ino`
An Arduino sketch that is crucial for receiving data from the PC, storing it in EEPROM, and sending it back upon request.

## Directory Contents

- **TransmissionPC**: This directory contains the PC-side script, `TransmissionPC.py`, which manages data transmission and displays received data.

- **TransmissionMCU**: This directory contains the MCU firmware, `TransmissionMCU.ino`, written in Embedded C/C++, which handles data reception, storage, and transmission.

## Getting Started

### Prerequisites
- Python 3.x installed on your PC.
- An Arduino Uno or a compatible microcontroller board.
- A standard USB cable to establish a connection with the PC.
- A USB to UART bridge for smooth communication

### Installation and Operation
1. Connect the Arduino Uno to the PC using the USB cable.
2. Upload the `TransmissionMCU.ino` sketch to the Arduino Uno.
3. Run the `TransmissionPC.py` script on the PC.
4. Make sure the correct COM port for the Arduino Uno is specified in the script.

## Note
The Arduino code provided avoids the use of standard libraries such as `EEPROM.h`. All EEPROM read and write functionalities are implemented from the ground up, without external libraries.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to the UART community and all contributors who have made this project possible.


