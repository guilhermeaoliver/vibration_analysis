import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="▶️",
)

st.write("# Vibration Analysis Project")

st.link_button("Author: Guilherme Oliver", "https://www.linkedin.com/in/guilhermeaoliver/")

st.link_button("Project Repository", "https://github.com/guilhermeaoliver/vibration_analysis")

st.subheader("Introduction")

st.markdown(
    """
    This is a project that covers the complete cycle from data acquisition to analysis and visualization. The goal was to build a complete system for vibration analysis, using accessible hardware and software tools.

    **Project Steps:**
    > *Navigate through the pages in the left sidebar to explore the different project steps.*

    1. **Electronics and Programming:**
        - Design of the electronic circuit for vibration data acquisition using a Raspberry Pi Pico W, an MPU6050 accelerometer, and a 0.96" I2C OLED display.
        - Programming of the Raspberry Pi Pico W using MicroPython for communication with the accelerometer (data reading), OLED display (displaying relevant information), and sending data via Wi-Fi to a local server. We address code optimization to ensure real-time data acquisition and hardware memory limitations.
        - Development of a local UDP server in Python to receive real-time data sent by the Raspberry Pi Pico W.
    2. **3D Printing:**
        - Design of the case using CAD software and 3D printing to accommodate the electronic components and the Raspberry Pi Pico W in a functional way. We present the case design, the materials used, and the printing process.
    3. **Data Analysis:**
        - Acquisition of vibration data using the prototype on a bench grinder.
        - Data processing using Python and the Pandas library for data organization and cleaning.
        - Vibration analysis in the time and frequency domain (from the Fast Fourier Transform) using the Numpy and Matplotlib libraries.
    """
)
