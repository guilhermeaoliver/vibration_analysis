import streamlit as st

st.set_page_config(
    page_title="Introdução",
    page_icon="▶️",
)

st.write("# Projeto de Análise de Vibrações")

st.link_button("Autor: Guilherme Oliver", "https://www.linkedin.com/in/guilhermeaoliver/")

st.link_button("Repositório do Projeto", "https://github.com/guilhermeaoliver/vibration_analysis")

st.subheader("Introdução")

st.markdown(
    """
    Este é um projeto que abrange o ciclo completo desde a aquisição de dados até a análise e visualização. O objetivo foi construir um sistema completo para análise de vibrações, utilizando ferramentas de hardware e software acessíveis.

    **Etapas do Projeto:**
    > *Navegue pelas páginas na barra lateral à esquerda para explorar as diferentes etapas do projeto.*

    1. **Eletrônica e Programação:**
        - Projeto do circuito eletrônico para aquisição de dados de vibração utilizando uma Raspberry Pi Pico W, um acelerômetro MPU6050 e um display OLED 0.96" I2C.
        - Programação da Raspberry Pi Pico W utilizando MicroPython para comunicação com o acelerômetro (leitura dos dados), display OLED (exibição de informações relevantes) e envio dos dados via Wi-Fi para um servidor local. Abordamos a otimização do código para garantir a aquisição de dados em tempo real e limitações de memória do hardware.
        - Desenvolvimento de um servidor UDP local em Python para receber os dados em tempo real enviados pela Raspberry Pi Pico W.
    2. **Impressão 3D:**
        - Desenho da case utilizando software CAD e impressão 3D para acomodar os componentes eletrônicos e a Raspberry Pi Pico W de forma funcional. Apresentamos o design da case, os materiais utilizados e o processo de impressão.
    3. **Análise de Dados:**
        - Aquisição de dados de vibração utilizando o protótipo em um moto esmeril.
        - Processamento dos dados utilizando Python e a biblioteca Pandas para organização e limpeza dos dados.
        - Análise de vibrações no domínio do tempo e da frequência (a partir da Transformada Rápida de Fourier) utilizando as bibliotecas Numpy e Matplotlib.
    """
)
