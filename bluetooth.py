import serial
#from serial.serialutil import SerialException
# Define the Bluetooth port
#bluetooth_port = '/dev/tty.ttyUSB8'  # Replace 'XXXXXX' with the correct port name on your system
bluetooth_port = 'COM8'
# Open the serial port
try:
    ser = serial.Serial(port=bluetooth_port, baudrate=9600, timeout=1)
    #ser = serial.Serial(bluetooth_port, 9600, timeout=1)
    print("Connected to Bluetooth port:", bluetooth_port)
    print('***')
except Exception as e:
    print("Error opening Bluetooth port:", e)
    exit()
print("outside of try")
# Read data from the serial port
try:
    print("inside of try")
    while True:
        print("inside of while")
        data = ser.read()
        print(data)
        if data:
            max_index = int.from_bytes(data, byteorder='big')
            print("Received:", data)
except KeyboardInterrupt:
    print("Keyboard interrupt, closing port.")
    ser.close()
