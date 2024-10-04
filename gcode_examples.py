# G90 G0 X0 Y0
# G21G91G1Y10F350
# G21G91G1X10Y10F350
# G21G91G1X10F350
# G21G91G1X10Y-10F350
# G21G91G1Y-10F350
# G21G91G1X-10Y-10F350
# G21G91G1X-10F350
# G21G91G1X-10Y10F350
# M03 S000
# M03 S089

# COM5

import serial
import time

# Open grbl serial port (adjust the port based on your system)
s = serial.Serial('COM5', 115200)

# Wake up grbl
s.write(b"\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

print("Interactive G-code Console (Type 'exit' to quit)\n")

while True:
    # Get user input (G-code command)
    gcode_input = input("Enter G-code: ").strip()

    # Check if user wants to exit
    if gcode_input.lower() == 'exit':
        break

    # Send G-code to GRBL
    s.write((gcode_input + '\n').encode('utf-8'))  # Send G-code block to GRBL
    
    # Wait for response from GRBL
    grbl_out = s.readline().decode('utf-8').strip()
    print("Response: " + grbl_out)

# Close serial port
s.close()

print("GRBL session closed.")
