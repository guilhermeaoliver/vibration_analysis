import streamlit as st
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title="Análise de Vibrações", page_icon="📈")

st.markdown("# Análise de Vibrações")
st.sidebar.header("Aquisição e análise dos dados de vibrações")

st.subheader("Aquisição de Dados")
st.markdown(
    """
    A aquisição dos dados desta análise foi feita conforme exibido no vídeo abaixo.

    O protótipo foi posicionado em cima do moto esmeril.
    A aquisição começou com o moto esmeril desligado que, em seguida foi ligado e deixado em funcionamento por alguns minutos e desligado novamente.
    """
)

st.video("https://www.youtube.com/watch?v=mVAaTQE6XIs")

st.markdown(
    """
    Os dados foram adquiridos com a frequência de 200 Hz, e o tempo total de aquisição foi de 163 segundos.

    A frequência de amostragem deve ser pelo menos o dobro da frequência de ressonância para garantir que os dados sejam capturados com precisão.
    Portanto, a escolha de 200 Hz como frequência de amostragem foi feita para garantir que a frequência de ressonância do sistema fosse capturada com precisão.
    A frequência de ressonância do sistema é a frequência na qual o sistema vibra com maior amplitude, e é importante para entender o comportamento dinâmico do sistema.
    """
)

# Leitura e processamento dos dados
df = pd.read_csv("server/acceleration_data.csv")
N = len(df)                     # Número de amostras
fs = 200                        # Frequência de amostragem (Hz)
T = 1 / fs                      # Período de amostragem (s)
df['t'] = np.arange(0, N/fs, T) # Tempo (s)

# Gráficos no domínio do tempo
st.subheader("Aceleração no Domínio do Tempo")

st.markdown(
    """
    A aceleração foi medida em três eixos: X, Y e Z. Os gráficos abaixo mostram a aceleração em cada eixo ao longo do tempo.

    A aceleração é uma medida da taxa de variação da velocidade de um objeto em movimento. Ela é expressa em unidades de gravidade (g), onde 1 g é igual à aceleração devido à gravidade na superfície da Terra (aproximadamente 9,81 m/s²).
    """
)

fig = make_subplots(rows=3, cols=1, subplot_titles=('Aceleração no Eixo X (g)', 'Aceleração no Eixo Y (g)', 'Aceleração no Eixo Z (g)'))

fig.add_trace(go.Scatter(x=df['t'], y=df['ax'], name='X', line=dict(color='#8BE9FD')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['t'], y=df['ay'], name='Y', line=dict(color='#50FA7B')), row=2, col=1)
fig.add_trace(go.Scatter(x=df['t'], y=df['az'], name='Z', line=dict(color='#FFB86C')), row=3, col=1)

fig.update_layout(height=1800, showlegend=True)
fig.update_xaxes(title_text="Tempo (s)")
fig.update_yaxes(title_text="Aceleração (g)")

st.plotly_chart(fig, use_container_width=True)

# Gráficos no domínio da frequência
st.subheader("Análise de Frequência (FFT)")

st.markdown(
    """
    A análise de frequência foi realizada utilizando a Transformada Rápida de Fourier (FFT). A FFT é uma técnica matemática que transforma um sinal do domínio do tempo para o domínio da frequência.

    A FFT fornece informações sobre as frequências presentes no sinal e suas respectivas amplitudes. Isso é útil para identificar padrões e características do sinal que podem não ser visíveis no domínio do tempo.
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

fig_fft = make_subplots(rows=3, cols=1, subplot_titles=('Transformada Rápida de Fourier no Eixo X', 'Transformada Rápida de Fourier no Eixo Y', 'Transformada Rápida de Fourier no Eixo Z'))

fig_fft.add_trace(go.Scatter(x=bins, y=fft_x_binned, name='X', line=dict(color='#8BE9FD')), row=1, col=1)
fig_fft.add_trace(go.Scatter(x=bins, y=fft_y_binned, name='Y', line=dict(color='#50FA7B')), row=2, col=1)
fig_fft.add_trace(go.Scatter(x=bins, y=fft_z_binned, name='Z', line=dict(color='#FFB86C')), row=3, col=1)

fig_fft.update_layout(height=1800, showlegend=True)
fig_fft.update_xaxes(title_text="Frequência (Hz)")
fig_fft.update_yaxes(title_text="Amplitude")

st.plotly_chart(fig_fft, use_container_width=True)

st.markdown(
    """
    Observamos que a FFT apresenta picos em determinadas frequências, indicando a presença de componentes de frequência específicas no sinal.
    Esses picos podem estar relacionados a ressonâncias do sistema, como o pico nos 71Hz ou a outras características dinâmicas do sistema,
    como o pico próximo dos 60Hz que é a frequência nominal da rede elétrica.
    """
)