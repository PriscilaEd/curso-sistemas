# EXERCÍCIO: Em uma cozinha de restaurante existem apenas os igredientes a seguir.
# Exiba todas as possíveis combinações (não importa a sequência) utilizando até 3 igredientes e quantas receitas isto totaliza.
# Igredientes disponíveis: tomate, agrião, filé de frango, pão de queijo, mel.
# Ao final, exiba a quantidade de combinações.

from itertools import combinations

ingredientes = ['tomate', 'agrião', 'filé de frango', 'pão de queijo', 'mel']
combinações = []

for r in range(1, 4):  # de 1 a 3 ingredientes
    for combo in combinations(ingredientes, r):
        combinações.append(combo)

# Exibir combinações
for i, c in enumerate(combinações, 1):
    print(f'{i}. Combinação: {c}')

print(f'Total de combinações: {len(combinações)}')
