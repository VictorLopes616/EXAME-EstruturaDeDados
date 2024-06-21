import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random


class EstruturaFila:
    def __init__(self, capacidade=10):
        self.elementos = [None] * capacidade
        self._tamanho = 0

    def esta_vazia(self):
        return self._tamanho == 0

    def enfileirar(self, elemento):
        self.aumentar_capacidade()
        if self._tamanho < len(self.elementos):
            self.elementos[self._tamanho] = elemento
            self._tamanho += 1

    def aumentar_capacidade(self):
        if self._tamanho == len(self.elementos):
            self.elementos = self.elementos + [None] * len(self.elementos)

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        elemento_removido = self.elementos[0]
        for i in range(self._tamanho - 1):
            self.elementos[i] = self.elementos[i + 1]
        self.elementos[self._tamanho - 1] = None
        self._tamanho -= 1
        return elemento_removido

    def tamanho(self):
        return self._tamanho

    def elemento(self, posicao):
        if posicao < 0 or posicao >= self._tamanho:
            raise ValueError("Posição inválida")
        return self.elementos[posicao]


class NodeFila:
    def __init__(self, texto, cor, pos_x, pos_y):
        self.texto = texto
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y


class FilaInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.fila = EstruturaFila(10)
        self.atendidos = []

        self.largura_quadrado = 50
        self.altura_quadrado = 50
        self.corredor_padding = 20
        self.espacamento_vertical = 10
        self.espacamento_horizontal = 10

        self.panel = tk.Canvas(self, bg="darkgray")
        self.panel.pack(fill=tk.BOTH, expand=True)

        self.botao_adicionar = tk.Button(self, text="Adicionar Elemento", bg="green", fg="black",
                                         command=self.adicionar_elemento)
        self.botao_adicionar.pack(side=tk.TOP, padx=10, pady=10)

        self.botao_remover = tk.Button(self, text="Remover Elemento", bg="red", fg="black",
                                       command=self.remover_elemento)
        self.botao_remover.pack(side=tk.TOP, padx=10, pady=10)

        self.title("Fila Visual")
        self.geometry("800x600")
        self.update()
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.panel.config(scrollregion=self.panel.bbox("all"))
        self.panel.delete("all")
        self.desenhar()

    def desenhar(self):
        x = 100 + self.corredor_padding
        y = 100

        self.panel.create_rectangle(x - self.corredor_padding, y - 5, x + self.largura_quadrado * 10, y + 5,
                                    fill="gray")
        self.panel.create_rectangle(x - self.corredor_padding, y + self.altura_quadrado + 5,
                                    x + self.largura_quadrado * 10, y + self.altura_quadrado + 15, fill="gray")

        for i in range(self.fila.tamanho()):
            node = self.fila.elemento(i)
            self.desenhar_no(node)

        for i, node in enumerate(self.atendidos):
            self.desenhar_no(node)

    def desenhar_no(self, node):
        self.panel.create_rectangle(node.pos_x, node.pos_y, node.pos_x + self.largura_quadrado,
                                    node.pos_y + self.altura_quadrado, fill=node.cor, outline="black")
        self.panel.create_text(node.pos_x + self.largura_quadrado // 2, node.pos_y + self.altura_quadrado // 2,
                               text=node.texto, fill="white", font=("Arial", 20))

    def adicionar_elemento(self):
        texto = simpledialog.askstring("Input", "Digite o texto para o elemento:")
        if texto:
            cor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            node = NodeFila(texto, cor, 800, 100)
            self.fila.enfileirar(node)
            self.animar_entrada_node(node)

    def animar_entrada_node(self, node):
        def move():
            index_node = self.fila.elementos.index(node)
            target_x = 100 + self.corredor_padding + index_node * (self.largura_quadrado + self.espacamento_horizontal)
            if node.pos_x > target_x:
                node.pos_x -= 5
                self.panel.delete("all")
                self.desenhar()
                self.after(10, move)
            else:
                node.pos_x = target_x
                self.panel.delete("all")
                self.desenhar()

        move()

    def remover_elemento(self):
        if not self.fila.esta_vazia():
            node = self.fila.desenfileirar()
            self.animar_saida_node(node)

    def animar_saida_node(self, node):
        target_x = 50
        target_y = 200 + len(self.atendidos) * (self.altura_quadrado + self.espacamento_vertical)

        def move_out():
            if node.pos_x > target_x:
                node.pos_x -= 5
            elif node.pos_y < target_y:
                node.pos_y += 5
            else:
                self.atendidos.append(node)
                self.animar_nodes_restantes()
                return

            self.panel.delete("all")
            self.desenhar()
            self.after(10, move_out)

        move_out()

    def animar_nodes_restantes(self):
        def move_remaining():
            all_moved = True
            for i in range(self.fila.tamanho()):
                node = self.fila.elemento(i)
                target_x = 100 + self.corredor_padding + i * (self.largura_quadrado + self.espacamento_horizontal)
                if node.pos_x > target_x:
                    node.pos_x -= 5
                    all_moved = False
            self.panel.delete("all")
            self.desenhar()
            if not all_moved:
                self.after(10, move_remaining)

        move_remaining()


if __name__ == "__main__":
    app = FilaInterface()
    app.mainloop()



## versão final antes da fusão de codigo {VERIFICADO!!!}