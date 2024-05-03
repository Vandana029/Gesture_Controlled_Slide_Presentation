import serial

# Initialize serial connection
ser = serial.Serial('COM4', 9600)  # Adjust 'COM3' to match your serial port and 9600 to match baud rate
# You may need to adjust the baud rate and port name based on your specific setup

while True:
    # Read a line of data from the serial port
    data = ser.readline().decode().strip()
    
    # Print the received data
    if data == 'N':
        print("Received: N")
        print(data)
    elif data == 'S':
        print("Received: S")
        print(data)
    elif data == 'U':
        print("Received: U")
        print(data)
