import os
import tkinter as tk
from tkinter import font
import subprocess


# pegar o diretório atual do codigo
dir_path = os.path.dirname(os.path.realpath(__file__))

def iniciar_grafo():
    subprocess.Popen(["python", os.path.join(dir_path, "grafo.py")])

def iniciar_fila():
    subprocess.Popen(["python", os.path.join(dir_path, "fila.py")])

def iniciar_lista_ligada():
    subprocess.Popen(["python", os.path.join(dir_path, "listaligada.py")])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("400x300")
    root.config(bg="#2c3e50")

    # Definir fontes
    title_font = font.Font(family='Helvetica', size=18, weight="bold")

    # Frame principal
    frame = tk.Frame(root, bg="#2c3e50")
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Título
    title = tk.Label(frame, text="Menu Principal", font=title_font, fg="#ecf0f1", bg="#2c3e50")
    title.pack(pady=10)

    # Função para animação de hover
    def on_enter(e, btn):
        btn['background'] = '#34495e'
        btn['foreground'] = '#ecf0f1'

    def on_leave(e, btn):
        btn['background'] = '#ecf0f1'
        btn['foreground'] = '#2c3e50'

    # Botões estilizados
    button_font = font.Font(family='Helvetica', size=12)
    btn_grafo = tk.Button(frame, text="Iniciar Grafo", command=iniciar_grafo, font=button_font, bg="#ecf0f1", fg="#2c3e50", relief="raised", bd=3, width=20)
    btn_grafo.pack(pady=10)
    btn_grafo.bind("<Enter>", lambda e: on_enter(e, btn_grafo))
    btn_grafo.bind("<Leave>", lambda e: on_leave(e, btn_grafo))

    btn_fila = tk.Button(frame, text="Iniciar Fila", command=iniciar_fila, font=button_font, bg="#ecf0f1", fg="#2c3e50", relief="raised", bd=3, width=20)
    btn_fila.pack(pady=10)
    btn_fila.bind("<Enter>", lambda e: on_enter(e, btn_fila))
    btn_fila.bind("<Leave>", lambda e: on_leave(e, btn_fila))

    btn_lista_ligada = tk.Button(frame, text="Iniciar Lista Ligada", command=iniciar_lista_ligada, font=button_font, bg="#ecf0f1", fg="#2c3e50", relief="raised", bd=3, width=20)
    btn_lista_ligada.pack(pady=10)
    btn_lista_ligada.bind("<Enter>", lambda e: on_enter(e, btn_lista_ligada))
    btn_lista_ligada.bind("<Leave>", lambda e: on_leave(e, btn_lista_ligada))

    root.mainloop()
