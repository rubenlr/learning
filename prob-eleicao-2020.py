matriz = [
    {'nome': 'Janaina', 'arrecadado': 746337,
        'custoMaisProvavel': 15, 'maximo': 10, 'minimo': 25},
    {'nome': 'Bolini', 'arrecadado': 383323,
        'custoMaisProvavel': 7, 'maximo': 4, 'minimo': 13},
    {'nome': 'Naira', 'arrecadado': 452941,
        'custoMaisProvavel': 10, 'maximo': 5, 'minimo': 15},
    {'nome': 'Japão', 'arrecadado': 176639,
        'custoMaisProvavel': 6, 'maximo': 3, 'minimo': 10},
    {'nome': 'Cris', 'arrecadado': 347597,
        'custoMaisProvavel': 17, 'maximo': 13, 'minimo': 30},
    {'nome': 'Matheus', 'arrecadado': 159049,
        'custoMaisProvavel': 10, 'maximo': 6, 'minimo': 15},
    {'nome': 'Diogo', 'arrecadado': 149842,
        'custoMaisProvavel': 15, 'maximo': 10, 'minimo': 25},
    {'nome': 'Wafá', 'arrecadado': 166957,
        'custoMaisProvavel': 15, 'maximo': 8, 'minimo': 20},
    {'nome': 'Romero', 'arrecadado': 38088,
        'custoMaisProvavel': 3, 'maximo': 2, 'minimo': 4},
    {'nome': 'Marcelo', 'arrecadado': 79411,
        'custoMaisProvavel': 10, 'maximo': 2, 'minimo': 20},
    {'nome': 'Pieri', 'arrecadado': 73234,
        'custoMaisProvavel': 10, 'maximo': 8, 'minimo': 20},
    {'nome': 'Naomy', 'arrecadado': 37539,
        'custoMaisProvavel': 4, 'maximo': 2.5, 'minimo': 5},
    {'nome': 'Minhonzinho', 'arrecadado': 87339,
        'custoMaisProvavel': 10, 'maximo': 3, 'minimo': 20}
]

print("nome,minimo,maximo,provavel,media ponderada,media forçando o meio")

for linha in matriz:
    item = linha
    nome = item['nome']
    arrecadado = item['arrecadado']
    minimo = int(arrecadado / item['minimo'])
    maximo = int(arrecadado / item['maximo'])
    meio = int(arrecadado / item['custoMaisProvavel'])
    mediaPonderada = int((minimo + maximo + meio) / 3)
    meioForte = int((minimo + maximo + meio + meio + meio) / 5)

    print(f"{nome},{minimo},{maximo:0},{meio},{mediaPonderada},{meioForte}")
