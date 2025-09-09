'''
23- Escreva um programa que inverta a ordem dos elementos de uma lista.
Entrada: lista = [1, 2, 3]
Saída esperada: [3, 2, 1]
'''

entrada = input("Digite os números inteiros (separados por vírgula): ")
lista = [int(x.strip()) for x in entrada.split(',')]
invertida = lista[::-1]
print(invertida)