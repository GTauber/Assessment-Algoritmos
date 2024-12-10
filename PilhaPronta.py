# esse exemplo usa as funções do python

class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        # Verifica se a pilha está vazia
        return len(self.itens) == 0

    def push(self, item):
        # Adiciona um item no topo da pilha
        self.itens.append(item)

    def pop(self):
        # Remove e retorna o item do topo da pilha
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        # Retorna o item do topo sem removê-lo
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        # Retorna o número de elementos na pilha
        return len(self.itens)

    def display(self):
        # Exibe o conteúdo da pilha
        print("Pilha:", self.itens)

# Exemplo de uso
pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(30)
print("Topo da pilha:", pilha.peek())  # Saída: 30
print("Tamanho da pilha:", pilha.size())  # Saída: 3
pilha.display()  # Exibe a pilha: [10, 20, 30]

pilha.pop()
print("Após remover o topo:")
pilha.display()  # Exibe a pilha: [10, 20]
print("Topo da pilha agora:", pilha.peek())  # Saída: 20
