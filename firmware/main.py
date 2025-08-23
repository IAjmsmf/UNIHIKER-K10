# firmware/main.py

import time
from unihiker import GUI, WIFI
import config  # Importa nossas configurações
import notification_manager # Importa nosso gerenciador de notificações

# --- Inicialização ---
gui = GUI()
wifi = WIFI()

# --- Conexão Wi-Fi ---
gui.draw_text(text="Conectando ao WiFi...", x=10, y=120)
print("Conectando ao WiFi...")
wifi.connect(ssid=config.WIFI_SSID, password=config.WIFI_PASS)

if wifi.is_connected():
    gui.draw_text(text="Conectado!", x=10, y=150, color='green')
    print("Conectado com sucesso!")
else:
    gui.draw_text(text="Falha na conexão.", x=10, y=150, color='red')
    print("Falha na conexão.")

# Sincroniza o relógio interno com a internet (NTP)
# Isso é crucial para ter a hora certa!
wifi.ntp_sync()

time.sleep(2) # Pequena pausa para mostrar o status da conexão

# --- Loop Principal ---
last_alert_minute = -1 # Variável para garantir que o alerta só toque uma vez por minuto

print("Iniciando loop principal do assistente.")

while True:
    # Obtém a hora atual
    # time.localtime() retorna uma tupla: (ano, mes, dia, hora, minuto, segundo, dia_semana, dia_ano)
    now = time.localtime()
    current_hour = now[3]
    current_minute = now[4]
    current_second = now[5]

    # --- Lógica de Verificação de Medicação ---
    # Verifica se o minuto atual é diferente do último minuto que teve alerta
    if current_minute != last_alert_minute:
        for med in config.MEDICATIONS:
            if med['hour'] == current_hour and med['minute'] == current_minute:
                # É hora de um medicamento!
                notification_manager.show_medication_alert(med['name'])
                last_alert_minute = current_minute # Atualiza o último minuto de alerta
                break # Sai do loop de medicamentos para evitar múltiplos alertas no mesmo minuto

    # --- Atualização da Tela Principal (Relógio) ---
    gui.clear()
    
    # Formata a hora e a data para exibição
    time_str = f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}"
    date_str = f"{now[2]:02d}/{now[1]:02d}/{now[0]}"

    # Desenha o relógio e a data na tela
    gui.draw_text(text=time_str, x=120, y=100, font_size=40, origin='center')
    gui.draw_text(text=date_str, x=120, y=160, font_size=18, origin='center')

    # Espera 1 segundo antes de atualizar a tela novamente
    time.sleep(1)
