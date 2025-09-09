'''
18- Desenvolva um programa que ordene de forma crescente os elementos de uma lista fornecida pelo usuário.
Entrada: valores = [9, 1, 4, 3]
Saída esperada: [1, 3, 4, 9]
'''

valores = input("Digite os números inteiros separados por vírgula: ")
lista = [int(x.strip()) for x in valores.split(',')]
lista_ordenada = sorted(lista)
print(lista_ordenada)