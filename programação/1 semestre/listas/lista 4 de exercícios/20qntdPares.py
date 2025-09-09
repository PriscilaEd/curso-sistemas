'''
20- Faça um programa que conte e exiba quantos números pares existem em uma lista de inteiros.
Entrada: numeros = [2, 3, 4, 5, 6]
Saída esperada: 3
'''

números = input("Digite os números inteiros (separados por vírgula): ")
lista = [int(x.strip()) for x in números.split(',')]
pares = [n for n in lista if n % 2 == 0]
print(f"Quantidade de números pares: {len(pares)}")