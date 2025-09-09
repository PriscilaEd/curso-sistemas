'''
17- Implemente um programa que receba uma lista de inteiros e retorne uma nova lista com todos os elementos duplicados removidos.
Entrada: lista = [1, 2, 2, 3, 1, 4]
Saída esperada: [1, 2, 3, 4]
'''

valores = input("Digite os números inteiros separados por vírgula: ")
lista = [int(x.strip()) for x in valores.split(',')]
duplicados = list(set(lista))
print(duplicados)