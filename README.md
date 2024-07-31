# BettaFishFeeder
Simple script for a diy 3D printed Betta fish feeder

[3d Printed Files](https://cults3d.com/en/3d-model/gadget/betta-fish-feeder-f008684d7eb13b9ea993)

Requires:
- [RP2040 Zero microcontroller](https://s.click.aliexpress.com/e/_Dd9FU1Z)
- [28BYJ-48 Motor + Driver](https://s.click.aliexpress.com/e/_Dd9FU1Z)
- 2x M4 screws
- 6x M3 screws

## 1. Install MicroPython on the RP2040 Zero
Visit the official MicroPython download page for RP2040 boards: [MicroPython for PiPico](https://micropython.org/download/RPI_PICO/).
Download the latest .uf2 firmware file.

Flash the Firmware
Connect your RP2040 Zero to your computer via USB while holding down the BOOTSEL button to put it into USB mass storage mode.
The RP2040 Zero should appear as a USB drive on your computer.
Drag and drop the downloaded .uf2 file onto the RP2040 Zero's USB drive.
The board will reboot automatically, and MicroPython will be installed.

## 2. Connect to the RP2040 Zero Using Thonny
Download and install Thonny from the [Thonny website](https://thonny.org/).
Open Thonny.
Go to Tools > Options and select the Interpreter tab.
Set the interpreter to "MicroPython (Raspberry Pi Pico)".
Select the correct port for your RP2040 Zero from the Port dropdown menu.
Click OK to save the settings.

## 3. Upload a Script to the RP2040 Zero
Upload both main.py and at24c32n.py to RP2040 Zero
Right-Click over the selected Files.
Click on "Upload to /".

[Youtube Tutorial](https://www.youtube.com/watch?v=FtlYC5Xqgns)
