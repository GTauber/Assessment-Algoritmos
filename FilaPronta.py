class Fila:
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self.itens = []

    def is_empty(self):
        # Verifica se a fila está vazia
        return len(self.itens) == 0

    def enqueue(self, item):
        # Adiciona um item no final da fila
        self.itens.append(item)

    def dequeue(self):
        # Remove e retorna o item do início da fila
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens.pop(0)  # Remove o primeiro item

    def peek(self):
        # Retorna o item do início da fila sem removê-lo
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[0]

    def size(self):
        # Retorna o número de elementos na fila
        return len(self.itens)

    def display(self):
        # Exibe o conteúdo da fila
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()

# Exemplo de uso
fila = Fila()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.display()  # Exibe: Fila: 10 20 30

print("Primeiro item da fila:", fila.peek())  # Saída: 10
print("Tamanho da fila:", fila.size())  # Saída: 3

fila.dequeue()
fila.display()  # Exibe: Fila: 20 30
print("Primeiro item da fila agora:", fila.peek())  # Saída: 20
