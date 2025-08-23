# 🤖 Projeto Guardião Sênior: Assistente Inteligente com UNIHIKER K10

![GitHub Repo stars](https://img.shields.io/github/stars/IAjmsmf/UNIHIKER-K10?style=social)
![GitHub forks](https://img.shields.io/github/forks/IAjmsmf/UNIHIKER-K10?style=social)
![GitHub license](https://img.shields.io/github/license/IAjmsmf/UNIHIKER-K10)

Um assistente inteligente de código aberto para idosos, utilizando IA embarcada na placa UNIHIKER K10 para promover mais segurança e autonomia.

<!-- ADICIONE UMA FOTO DO SEU PROJETO MONTADO AQUI QUANDO TIVER UMA -->
<!-- Ex: <p align="center"><img src="./assets/foto_projeto.jpg" width="600"></p> -->

---

## 📖 Sobre o Projeto

O envelhecimento da população é uma realidade global, trazendo consigo a necessidade de soluções inovadoras que garantam a segurança, saúde e autonomia dos idosos. Muitos vivem sozinhos e necessitam de um acompanhamento constante que, muitas vezes, familiares e cuidadores não conseguem prover 24/7.

O **Projeto Guardião Sênior** nasce como uma solução de baixo custo e código aberto para este desafio. Utilizando a poderosa placa de desenvolvimento **UNIHIKER K10**, desenvolvemos um assistente que atua como um companheiro proativo, combinando o potencial da IA embarcada (*Embedded AI*) com a Internet das Coisas (IoT) para oferecer funcionalidades como reconhecimento de voz, detecção de presença e notificações inteligentes.

Todo o processamento principal ocorre localmente na placa, garantindo a privacidade do usuário e o funcionamento mesmo sem conexão constante à internet.

---

## ✨ Funcionalidades Principais

*   🗣️ **Interação por Voz Simplificada:** Comandos de voz offline para consultar horas, agendar lembretes e confirmar a toma de medicamentos.
*   💊 **Notificações Inteligentes de Medicação:** Alertas visuais na tela de 2.8" e sonoros para lembrar os horários dos remédios.
*   👀 **Detecção de Presença e Bem-estar:** Usando a câmera integrada, o sistema monitora a presença no ambiente, podendo alertar cuidadores em caso de inatividade prolongada.
*   🌡️ **Monitoramento de Ambiente:** Sensores de temperatura e umidade integrados para garantir o conforto e a segurança do local.
*   🌐 **Relatórios para Cuidadores (IoT):** Envio de status importantes (ex: "Medicamento confirmado", "Ausência prolongada") para uma plataforma online, acessível por familiares.

---

## ⚙️ Arquitetura do Sistema

O sistema opera de forma centralizada na UNIHIKER K10, gerenciando todas as entradas, processamento e saídas.

<!-- ADICIONE UM DIAGRAMA DA ARQUITETURA AQUI -->
<!-- Ex: <p align="center"><img src="./assets/arquitetura.png"></p> -->

*   **Entrada de Dados:**
    *   🎤 **Microfone:** Captura comandos de voz.
    *   📷 **Câmera 2MP:** Realiza a detecção de movimento/presença.
    *   🕹️ **Sensores Integrados:** Coletam dados de luz, temperatura, umidade e aceleração.
    *   🔘 **Botões A/B:** Para interações manuais (ex: adiar um alarme).

*   **Processamento (ESP32-S3):**
    *   O firmware em **MicroPython** gerencia os periféricos.
    *   Modelos de **TinyML** para reconhecimento de voz e visão computacional rodam localmente.
    *   A lógica principal do programa controla os horários, os alertas e a comunicação.

*   **Saída de Dados e Ação:**
    *   🖥️ **Tela Colorida 2.8":** Exibe horas, lembretes e status.
    *   🔊 **Alto-falante:** Emite alertas sonoros e respostas de voz.
    *   💡 **LEDs RGB:** Fornecem feedback visual de status (ouvindo, confirmado, alerta).
    *   📶 **Módulo Wi-Fi:** Envia dados para a nuvem (servidor MQTT ou plataforma IoT).

---

## 🛠️ Hardware e Software Necessários

### Hardware
*   Placa [UNIHIKER K10](https://www.robocore.net/dfrobot/unihiker-k10)
*   Cabo USB-C para alimentação e programação.
*   (Opcional) Bateria de Lítio para autonomia de energia.
*   (Opcional) Sensores externos da linha Gravity para expansão.

### Software
*   **Firmware:** MicroPython para a UNIHIKER K10.
*   **IDE:** Mind+ (para programação em blocos/Python) ou Thonny IDE.
*   **Bibliotecas:** Bibliotecas nativas da UNIHIKER.
*   **(Opcional) Plataforma IoT:** Adafruit IO, Tago.io, Thingspeak, ou um broker MQTT.

---

## 🚀 Como Começar

Para ter uma cópia local do projeto rodando, siga estes passos.

### Pré-requisitos

1.  Tenha o Thonny IDE ou o Mind+ instalado.
2.  Siga o guia oficial da DFRobot para configurar a UNIHIKER e o ambiente MicroPython pela primeira vez.

### Instalação

1.  Clone o repositório:
    ```sh
    git clone https://github.com/IAjmsmf/UNIHIKER-K10.git
    ```
2.  Abra a pasta do projeto no seu IDE de preferência.
3.  Transfira os arquivos do diretório `/firmware` para o sistema de arquivos da UNIHIKER.
4.  Reinicie a placa. O `main.py` deverá ser executado automaticamente.

---

## 📁 Estrutura do Repositório
