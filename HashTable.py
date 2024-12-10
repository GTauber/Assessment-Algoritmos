class HashTable:
    def __init__(self, capacidade=10):
        # Inicializa a tabela hash com uma capacidade fixa
        self.capacidade = capacidade  # Tamanho da tabela
        self.tabela = [[] for _ in range(capacidade)]  # Lista de listas para o encadeamento
        self.size = 0  # Contador de elementos na tabela

    def hash(self, chave):
        # Função hash simples que retorna um índice
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        # Insere um valor associado à chave na tabela hash
        indice = self.hash(chave)  # Obtém o índice usando a função hash
        for par in self.tabela[indice]:  # Verifica se a chave já existe
            if par[0] == chave:
                par[1] = valor  # Atualiza o valor se a chave já estiver presente
                return
        
        # Se a chave não existe, adiciona uma nova entrada
        self.tabela[indice].append([chave, valor])
        self.size += 1  # Incrementa o contador de elementos

    def buscar(self, chave):
        # Busca o valor associado à chave na tabela hash
        indice = self.hash(chave)  # Obtém o índice usando a função hash
        for par in self.tabela[indice]:  # Verifica a lista encadeada
            if par[0] == chave:
                return par[1]  # Retorna o valor se a chave for encontrada
        return None  # Retorna None se a chave não existir

    def remover(self, chave):
        # Remove o par chave-valor da tabela hash
        indice = self.hash(chave)  # Obtém o índice usando a função hash
        for i, par in enumerate(self.tabela[indice]):  # Verifica a lista encadeada
            if par[0] == chave:
                del self.tabela[indice][i]  # Remove o par da lista
                self.size -= 1  # Decrementa o contador de elementos
                return True  # Retorna True se a chave foi removida
        return False  # Retorna False se a chave não foi encontrada

    def __str__(self):
        # Retorna uma representação em string da tabela hash
        resultado = []
        for lista in self.tabela:
            for par in lista:
                resultado.append(f"{par[0]}: {par[1]}")
        return "{ " + ", ".join(resultado) + " }"

# Exemplo de uso
tabela_hash = HashTable()
tabela_hash.inserir("chave1", "valor1")
tabela_hash.inserir("chave2", "valor2")
tabela_hash.inserir("chave3", "valor3")

print("Tabela Hash após inserções:", tabela_hash)  # Mostra os pares chave-valor inseridos

# Busca de valores
print("Busca 'chave2':", tabela_hash.buscar("chave2"))  # Saída: valor2
print("Busca 'chave4':", tabela_hash.buscar("chave4"))  # Saída: None

# Remoção de um par
tabela_hash.remover("chave2")
print("Tabela Hash após remoção de 'chave2':", tabela_hash)  # Mostra a tabela após remoção
