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
    This project covers the full pipeline from data acquisition to analysis and visualization. The goal was to build a complete vibration analysis system using accessible hardware and software tools.

    **Project Stages**:
    > *Use the sidebar pages to explore the different parts of the project.*

    1. **Electronics and Programming:**
        - Circuit design for vibration data acquisition using a Raspberry Pi Pico W, an MPU6050 accelerometer and a 0.96" I2C OLED display.
        - Programming the Pico in MicroPython to read the sensor, update the OLED, and send data via Wi-Fi to a local server. The code is optimized to collect data in real-time within the device memory limits.
        - Development of a local UDP server in Python to receive real-time data from the Pico.
    2. **3D Printing:**
        - CAD design and 3D printing of an enclosure to house the electronics and the Raspberry Pi Pico W. We show the design, materials used and the printing process.
    3. **Data Analysis:**
        - Data collection using the prototype mounted on a bench grinder.
        - Processing with Python and Pandas for cleaning and organizing the samples.
        - Time and frequency domain analysis using Numpy and Matplotlib (FFT) to inspect vibration characteristics.
    """
)
