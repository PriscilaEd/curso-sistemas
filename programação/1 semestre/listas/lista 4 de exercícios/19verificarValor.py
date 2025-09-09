'''
19- Escreva um programa que verifique se um determinado valor está presente em uma lista e exiba a posição do valor caso ele exista.
Entrada: lista = [10, 20, 30] valor = 20
Saída esperada: 'Encontrado na posição 1'
'''

valores = input("Digite os números inteiros (separados por vírgula): ")
lista = [int(x.strip()) for x in valores.split(',')]
valor = int(input("Digite o valor que deseja procurar: "))

if valor in lista:
    posicao = lista.index(valor)
    print(f"Encontrado na posição {posicao}")
else:
    print("Valor não encontrado na lista.")