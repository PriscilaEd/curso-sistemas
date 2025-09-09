'''
30- Implemente um programa que rotacione os elementos de uma lista N posições à direita.
Entrada: lista = [1, 2, 3, 4, 5] n = 2
Saída esperada: [4, 5, 1, 2, 3]
'''

entrada = input("Digite os elementos da lista (separados por vírgula): ")
n = int(input("Digite o número de posições para rotacionar: "))
lista = [int(x.strip()) for x in entrada.split(',')]
n = n % len(lista)  
rotacionada = lista[-n:] + lista[:-n]
print(rotacionada)