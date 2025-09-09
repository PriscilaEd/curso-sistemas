'''
25- Implemente um programa que leia os preços de produtos em um carrinho e calcule o valor total da compra.
Entrada: carrinho = [10.5, 20.0, 5.25]
Saída esperada: 35.75
'''

preços = input("Digite os preços dos produtos (separados por vírgula): ")
carrinho = [float(x.strip()) for x in preços.split(',')]
total = round(sum(carrinho), 2)
print(total)