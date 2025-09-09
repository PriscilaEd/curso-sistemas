'''
24- Desenvolva um programa que receba duas listas de igual tamanho e crie uma nova lista intercalando seus elementos.
Entrada: a = [1,3,5] b = [2,4,6]
Saída esperada: [1,2,3,4,5,6]
'''

a = input("Digite os elementos da primeira lista (separados por vírgula): ")
b = input("Digite os elementos da segunda lista (separados por vírgula): ")
lista_a = [int(x.strip()) for x in a.split(',')]
lista_b = [int(x.strip()) for x in b.split(',')]

if len(lista_a) == len(lista_b):
    intercalada = [val for par in zip(lista_a, lista_b) for val in par]
    print(intercalada)
else:
    print("As listas devem ter o mesmo tamanho.")