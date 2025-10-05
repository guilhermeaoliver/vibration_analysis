# Vibration Analysis Project

## Overview

This repository contains the files and documentation for a vibration analysis project developed as an educational exercise. The project is divided into the following components:

- **Data acquisition on Raspberry Pi Pico W:** Code to read acceleration data from an MPU6050 accelerometer, send the data over the local Wi-Fi network, and display information on a 0.96" OLED screen.
- **Server application:** Code running on the local machine to receive and process data sent by the Raspberry Pi Pico.
- **3D printed models:** CAD files for a custom enclosure to house the Pico and related electronics.
- **Streamlit:** An interactive web interface to visualize collected data, perform vibration analysis, and present additional project information.

## Repository structure
```
vibration_analysis/
├── raspberry_pi_pico/  # Data acquisition code for Raspberry Pi Pico W
│   ├── lib/            # Libraries used on the device
│   └── main.py         # Main script running on the Pico
├── server/             # Server application to receive data
│   ├── server.py       # Main server code
│   └── acceleration_data.csv # Collected data
├── 3d_printed_models/  # 3D model files for the enclosure
│   ├── case_bottom.step
│   └── case_top.step
└── pages/              # Streamlit pages for the web interface
```

## Component details

### Raspberry Pi Pico W (`raspberry_pi_pico/`)

This folder contains the code to run on the Raspberry Pi Pico W. The main goal is to collect vibration data with the MPU6050 and send it to the server.

- `lib/`: Additional libraries used on the Pico, such as drivers for the MPU6050 and the OLED display.
- `main.py`: The main script that reads accelerometer data, connects to Wi-Fi to send data, and updates the OLED display.

### Server application (`server/`)

The server receives data sent by the Raspberry Pi Pico W, processes it, and stores it.

- `server.py`: Implements the server logic, including receiving UDP packets, parsing the measurements, and appending them to a CSV file.
- `acceleration_data.csv`: CSV file where received acceleration samples are stored.

### 3D printed models (`3d_printed_models/`)

Contains the CAD files for the 3D printed enclosure that houses the Pico W and the electronics.

- `case_bottom.step`: STEP file with the bottom part design.
- `case_top.step`: STEP file with the top part design.

### Streamlit (`pages/`)

This folder contains the files needed to run the Streamlit web interface.

- `Introduction.py`: Streamlit page that provides an overview of the project, displays collected data, and explains the vibration analysis performed in the project.