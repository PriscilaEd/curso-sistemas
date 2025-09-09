'''
22- Crie um programa que receba uma lista de inteiros e um valor X, e retorne apenas os valores maiores que X.
Entrada: lista = [5, 8, 12, 3] x = 6
Saída esperada: [8, 12]
'''

entrada = input("Digite os números inteiros (separados por vírgula): ")
lista = [int(x.strip()) for x in entrada.split(',')]
x = int(input("Digite o valor de X: "))
maiores = [n for n in lista if n > x]
print(maiores)