# Gesture_Controlled_Slide_Presentation
**Gesture Controlled PPT Slide Presentation - README**
 *Demo OutPut:*
 https://indianinstituteofscience-my.sharepoint.com/:v:/g/personal/saylisantosh_iisc_ac_in/EYkqw3X3GgJFucVsfOE00s4BmcyrR_1gBI02yrlHW96tjw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=lclP4S
 
*Project Overview:*
 
The Gesture Controlled PPT Slide Presentation project aims to provide a seamless and intuitive interface for navigating PowerPoint slides using hand gestures. By leveraging edge AI technology and gesture recognition algorithms, users can interact with presentations in a more natural and accessible manner, overcoming traditional input limitations such as mouse clicks or keyboard commands.
 
*Files Included:*
 
1. **Arrowkey.py**:
   - Python script responsible for receiving gesture data from the Arduino Nano BLE Sense board and controlling Computer applications accordingly.
   - Utilizes the `pyautogui` library for simulating keyboard presses.
   - Communicates with the Arduino Nano BLE Sense board via serial communication.
 
2. **lab3.ino**:
   - Arduino sketch for the Arduino Nano BLE Sense board.
   - Implements gesture recognition using an onboard IMU sensor.
   - Transmits gesture data to the connected PC via Bluetooth Low Energy (BLE).
   - Integrates with the Python script to enable gesture-controlled slide navigation.
 
3. **Gesture Dataset JSON Files**:
   - Contains the dataset of gestures (N, S, U, X) representing the four keyboard arrow keys.
   - Used for training and testing the machine learning model on the Arduino Nano BLE Sense board.
 
*Setup Instructions:*
 
1. Connect the Arduino Nano BLE Sense board to your computer using a USB cable.
2. Upload the `lab3.ino` sketch to the Arduino Nano BLE Sense board using the Arduino IDE.
3. Install the required Python dependencies by running `pip install pyautogui serial`.
4. Ensure that PowerPoint is installed on your computer and have a presentation ready for testing.
5. Open `Arrowkey.py` and modify the `filepath` variable to point to your PowerPoint presentation file.
6. Adjust the COM port in the `serial.Serial()` constructor to match the port to which the Arduino Nano BLE Sense board is connected.
7. Run the `Arrowkey.py` script to start the gesture-controlled PowerPoint slide navigation.
 
*Usage:*
 
1. Power on the Arduino Nano BLE Sense board and ensure that it is connected to the computer via BLE.
2. Execute the `Arrowkey.py` script on your computer.
3. Perform the predefined hand gestures (N, S, U, X) to navigate through PowerPoint slides.
4. Monitor the console output for debugging information and confirmation of received gestures.
 
*Notes:*
 
- Ensure that the IMU sensor on the Arduino Nano BLE Sense board is calibrated and functioning properly for accurate gesture recognition.
- Experiment with different gesture recognition models and parameters to optimize performance and accuracy.
- Customize the Python script and Arduino sketch as needed to adapt to specific presentation requirements or user preferences.
