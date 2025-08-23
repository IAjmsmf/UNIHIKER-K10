# firmware/notification_manager.py

import time
from unihiker import GUI

# Instanciando a GUI para uso neste módulo
# É comum instanciar a GUI uma vez no main, mas para modularidade,
# podemos passar o objeto 'gui' como argumento nas funções.
# Por simplicidade inicial, vamos criar uma instância local aqui.
gui = GUI()

def show_medication_alert(medication_name):
    """
    Exibe um alerta visual e sonoro para um medicamento específico.
    """
    print(f"ALERTA: Hora de tomar {medication_name}!")
    
    # Limpa a tela para focar no alerta
    gui.clear()
    
    # Toca um som de alerta
    gui.play_sound(gui.SOUND_ALERT)
    
    # Mostra o alerta na tela
    gui.draw_text(text=f"Hora de tomar:", x=120, y=80, font_size=20, origin='center')
    gui.draw_text(text=medication_name, x=120, y=140, font_size=24, origin='center', color='red')
    
    # Mantém o alerta na tela por um tempo determinado
    time.sleep(10) # Pausa por 10 segundos
    
    # Toca um som de confirmação ao final
    gui.play_sound(gui.SOUND_SUCCESS)
