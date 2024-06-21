import tkinter as tk


# Definição da estrutura de dados da lista ligada simples
class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class ListaLigadaSimples:
    def __init__(self):
        self.primeiro = None

    def adicionar_primeiro(self, v):
        novo_no = No(v)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def adicionar_ultimo(self, v):
        novo_no = No(v)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover_primeiro(self):
        if self.primeiro is None:
            return None
        valor_removido = self.primeiro.valor
        self.primeiro = self.primeiro.proximo
        return valor_removido

    def remover_ultimo(self):
        if self.primeiro is None:
            return None
        if self.primeiro.proximo is None:
            valor_removido = self.primeiro.valor
            self.primeiro = None
            return valor_removido
        atual = self.primeiro
        while atual.proximo.proximo is not None:
            atual = atual.proximo
        valor_removido = atual.proximo.valor
        atual.proximo = None
        return valor_removido

    def tamanho(self):
        tamanho = 0
        atual = self.primeiro
        while atual is not None:
            tamanho += 1
            atual = atual.proximo
        return tamanho


# Classe para a interface gráfica
class ListaLigadaInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualização de Lista Ligada")

        # Lista ligada e elementos gráficos
        self.lista = ListaLigadaSimples()
        self.node_width = 80
        self.node_height = 50
        self.node_distance = 100
        self.canvas = tk.Canvas(self.master, width=800, height=400, bg="white")
        self.canvas.pack()

        # Botões e entrada
        self.label_valor = tk.Label(self.master, text="Valor:")
        self.label_valor.pack()
        self.entry_valor = tk.Entry(self.master)
        self.entry_valor.pack()
        self.botao_adicionar_primeiro = tk.Button(self.master, text="Adicionar no Início",
                                                  command=self.adicionar_primeiro)
        self.botao_adicionar_primeiro.pack()
        self.botao_adicionar_ultimo = tk.Button(self.master, text="Adicionar no Final", command=self.adicionar_ultimo)
        self.botao_adicionar_ultimo.pack()
        self.botao_remover_primeiro = tk.Button(self.master, text="Remover do Início", command=self.remover_primeiro)
        self.botao_remover_primeiro.pack()
        self.botao_remover_ultimo = tk.Button(self.master, text="Remover do Final", command=self.remover_ultimo)
        self.botao_remover_ultimo.pack()

        # Inicialização da visualização
        self.render_list()

    def render_list(self):
        self.canvas.delete("all")
        x = 50
        y = 100
        atual = self.lista.primeiro
        while atual is not None:
            # Desenha o nó
            self.canvas.create_rectangle(x, y, x + self.node_width, y + self.node_height, outline="black",
                                         fill="lightblue")
            self.canvas.create_text(x + self.node_width // 2, y + self.node_height // 2, text=str(atual.valor))

            # Desenha a seta para o próximo nó
            if atual.proximo is not None:
                self.canvas.create_line(x + self.node_width, y + self.node_height // 2, x + self.node_distance,
                                        y + self.node_height // 2, arrow=tk.FIRST)

            # Atualiza as coordenadas para o próximo nó
            x += self.node_distance
            atual = atual.proximo

    def adicionar_primeiro(self):
        valor = self.entry_valor.get()
        if valor.isdigit():
            valor = int(valor)
            self.lista.adicionar_primeiro(valor)
            self.render_list()
            self.entry_valor.delete(0, tk.END)

    def adicionar_ultimo(self):
        valor = self.entry_valor.get()
        if valor.isdigit():
            valor = int(valor)
            self.lista.adicionar_ultimo(valor)
            self.render_list()
            self.entry_valor.delete(0, tk.END)

    def remover_primeiro(self):
        valor_removido = self.lista.remover_primeiro()
        if valor_removido is not None:
            self.show_message(f"Valor removido do início: {valor_removido}")
            self.render_list()

    def remover_ultimo(self):
        valor_removido = self.lista.remover_ultimo()
        if valor_removido is not None:
            self.show_message(f"Valor removido do final: {valor_removido}")
            self.render_list()

    def show_message(self, message):
        top = tk.Toplevel(self.master)
        top.title("Mensagem")
        msg_label = tk.Label(top, text=message)
        msg_label.pack()
        ok_button = tk.Button(top, text="OK", command=top.destroy)
        ok_button.pack()


# Função principal para executar o programa
def main():
    root = tk.Tk()
    app = ListaLigadaInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
