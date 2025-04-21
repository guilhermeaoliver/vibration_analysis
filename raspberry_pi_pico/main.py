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
    """
    Reads the acceleration values from the MPU6050 sensor and applies a calibration to the z-axis.
    The calibration adjusts the z-axis reading to account for sensor bias and gravitational force.
    Args:
        mpu: An object representing the MPU6050 sensor. It is expected to have an 'accel' attribute
                with x, y, and z attributes representing acceleration in each axis.
    Returns:
        A tuple containing the calibrated acceleration values (ax, ay, az) in g's.
        ax: Acceleration in the x-axis.
        ay: Acceleration in the y-axis.
        az: Calibrated acceleration in the z-axis.
    """
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z - 0.02084873 * mpu.accel.z - 0.3439426
    return ax, ay, az


# Pre-allocate the readings list and the message buffer
NUM_READINGS = 200
readings = [None] * NUM_READINGS  # Pre-allocate list
message_buffer = bytearray(25 * NUM_READINGS)  # Pre-allocate byte array for the message

while True:
    # Collect readings from the MPU6050 sensor
    for i in range(NUM_READINGS):
        ax, ay, az = get_acceleration(mpu)  # Get calibrated acceleration values
        readings[i] = "{:.4f}, {:.4f}, {:.4f}".format(ax, ay, az)  # Format and store the reading
        time.sleep(0.005)  # Delay for 5ms

    # Construct the message directly into the buffer
    message_len = 0
    for reading in readings:
        encoded_reading = reading.encode()
        message_buffer[message_len:message_len + len(encoded_reading)] = encoded_reading
        message_len += len(encoded_reading)
        message_buffer[message_len] = 10  # Add newline character
        message_len += 1

    # Send the message to the UDP server, using a memoryview to avoid copying
    UDP_SERVER.sendto(memoryview(message_buffer)[:message_len], (UDP_IP, UDP_PORT))

    # Clear the OLED display
    oled.fill(0)
    oled.show()

    # Display acceleration values on the OLED
    oled.text("Acceleration:", 0, 0)
    oled.text("ax: {:.2f} G".format(ax), 0, 20)
    oled.text("ay: {:.2f} G".format(ay), 0, 30)
    oled.text("az: {:.2f} G".format(az), 0, 40)
    oled.show()  # Update the OLED display
