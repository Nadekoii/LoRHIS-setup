import subprocess
import time
import serial
from pydub import AudioSegment
from pydub.playback import play

# Serial Connection
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Adjust the port name as identified
time.sleep(2) # Wait for the serial connection to initialize
print("Starting")

while True:
    if ser.in_waiting > 0:
        print("Waiting serial:")
        message = ser.readline().decode('utf-8').rstrip()
        print("Received: "+ message)
        command = f"echo '{message}' | /home/raspberrypi/Piper/piper/piper --model /home/raspberrypi/Piper/vi_VN-vais1000-medium.onnx --output_file /home/raspberrypi/Piper/message.wav"
        # Call Piper console application with the message        
        subprocess.run(command, shell=True, check=True)        
        # Calculate the stop time (15 minutes from now)
        stop_time = time.time() + 15 * 60
        message_audio = AudioSegment.from_wav("/home/raspberrypi/Piper/message.wav")
        while time.time() < stop_time:
            subprocess.run(command, shell=True, check=True)
            # Wait for 10 seconds before repeating
            print("playing message audio")
            play(message_audio)
            time.sleep(30)
# Close the serial connection when needed, consider adding if(...)
ser.close()
