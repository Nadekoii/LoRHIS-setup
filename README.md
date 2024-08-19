# LoRHIS-setup
Everything you need to setup the LoRHIS project

## System Demo
<iframe width="560" height="315" src="https://www.youtube.com/embed/kN-17XNx0wQ?si=YUWwVEHYZ81-Hlpy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Github Repositories
All of the repositories for the LoRHIS project can be found below:

[LoRHIS - Front-end](https://github.com/Nadekoii/LoRHIS-frontend)

[LoRHIS - Back-end](https://github.com/Nadekoii/LoRHIS-backend)

[LoRHIS - Setup](https://github.com/Nadekoii/LoRHIS-setup)

## Recommended IDE
This IDE was originally used for the development of the project:
For UCA Board:
[Arduino IDE](https://www.arduino.cc/en/software/)
For Raspberry Pi's Python Script:
[Thonny](https://thonny.org)

## Project's Embedded Systems Setup
### UCA Board Setup
1. Install Arduino IDE on the machine
2. Clone/download and unzip the UCA21 repository
3. Follows the README.md of the UCA21 repository
4. Navigate to the repository and copy the PATH
5. Copy path and in Arduino IDE, File>Preferences set Sketchbook Location to the copied PATH
6. Download the downlinkNodeUCA.ino file in this setup repository
7. Connect UCA Board to the PC, make sure to select RFThings UCA as Board, if it doesn’t exist redo 3.
8. Verify and Upload code to UCA Board on the IDE
   
### UART Setup
![Raspberry-pin-out-Wiringpi](https://github.com/user-attachments/assets/995995b3-68d1-4e8c-9242-f39dbbe61883)
### Raspberry Pi Setup
1. Install [Raspberry Pi OS](https://www.raspberrypi.com/documentation/computers/getting-started.html) onto the Raspberry Pi
2. Update the Raspberry Pi 
```sh 
 sudo apt update
 sudo apt upgrade
```
3. Create an empty folder and navigate to said folder
```sh 
 mkdir Piper
 cd Piper/
```
4. Clone/Download the [Piper](https://github.com/rhasspy/piper) repository into the folder
5. Download the wanted [voice](https://github.com/rhasspy/piper/blob/master/VOICES.md) (guide on the Piper repository) into the same folder
6. Create and activate Python3 virtual environment using 
```sh
 python3 -m venv .venv
 source .venv/bin/activate
```
  Then install the Python's script required libraries
```sh
 pip3 install pydub
```
7. Download the read_serial.py script in the setup repository and put it in the same folder
8. Modify the PATHs in read_serial.py to the corresponding true PATHs
#### Optional
9. Download the autoStartScript.desktop file
10. Move the autoStartScript.desktop file to /home/raspberrypi/.config/autostart and rename it to <GUI Controller>
11. Modify the read_serial.py PATH inside <GUI Controller> to it's corresponding PATH
12. Enjoy the Python script automatically start on reboot !

### Known Bug
When running the Python Script, there might be a bug reading line 8:
```py
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Adjust the port name as identified
```
You can changes /dev/ttyUSB0 to /dev/ttyUSB1 and try again or the reverse (/dev/ttyUSB1 to /dev/ttyUSB0).
This is a known hardware problem of the Raspberry Pi where the USB port name changes when we unplug and replug the UCA Board.
