import tkinter as tk
import subprocess

class MainInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Seleção de Estrutura de Dados")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Selecione a estrutura de dados:")
        self.label.pack(pady=20)

        self.button_fila = tk.Button(self, text="Fila", command=self.executar_fila)
        self.button_fila.pack(pady=10)

        self.button_lista_ligada = tk.Button(self, text="Lista Ligada Simples", command=self.executar_lista_ligada)
        self.button_lista_ligada.pack(pady=10)

        self.button_grafo = tk.Button(self, text="Grafo", command=self.executar_grafo)
        self.button_grafo.pack(pady=10)

    def executar_fila(self):
        subprocess.Popen(["python", "Fila.py"])

    def executar_lista_ligada(self):
        subprocess.Popen(["python", "ListaLigada.py"])

    def executar_grafo(self):
        subprocess.Popen(["python", "Grafo.py"])

if __name__ == "__main__":
    app = MainInterface()
    app.mainloop()
