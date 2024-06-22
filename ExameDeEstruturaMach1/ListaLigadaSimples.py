import tkinter as tk
from tkinter import messagebox, simpledialog

class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_no_fim(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            return
        ultimo = self.cabeca
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_no

    def remover_do_inicio(self):
        if self.cabeca is None:
            return None
        dado = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        return dado

    def remover_do_fim(self):
        if self.cabeca is None:
            return None
        if self.cabeca.proximo is None:
            dado = self.cabeca.dado
            self.cabeca = None
            return dado
        penultimo = self.cabeca
        while penultimo.proximo.proximo:
            penultimo = penultimo.proximo
        dado = penultimo.proximo.dado
        penultimo.proximo = None
        return dado

class AplicacaoListaLigada:
    def __init__(self, root):
        self.lista_ligada = ListaLigada()
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white', scrollregion=(0, 0, 2000, 400))
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.iniciar_scroll)
        self.canvas.bind("<B1-Motion>", self.navegar_scroll)

        self.frame_controle = tk.Frame(root)
        self.frame_controle.pack()

        self.label_dado = tk.Label(self.frame_controle, text="Dado:")
        self.label_dado.pack(side=tk.LEFT, padx=5)
        self.entrada_dado = tk.Entry(self.frame_controle)
        self.entrada_dado.pack(side=tk.LEFT, padx=5)

        self.btn_inserir_inicio = tk.Button(self.frame_controle, text="Inserir no Início", command=self.inserir_no_inicio)
        self.btn_inserir_inicio.pack(side=tk.LEFT, padx=5)

        self.btn_inserir_fim = tk.Button(self.frame_controle, text="Inserir no Fim", command=self.inserir_no_fim)
        self.btn_inserir_fim.pack(side=tk.LEFT, padx=5)

        self.btn_remover_inicio = tk.Button(self.frame_controle, text="Remover do Início", command=self.remover_do_inicio)
        self.btn_remover_inicio.pack(side=tk.LEFT, padx=5)

        self.btn_remover_fim = tk.Button(self.frame_controle, text="Remover do Fim", command=self.remover_do_fim)
        self.btn_remover_fim.pack(side=tk.LEFT, padx=5)

        self.label_status = tk.Label(root, text="", fg='blue')
        self.label_status.pack()

        self.desenhar_lista_ligada()

    def desenhar_lista_ligada(self):
        self.canvas.delete('all')
        atual = self.lista_ligada.cabeca
        x = 50
        y = 200
        while atual:
            self.canvas.create_rectangle(x, y, x + 50, y + 30, outline='black')
            self.canvas.create_text(x + 25, y + 15, text=str(atual.dado))
            if atual.proximo:
                self.canvas.create_line(x + 50, y + 15, x + 100, y + 15, arrow=tk.LAST)
            atual = atual.proximo
            x += 100

    def inserir_no_inicio(self):
        dado = self.obter_dado_entrada()
        if dado:
            self.lista_ligada.inserir_no_inicio(dado)
            self.desenhar_lista_ligada()

    def inserir_no_fim(self):
        dado = self.obter_dado_entrada()
        if dado:
            self.lista_ligada.inserir_no_fim(dado)
            self.desenhar_lista_ligada()

    def remover_do_inicio(self):
        dado = self.lista_ligada.remover_do_inicio()
        if dado is not None:
            self.label_status.config(text=f"Removido do Início: {dado}")
            self.desenhar_lista_ligada()
        else:
            self.label_status.config(text="Lista vazia, nada para remover.", fg='red')

    def remover_do_fim(self):
        dado = self.lista_ligada.remover_do_fim()
        if dado is not None:
            self.label_status.config(text=f"Removido do Fim: {dado}")
            self.desenhar_lista_ligada()
        else:
            self.label_status.config(text="Lista vazia, nada para remover.", fg='red')

    def obter_dado_entrada(self):
        dado_str = self.entrada_dado.get().strip()
        if dado_str:
            self.entrada_dado.delete(0, tk.END)
            return dado_str
        messagebox.showerror("Erro", "Digite um valor válido.")
        return None

    def iniciar_scroll(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def navegar_scroll(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lista Ligada Simples")
    app = AplicacaoListaLigada(root)
    root.mainloop()
