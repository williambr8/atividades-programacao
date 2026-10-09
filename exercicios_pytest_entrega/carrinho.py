class CarrinhoDeCompras:

    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            raise ValueError("Item não encontrado")

    def listar_itens(self):
        return self.itens
