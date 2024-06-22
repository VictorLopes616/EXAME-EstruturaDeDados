import tkinter as tk
from collections import deque

class Aresta:
    def __init__(self, peso, inicio, fim, edge_id=None):
        self.peso = peso
        self.inicio = inicio
        self.fim = fim
        self.edge_id = edge_id

    def get_peso(self):
        return self.peso
 
    def set_peso(self, peso):
        self.peso = peso

    def get_inicio(self):
        return self.inicio

    def set_inicio(self, inicio):
        self.inicio = inicio

    def get_fim(self):
        return self.fim

    def set_fim(self, fim):
        self.fim = fim

class Vertice:
    def __init__(self, valor, x, y, node_id, text_id):
        self.valor = valor
        self.x = x
        self.y = y
        self.node_id = node_id
        self.text_id = text_id
        self.arestas_entrada = []
        self.arestas_saida = []

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def adicionar_aresta_entrada(self, aresta):
        self.arestas_entrada.append(aresta)

    def adicionar_aresta_saida(self, aresta):
        self.arestas_saida.append(aresta)

    def remover_aresta_entrada(self, aresta):
        if aresta in self.arestas_entrada:
            self.arestas_entrada.remove(aresta)

    def remover_aresta_saida(self, aresta):
        if aresta in self.arestas_saida:
            self.arestas_saida.remove(aresta)

    def get_arestas_entrada(self):
        return self.arestas_entrada

    def get_arestas_saida(self):
        return self.arestas_saida

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def adicionar_vertice(self, valor, x, y, node_id, text_id):
        novo_vertice = Vertice(valor, x, y, node_id, text_id)
        self.vertices.append(novo_vertice)
        return novo_vertice

    def adicionar_aresta(self, peso, inicio, fim, edge_id):
        aresta = Aresta(peso, inicio, fim, edge_id)
        inicio.adicionar_aresta_saida(aresta)
        fim.adicionar_aresta_entrada(aresta)
        self.arestas.append(aresta)
        return aresta

    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            self.vertices.remove(vertice)
            for aresta in vertice.get_arestas_saida() + vertice.get_arestas_entrada():
                self.arestas.remove(aresta)
            for aresta in vertice.get_arestas_entrada():
                aresta.get_inicio().remover_aresta_saida(aresta)
            for aresta in vertice.get_arestas_saida():
                aresta.get_fim().remover_aresta_entrada(aresta)

    def get_vertice_by_id(self, node_id):
        for vertice in self.vertices:
            if vertice.node_id == node_id:
                return vertice
        return None

    def get_vertice_by_valor(self, valor):
        for vertice in self.vertices:
            if vertice.valor == valor:
                return vertice
        return None

    def buscar_largura(self):
        if not self.vertices:
            return

        visitados = []
        fila = deque()
        atual = self.vertices[0]
        visitados.append(atual)
        print(atual.get_valor())
        fila.append(atual)

        while fila:
            visitado = fila.popleft()
            for aresta in visitado.get_arestas_saida():
                proximo = aresta.get_fim()
                if proximo not in visitados:
                    visitados.append(proximo)
                    print(proximo.get_valor())
                    fila.append(proximo)

class GrafoInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualização de Grafo")

        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(self.frame, text="Início:").grid(row=0, column=0)
        self.start_entry = tk.Entry(self.frame)
        self.start_entry.grid(row=1, column=0)

        tk.Label(self.frame, text="Fim:").grid(row=2, column=0)
        self.end_entry = tk.Entry(self.frame)
        self.end_entry.grid(row=3, column=0)

        self.add_edge_button = tk.Button(self.frame, text="Adicionar Aresta", command=self.adicionar_aresta)
        self.add_edge_button.grid(row=4, column=0)

        self.grafo = Grafo()
        self.node_counter = 0
        self.selected_node = None
        self.start_node = None

        self.canvas.bind("<Button-1>", self.clicar)
        self.canvas.bind("<B1-Motion>", self.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.soltar)
        self.canvas.bind("<Button-3>", self.remover_vertice)

        self.master.bind("b", self.buscar_largura)
        self.master.bind("d", self.buscar_profundidade)

    def clicar(self, event):
        item = self.canvas.find_withtag("current")
        if not item:
            self.criar_vertice(event.x, event.y)
        else:
            node_id = self.encontrar_vertice(item)
            if node_id:
                self.selected_node = node_id
                self.start_node = (event.x, event.y)

    def arrastar(self, event):
        if self.selected_node:
            dx, dy = event.x - self.start_node[0], event.y - self.start_node[1]
            self.canvas.move(self.selected_node, dx, dy)
            vertice = self.grafo.get_vertice_by_id(self.selected_node)
            vertice.x += dx
            vertice.y += dy
            self.canvas.move(vertice.text_id, dx, dy)
            self.start_node = (event.x, event.y)
            for aresta in vertice.get_arestas_saida() + vertice.get_arestas_entrada():
                self.atualizar_aresta(aresta)

    def soltar(self, event):
        self.selected_node = None
        self.start_node = None

    def encontrar_vertice(self, item):
        for vertice in self.grafo.vertices:
            if vertice.node_id in item or vertice.text_id in item:
                return vertice.node_id
        return None

    def criar_vertice(self, x, y):
        valor = chr(65 + self.node_counter)  # A partir de 'A'
        node_id = self.canvas.create_oval(x-20, y-20, x+20, y+20, outline="black", fill="lightblue")
        text_id = self.canvas.create_text(x, y, text=valor)
        self.grafo.adicionar_vertice(valor, x, y, node_id, text_id)
        self.node_counter += 1

    def adicionar_aresta(self):
        inicio_valor = self.start_entry.get()
        fim_valor = self.end_entry.get()

        inicio = self.grafo.get_vertice_by_valor(inicio_valor)
        fim = self.grafo.get_vertice_by_valor(fim_valor)
        if inicio and fim:
            edge_id = self.canvas.create_line(inicio.x, inicio.y, fim.x, fim.y, arrow=tk.LAST)
            self.grafo.adicionar_aresta(1, inicio, fim, edge_id)

    def atualizar_aresta(self, aresta):
        inicio = aresta.get_inicio()
        fim = aresta.get_fim()
        self.canvas.coords(aresta.edge_id, inicio.x, inicio.y, fim.x, fim.y)

    def remover_vertice(self, event):
        item = self.canvas.find_withtag("current")
        node_id = self.encontrar_vertice(item)
        vertice = self.grafo.get_vertice_by_id(node_id)
        if vertice:
            for aresta in vertice.get_arestas_saida() + vertice.get_arestas_entrada():
                self.canvas.delete(aresta.edge_id)
            self.grafo.remover_vertice(vertice)
            self.canvas.delete(vertice.text_id)
            self.canvas.delete(vertice.node_id)

    def buscar_largura(self, event=None):
        if not self.grafo.vertices:
            return
        start_node = self.grafo.vertices[0]
        visitados = []
        fila = deque()
        visitados.append(start_node)
        print(start_node.get_valor())
        fila.append(start_node)

        while fila:
            visitado = fila.popleft()
            for aresta in visitado.get_arestas_saida():
                proximo = aresta.get_fim()
                if proximo not in visitados:
                    visitados.append(proximo)
                    print(proximo.get_valor())
                    fila.append(proximo)

    def buscar_profundidade(self, event=None):
        if not self.grafo.vertices:
            return
        start_node = self.grafo.vertices[0]
        visitados = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node in visitados:
                continue
            visitados.add(node)
            self.destacar_vertice(node.node_id)
            for aresta in node.get_arestas_saida():
                neighbor = aresta.get_fim()
                if neighbor not in visitados:
                    stack.append(neighbor)

    def destacar_vertice(self, node_id):
        self.canvas.itemconfig(node_id, fill="yellow")
        self.canvas.update()
        self.master.after(500)
        self.canvas.itemconfig(node_id, fill="lightblue")
        self.canvas.update()

root = tk.Tk()
app = GrafoInterface(root)
root.mainloop()


