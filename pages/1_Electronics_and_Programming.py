import streamlit as st

st.set_page_config(page_title="Electronics and Programming", page_icon="💻")

st.markdown("# Electronics and Programming")
st.sidebar.header("Prototype construction and code development.")

st.subheader("Circuit Design")
st.markdown(
    """
    The circuit was designed to acquire vibration data using a Raspberry Pi Pico W, an MPU6050 accelerometer and a 0.96" I2C OLED display:
    - **Raspberry Pi Pico W:** Microcontroller with Wi-Fi connectivity.
    - **MPU6050 accelerometer:** Motion sensor that provides acceleration and rotation data.
    - **0.96" I2C OLED display:** Screen to show real-time information.
    """
)

st.image("images/protoboard.jpeg", caption="Prototype assembled on a breadboard", use_container_width=True)
st.markdown(
    """
    The image above shows the connections between components. The Pico communicates with the accelerometer and the OLED over I2C.
    """
)

st.subheader("Raspberry Pi Pico W Programming")

st.code(
"""
import socket
import network  # type: ignore
import time
import lib.secrets as secrets
from imu import MPU6050  # type: ignore
from ssd1306 import SSD1306_I2C  # type: ignore
from machine import I2C, Pin  # type: ignore

# Wi-Fi Connection
wifi = network.WLAN(network.STA_IF)  # Initialize the Wi-Fi interface
wifi.active(True)  # Activate the Wi-Fi interface
wifi.connect(secrets.SSID, secrets.PASSWORD)  # Connect to the Wi-Fi network using credentials from secrets.py
while not wifi.isconnected():  # Wait until connected to Wi-Fi
    print('Connecting to Wi-Fi')
    time.sleep(1)

# Server setup
UDP_IP = '192.168.0.19'  # Define the UDP server IP address
UDP_PORT = 1994  # Define the UDP server port
UDP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

# MPU6050 setup
i2c_mpu = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)  # Initialize I2C for MPU6050
mpu = MPU6050(i2c_mpu)  # Create MPU6050 object

# OLED setup
i2c_oled = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)  # Initialize I2C for OLED display
oled = SSD1306_I2C(128, 64, i2c_oled)  # Create OLED object with specified dimensions


def get_acceleration(mpu):
    '''
    Reads the acceleration values from the MPU6050 sensor and applies a calibration to the z-axis.
    The calibration adjusts the z-axis reading to account for sensor bias and gravitational force.
    Args:
        mpu: An object representing the MPU6050 sensor. It is expected to have an 'accel' attribute
                with x, y, and z attributes representing acceleration in each axis.
    Returns:
        A tuple containing the calibrated acceleration values (ax, ay, az) in g's.
    '''
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z - 0.02084873 * mpu.accel.z - 0.3439426
    return ax, ay, az
""",
    language="python"
)

st.subheader("Local UDP server programming")
st.code(
"""
import socket
import csv

UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 1994  # Port to listen on
UDP_SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
UDP_SERVER.bind((UDP_IP, UDP_PORT))  # Bind socket to address
print(f"UDP server started on {UDP_IP} port {UDP_PORT}")

CSV_FILE = "acceleration_data.csv"  # CSV file to store data
with open(CSV_FILE, mode="w", newline="") as file:  # Open CSV file in write mode
    writer = csv.writer(file)  # Create CSV writer object
    writer.writerow(["ax", "ay", "az"])  # Write header row
print(f"CSV file created: {CSV_FILE}")

while True:
    try:
        data, address = UDP_SERVER.recvfrom(65535)  # Receive data from UDP socket
        message = data.decode().strip()  # Decode data and remove whitespace
        print(f"Received packet from {address}")

        # Split the message into readings
        readings = message.split("\\n")

        # Open the CSV file to append the readings
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)

            # For each reading, split the data and write to the CSV file
            for i, reading in enumerate(readings):
                try:
                    measurement = reading.split(",")
                    ax = float(measurement[0])
                    ay = float(measurement[1])
                    az = float(measurement[2])
                    writer.writerow([ax, ay, az])
                except Exception as e:
                    print(f"Error processing line '{reading}': {e}")
            print(f"Packet with {i + 1} readings saved to {CSV_FILE}")

    except Exception as error:
        print(f"Error receiving or saving packet: {error}")
""",
    language="python"
)

