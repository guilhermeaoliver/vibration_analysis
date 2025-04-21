# Projeto de Análise de Vibrações 

## Visão Geral

Este repositório contém os arquivos e documentação de um projeto de análise de vibrações desenvolvido por mim para fins didáticos. O projeto é dividido nos seguintes componentes:

- **Aquisição de dados no Raspberry Pi Pico W:** O código engloba a aquisição de dados de aceleração de um acelerômetro MPU6050, envio dos dados pela rede Wi-Fi local e exibição dos dados em uma tela OLED de 0.96".
- **Aplicação Servidor:** Código executado na máquina local para receber e processar dados enviados pelo Raspberry Pi Pico, via Wi-Fi.
- **Modelos Impressos em 3D:** Arquivos de design para uma case personalizada para abrigar o Raspberry Pi e os componentes associados.

## Estrutura do Repositório
```
vibration_analysis/
├── raspberry_pi_pico/  # Aquisição de dados no Raspberry Pi Pico W
│   ├── lib/            # Bibliotecas usadas no projeto
│   └── main.py         # Código principal executado no Raspberry Pi Pico W
├── server/                    # Aplicação servidor para recepção de dados
│   ├── server.py              # Código principal do servidor
│   └──  acceleration_data.csv # Dados coletados
└── 3d_printed_models/    # Modelos 3D para a case
    ├── case_bottom.step  # Arquivo STEP com a parte inferior da case
    └── case_top.step     # Arquivo STEP com a parte superior da case
```

## Detalhes dos Componentes

### Raspberry Pi Pico W (`raspberry_pi_pico/`)

Esta pasta contém todo o código necessário para rodar no Raspberry Pi Pico W. O objetivo principal é coletar dados de vibração usando o acelerômetro MPU6050 e enviá-los para o servidor.

- `lib/`: Contém bibliotecas adicionais utilizadas no projeto, como drivers para o MPU6050 e para a tela OLED.
- `main.py`: É o script principal que controla a leitura dos dados do acelerômetro, a comunicação Wi-Fi para enviar os dados e a exibição das informações na tela OLED.

### Aplicação Servidor (`server/`)

Responsável por receber os dados enviados pelo Raspberry Pi Pico W, processá-los e armazená-los.

- `server.py`: Implementa a lógica do servidor, incluindo a recepção de dados via Wi-Fi, o tratamento dos dados recebidos e o armazenamento em um arquivo.
- `acceleration_data.csv`: Arquivo onde os dados de aceleração recebidos são armazenados em formato CSV (Comma Separated Values).

### Modelos Impressos em 3D (`3d_printed_models/`)

Contém os arquivos de design para a case impressa em 3D que acomoda o Raspberry Pi Pico W e seus componentes.

- `case_bottom.step`: Arquivo STEP (Standard for the Exchange of Product Data) contendo o design da parte inferior da case.
- `case_top.step`: Arquivo STEP contendo o design da parte superior da case.
