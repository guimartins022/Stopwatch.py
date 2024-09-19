import tkinter as tk
import time

# Variáveis de controle
running = False
paused = False
elapsed_time = 0

def start_timer():
    global running, paused, elapsed_time
    if not running:
        running = True
        paused = False
        start_time = time.time() - elapsed_time
        update_timer(start_time)

def update_timer(start_time):
    global running, elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        time_str.set(format_time(elapsed_time))
        root.after(100, update_timer, start_time)

def pause_timer():
    global running, paused
    if running:
        paused = True
        running = False

def reset_timer():
    global running, paused, elapsed_time
    running = False
    paused = False
    elapsed_time = 0
    time_str.set('00:00:00.0')

def format_time(seconds):
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    return f'{hours:02}:{mins:02}:{secs:02}.{int(seconds * 10 % 10)}'

# Interface gráfica
root = tk.Tk()
root.title('Cronômetro')
root.resizable(False, False)  # Impede maximizar a janela

time_str = tk.StringVar()
time_str.set('00:00:00.0')

label = tk.Label(root, textvariable=time_str, font=('Helvetica', 40))
label.pack()

start_button = tk.Button(root, text='Iniciar', command=start_timer)
start_button.pack(side='left')

pause_button = tk.Button(root, text='Pausar', command=pause_timer)
pause_button.pack(side='left')

reset_button = tk.Button(root, text='Reiniciar', command=reset_timer)
reset_button.pack(side='left')

root.mainloop()
