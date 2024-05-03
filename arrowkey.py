import time
import os
from pyautogui import press
import serial

def open_powerpoint(filepath):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = True
    presentation = powerpoint.Presentations.Open(filepath)
    return powerpoint, presentation

def start_slide_show(powerpoint):
    presentation = powerpoint.ActivePresentation
    presentation.SlideShowSettings.Run()

def stop_slide_show(powerpoint):
    try:
        slide_show_window = powerpoint.ActivePresentation.SlideShowWindow
        slide_show_window.View.Exit()
    except Exception as e:
        print("Error:", e)

def next_slide(powerpoint):
    try:
        slide_show_window = powerpoint.ActivePresentation.SlideShowWindow
        slide_show_window.View.Next()
    except Exception as e:
        print("Error:", e)

def previous_slide(powerpoint):
    try:
        slide_show_window = powerpoint.ActivePresentation.SlideShowWindow
        slide_show_window.View.Previous()
    except Exception as e:
        print("Error:", e)

def main():
    # Initialize serial connection
    ser = serial.Serial('COM8', 9600)  # Adjust 'COM3' to match your serial port and 9600 to match baud rate
    # You may need to adjust the baud rate and port name based on your specific setup


    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode().strip()
        
        # Print the received data
        if data == 'N':
            print("Received: N")
            press('right')
        elif data == 'S':
            print("Received: S")
            press('down')
        elif data == 'U':
            print("Received: U")
        elif data == 'X':
            print("Received: X")
            press('left')


if __name__ == "__main__":
    main()
