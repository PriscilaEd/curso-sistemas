# EXERCÍCIO: Em uma cozinha de restaurante existem apenas os igredientes a seguir.
# Exiba todas as possíveis combinações (não importa a sequência) utilizando até 3 igredientes e quantas receitas isto totaliza.
# Igredientes disponíveis: tomate, agrião, filé de frango, pão de queijo, mel.
# Ao final, exiba a quantidade de combinações.

ingredientes = ['tomate', 'agrião', 'filé de frango', 'pão de queijo', 'mel']
combinações = []

contador = 0

for a in ingredientes: 
    for b in ingredientes:
        for c in ingredientes:
            print (f'As combinações são {a}, {b} e {c}')
            contador += 1
            print(f'{contador}. Combinação: {a}, {b}, {c}')

print (f'O número total de combinações é igual a {contador}')
