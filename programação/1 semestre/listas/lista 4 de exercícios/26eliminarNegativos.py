'''
26- Escreva um programa que receba uma lista de números e elimine os valores negativos,  retornando apenas os positivos.
Entrada: lista = [-1, 4, -3, 2]
Saída esperada: [4, 2]
'''

entrada = input("Digite os números (separados por vírgula): ")
lista = [int(x.strip()) for x in entrada.split(',')]
positivos = [n for n in lista if n >= 0]
print(positivos)