# Guia de Instalação e Primeiro Teste

Este documento fornece um passo a passo detalhado para configurar o ambiente de desenvolvimento, transferir o código-fonte para a sua placa UNIHIKER K10 e executar o protótipo inicial do projeto Guardião Sênior.

## 1. Pré-requisitos

Antes de começar, garanta que você possui:

*   **Hardware:**
    *   1x Placa [UNIHIKER K10](https://www.robocore.net/dfrobot/unihiker-k10)
    *   1x Cabo USB-C de dados

*   **Software:**
    *   [Thonny IDE](https://thonny.org/) instalado em seu computador. É a IDE recomendada por sua simplicidade e integração com MicroPython.

## 2. Configuração do Ambiente (Thonny + UNIHIKER)

1.  **Conecte a Placa:** Conecte sua UNIHIKER K10 ao computador com o cabo USB-C.

2.  **Abra o Thonny:** Inicie o Thonny IDE.

3.  **Selecione o Interpretador:**
    *   Vá ao menu **Ferramentas (Tools) -> Opções (Options)**.
    *   Na aba **Interpretador (Interpreter)**, selecione **`MicroPython (ESP32)`**.
    *   No campo **Porta (Port)**, escolha a porta serial correspondente à sua UNIHIKER (ex: `COM3` ou `/dev/ttyUSB0`).
    *   Clique em **OK**.

4.  **Verifique a Conexão:** O painel inferior do Thonny (Shell/REPL) deve se conectar e exibir o prompt `>>>`. Isso confirma que a comunicação com a placa está funcionando.

![Configuração do Interpretador no Thonny](https://raw.githubusercontent.com/thonny/thonny/master/images/for_readme/esp_backend_config.png)
*(Exemplo de tela de configuração do Thonny)*

## 3. Preparando e Enviando o Código

1.  **Clone o Repositório:** Primeiro, obtenha os arquivos do projeto em seu computador.
    ```sh
    git clone https://github.com/IAjmsmf/UNIHIKER-K10.git
    ```

2.  **Abra os Arquivos no Thonny:**
    *   No Thonny, vá em **Visualizar (View) -> Arquivos (Files)** para exibir o gerenciador de arquivos.
    *   No painel "Este computador", navegue até a pasta onde você clonou o repositório (ex: `UNIHIKER-K10/firmware`).

3.  **Configure suas Credenciais:**
    *   Abra o arquivo `config.py` no editor do Thonny.
    *   **Importante:** Altere os valores de `WIFI_SSID` e `WIFI_PASS` para as credenciais da sua rede Wi-Fi.
    *   Salve o arquivo (`Ctrl+S`).

4.  **Envie os Arquivos para a Placa:**
    *   No painel de arquivos, selecione todos os arquivos dentro da pasta `firmware` (`main.py`, `config.py`, `notification_manager.py`).
    *   Clique com o botão direito sobre eles e escolha a opção **"Upload para /"** ou **"Enviar para /"**. Isso copiará os arquivos para a memória interna da UNIHIKER.

## 4. Execução e Teste Final

1.  **Reinicie a Placa:** Para que o código comece a rodar, você precisa reiniciar a UNIHIKER. Pressione o botão `RESET` na placa ou pressione **Ctrl+D** no Shell do Thonny.

2.  **Observe o Resultado:**
    *   **Na tela da UNIHIKER:** Você verá a mensagem "Conectando ao WiFi...", seguida de "Conectado!". Logo depois, um relógio digital aparecerá e será atualizado a cada segundo.
    *   **No Shell do Thonny:** Mensagens de log sobre o status da conexão e o início do loop principal serão exibidas.

3.  **Teste o Alerta de Medicação:**
    *   Para testar a notificação sem esperar o horário real, modifique temporariamente um dos horários no arquivo `config.py` para um ou dois minutos no futuro.
    *   Salve e envie o arquivo `config.py` novamente para a placa.
    *   Reinicie a UNIHIKER.
    *   Observe o alerta visual e sonoro aparecer na tela no horário programado!

Parabéns! Você acaba de implementar e testar com sucesso a base do projeto Guardião Sênior. A partir daqui, você está pronto para explorar e adicionar novas funcionalidades.
