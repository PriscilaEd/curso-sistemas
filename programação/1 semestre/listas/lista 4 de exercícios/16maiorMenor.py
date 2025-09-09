'''
16- Crie um programa que leia uma lista de números inteiros e exiba o maior e o menor valor contido nela.
Entrada: valores = [3, 8, 2, 10, 5]
Saída esperada: 'Maior: 10, Menor: 2'
'''

valores = input("Digite os números inteiros separados por vírgula: ")
lista = [int(x.strip()) for x in valores.split(',')]
maior = max(lista)
menor = min(lista)
print(f"Maior: {maior}, Menor: {menor}")