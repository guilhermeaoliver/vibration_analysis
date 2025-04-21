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

        # Split the message into readings, each with four measurements
        readings = message.split("\n")

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
