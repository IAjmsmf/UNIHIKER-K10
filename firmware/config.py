# firmware/config.py

# --- Configurações de Rede ---
WIFI_SSID = "NOME_DA_SUA_REDE_WIFI"
WIFI_PASS = "SENHA_DA_SUA_REDE_WIFI"

# --- Configurações do Assistente ---

# Lista de medicamentos e seus horários
# Formato: {'nome': 'Nome do Remédio', 'hora': HORA, 'minuto': MINUTO}
MEDICATIONS = [
    {'name': 'Vitamina C', 'hour': 8, 'minute': 0},
    {'name': 'Remédio Pressão', 'hour': 12, 'minute': 30},
    {'name': 'Cálcio', 'hour': 20, 'minute': 0},
    # Adicione mais medicamentos aqui
]

# Tempo em segundos que o alerta de medicação fica na tela
ALERT_DURATION_SECONDS = 30
