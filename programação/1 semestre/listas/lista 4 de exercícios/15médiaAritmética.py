'''
15- Faça um programa que leia uma lista de notas (valores float) e calcule a média aritmética das notas.
Entrada: notas = [7.5, 8.0, 9.0]
Saída esperada: 8.17
'''

entrada = input("Digite as notas (separadas por vírgula): ")
notas = [float(n.strip()) for n in entrada.split(',')]
media = sum(notas) / len(notas)
print(f"{media:.2f}")