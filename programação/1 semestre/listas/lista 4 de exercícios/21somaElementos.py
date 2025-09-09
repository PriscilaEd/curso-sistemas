'''
21 Implemente um programa que leia uma lista de inteiros e calcule a soma de todos os elementos.
Entrada: lista = [1, 2, 3, 4]
Saída esperada: 10
'''

entrada = input("Digite os números inteiros (separados por vírgula): ")
lista = [int(x.strip()) for x in entrada.split(',')]
soma = sum(lista)
print(soma)