# Importing Libraries

def switchcontrol():

    import serial
    import time

    arduino = serial.Serial(port='/dev/cu.usbmodem14201', baudrate=115200, timeout=.1)
    arduino.write(11)
    arduino.write(0)

switchcontrol()
  
      