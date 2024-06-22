import tkinter as tk
from tkinter import messagebox

class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.frente = None
        self.fim = None

    def enfileirar(self, dado):
        novo_no = No(dado)
        if self.fim is None:
            self.frente = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.frente is None:
            return None
        temp = self.frente
        self.frente = temp.proximo
        if self.frente is None:
            self.fim = None
        return temp.dado

    def limpar(self):
        self.frente = self.fim = None

class AplicacaoFila:
    def __init__(self, root):
        self.fila = Fila()
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white', scrollregion=(0, 0, 2000, 400))
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.iniciar_scroll)
        self.canvas.bind("<B1-Motion>", self.navegar_scroll)

        self.frame_controle = tk.Frame(root)
        self.frame_controle.pack()

        self.label_dado = tk.Label(self.frame_controle, text="Valor:")
        self.label_dado.pack(side=tk.LEFT, padx=5)
        self.entrada_dado = tk.Entry(self.frame_controle)
        self.entrada_dado.pack(side=tk.LEFT, padx=5)

        self.btn_enfileirar = tk.Button(self.frame_controle, text="Enfileirar", command=self.enfileirar)
        self.btn_enfileirar.pack(side=tk.LEFT, padx=5)

        self.btn_desenfileirar = tk.Button(self.frame_controle, text="Desenfileirar", command=self.desenfileirar)
        self.btn_desenfileirar.pack(side=tk.LEFT, padx=5)

        self.btn_limpar = tk.Button(self.frame_controle, text="Limpar", command=self.limpar)
        self.btn_limpar.pack(side=tk.LEFT, padx=5)

        self.label_concatenado_entrada = tk.Label(root, text="Valores de Entrada:")
        self.label_concatenado_entrada.pack()
        self.entrada_concatenada = tk.Entry(root, state='readonly', width=80)
        self.entrada_concatenada.pack()

        self.label_concatenado_saida = tk.Label(root, text="Valores de Saída:")
        self.label_concatenado_saida.pack()
        self.saida_concatenada = tk.Entry(root, state='readonly', width=80)
        self.saida_concatenada.pack()

        self.concatenado_entrada = ""
        self.concatenado_saida = ""

        self.label_status = tk.Label(root, text="", fg='blue')
        self.label_status.pack()

        self.desenhar_fila()

    def desenhar_fila(self):
        self.canvas.delete('all')
        atual = self.fila.frente
        x = 50
        y = 200
        while atual:
            self.canvas.create_rectangle(x, y, x + 50, y + 30, outline='black')
            self.canvas.create_text(x + 25, y + 15, text=str(atual.dado))
            if atual.proximo:
                self.canvas.create_line(x + 50, y + 15, x + 100, y + 15, arrow=tk.LAST)
            atual = atual.proximo
            x += 100

    def enfileirar(self):
        dado = self.obter_dado_entrada()
        if dado:
            if self.concatenado_entrada:
                self.concatenado_entrada += f", {dado}"
            else:
                self.concatenado_entrada += dado
            self.fila.enfileirar(dado)
            self.atualizar_concatenado_entrada()
            self.desenhar_fila()

    def desenfileirar(self):
        dado = self.fila.desenfileirar()
        if dado is not None:
            self.label_status.config(text=f"Desenfileirado: {dado}")
            if self.concatenado_saida:
                self.concatenado_saida += f", {dado}"
            else:
                self.concatenado_saida += dado
            self.atualizar_concatenado_saida()
            self.desenhar_fila()
        else:
            self.label_status.config(text="Fila vazia, nada para desenfileirar.", fg='red')

    def limpar(self):
        self.fila.limpar()
        self.concatenado_entrada = ""
        self.concatenado_saida = ""
        self.atualizar_concatenado_entrada()
        self.atualizar_concatenado_saida()
        self.label_status.config(text="Fila limpa.", fg='blue')
        self.desenhar_fila()

    def obter_dado_entrada(self):
        dado_str = self.entrada_dado.get().strip()
        if dado_str:
            self.entrada_dado.delete(0, tk.END)
            return dado_str
        messagebox.showerror("Erro", "Digite um valor válido.")
        return None

    def atualizar_concatenado_entrada(self):
        self.entrada_concatenada.config(state='normal')
        self.entrada_concatenada.delete(0, tk.END)
        self.entrada_concatenada.insert(0, self.concatenado_entrada)
        self.entrada_concatenada.config(state='readonly')

    def atualizar_concatenado_saida(self):
        self.saida_concatenada.config(state='normal')
        self.saida_concatenada.delete(0, tk.END)
        self.saida_concatenada.insert(0, self.concatenado_saida)
        self.saida_concatenada.config(state='readonly')

    def iniciar_scroll(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def navegar_scroll(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fila")
    app = AplicacaoFila(root)
    root.mainloop()


## versão final sem interligação com a interface