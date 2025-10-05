import streamlit as st
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title="Vibration Analysis", page_icon="📈")

st.markdown("# Vibration Analysis")
st.sidebar.header("Acquisition and analysis of vibration data")

st.subheader("Data Acquisition")
st.markdown(
    """
    The data for this analysis were collected as shown in the video below.

    The device was positioned on a bench grinder. Acquisition started with the grinder off, then it was turned on and run for a few minutes before being turned off again.
    """
)

st.video("https://www.youtube.com/watch?v=mVAaTQE6XIs")

st.markdown(
    """
    Data were sampled at 200 Hz for a total duration of 163 seconds.

    The sampling frequency should be at least twice the resonance frequency to guarantee accurate capture of the system dynamics. Choosing 200 Hz ensures the resonance frequency of the tested system is captured.
    """
)

# Read and process data
df = pd.read_csv("server/acceleration_data.csv")
N = len(df)
fs = 200
T = 1 / fs
df['t'] = np.arange(0, N/fs, T)

st.subheader("Acceleration in the Time Domain")

st.markdown(
    """
    Acceleration was measured on three axes: X, Y and Z. The plots below show acceleration for each axis over time.
    """
)

fig = make_subplots(rows=3, cols=1, subplot_titles=('Acceleration X (g)', 'Acceleration Y (g)', 'Acceleration Z (g)'))

fig.add_trace(go.Scatter(x=df['t'], y=df['ax'], name='X', line=dict(color='#8BE9FD')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['t'], y=df['ay'], name='Y', line=dict(color='#50FA7B')), row=2, col=1)
fig.add_trace(go.Scatter(x=df['t'], y=df['az'], name='Z', line=dict(color='#FFB86C')), row=3, col=1)

fig.update_layout(height=1800, showlegend=True)
fig.update_xaxes(title_text="Time (s)")
fig.update_yaxes(title_text="Acceleration (g)")

st.plotly_chart(fig, use_container_width=True)

st.subheader("Frequency Analysis (FFT)")

st.markdown(
    """
    Frequency analysis was performed using the Fast Fourier Transform (FFT). The FFT transforms a time-domain signal into the frequency domain and highlights frequency components.
    """
)

f = np.fft.fftfreq(N, T)
fft_x = np.abs(np.fft.fft(df['ax']))
fft_y = np.abs(np.fft.fft(df['ay']))
fft_z = np.abs(np.fft.fft(df['az']))

bins = np.arange(0, int(fs / 2) + 1)

fft_x_binned = np.histogram(f[f > 0], bins=bins, weights=fft_x[f > 0])[0] / np.histogram(f[f > 0], bins=bins)[0]
fft_y_binned = np.histogram(f[f > 0], bins=bins, weights=fft_y[f > 0])[0] / np.histogram(f[f > 0], bins=bins)[0]
fft_z_binned = np.histogram(f[f > 0], bins=bins, weights=fft_z[f > 0])[0] / np.histogram(f[f > 0], bins=bins)[0]

fig_fft = make_subplots(rows=3, cols=1, subplot_titles=('FFT X', 'FFT Y', 'FFT Z'))

fig_fft.add_trace(go.Scatter(x=bins, y=fft_x_binned, name='X', line=dict(color='#8BE9FD')), row=1, col=1)
fig_fft.add_trace(go.Scatter(x=bins, y=fft_y_binned, name='Y', line=dict(color='#50FA7B')), row=2, col=1)
fig_fft.add_trace(go.Scatter(x=bins, y=fft_z_binned, name='Z', line=dict(color='#FFB86C')), row=3, col=1)

fig_fft.update_layout(height=1800, showlegend=True)
fig_fft.update_xaxes(title_text="Frequency (Hz)")
fig_fft.update_yaxes(title_text="Amplitude")

st.plotly_chart(fig_fft, use_container_width=True)

st.markdown(
    """
    Peaks in the FFT indicate dominant frequency components, which may be related to system resonances or environmental sources such as the mains frequency (~60 Hz).
    """
)
