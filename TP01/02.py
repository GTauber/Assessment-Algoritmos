import random

# Definição das cartas de espadas
cartas_espadas = [f"{valor}♠" for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

# Embaralhar as cartas de espadas
random.shuffle(cartas_espadas)

# Simulação da mão inicial (todas as cartas embaralhadas)
mao_primeira = cartas_espadas.copy()  # Cartas na primeira mão (empilhadas, apenas a do topo é visível)
mao_segunda = []  # A outra mão (pode segurar apenas uma carta por vez)

def valor_carta(carta):
    # Função para atribuir valores numéricos às cartas
    valor = carta[:-1]  # Remove o naipe
    if valor == 'A':
        return 1
    elif valor == 'J':
        return 11
    elif valor == 'Q':
        return 12
    elif valor == 'K':
        return 13
    else:
        return int(valor)

def ordenar_cartas(mao):
    # Lista para manter as cartas ordenadas na primeira mão
    cartas_ordenadas = []

    while mao:
        # Passo 1: Pegue a carta visível (do topo) com a segunda mão
        mao_segunda = [mao.pop(0)]  # Retira a carta do topo da primeira mão
        carta_na_mao = mao_segunda[0]

        # Passo 2: Encontre a posição correta na mão ordenada
        inserido = False
        for i in range(len(cartas_ordenadas)):
            if valor_carta(carta_na_mao) < valor_carta(cartas_ordenadas[i]):
                # Passo 3: Insira a carta na posição correta
                cartas_ordenadas.insert(i, carta_na_mao)
                inserido = True
                break

        if not inserido:
            # Se a carta é a de maior valor, adiciona ao final
            cartas_ordenadas.append(carta_na_mao)

        # A segunda mão agora está vazia (colocou a carta na primeira mão)

    # Atualiza a mão inicial com as cartas ordenadas
    return cartas_ordenadas

# Executa o algoritmo de ordenação
mao_ordenada = ordenar_cartas(mao_primeira)

# Exibe o resultado
print("Cartas ordenadas:")
print(mao_ordenada)
