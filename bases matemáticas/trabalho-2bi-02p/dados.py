'''
Você deverá desenvolver uma aplicação simples em Python que simule o gerenciamento de dados de uma rede de sensores em uma cidade inteligente. Os sensores monitoram a temperatura em diferentes pontos da cidade em determinados períodos do dia.

A cidade será representada por uma matriz 5x5, onde:
• Cada célula da matriz representa uma região.
• Os valores dentro da matriz representam a temperatura (em °C) capturada naquela região.

Requisitos
O programa deverá:
1) Gerar automaticamente uma matriz 5x5 com valores aleatórios entre 15°C e 40°C.
2) Exibir a matriz formatada, com os valores de temperatura.
3) Calcular e exibir:
• A média de temperatura geral da cidade.
• A região (linha e coluna) com a maior e a menor temperatura.
• A média de temperatura por linha (região horizontal).
• A média de temperatura por coluna (região vertical).
4) Permitir que o usuário substitua manualmente a temperatura de uma determinada célula.
5) Gerar uma nova matriz com temperaturas convertidas para Fahrenheit (fórmula: F = C * 1.8 + 32).
'''

import random

print ('='*30)

def gerar_matriz():
    return [[random.randint(15, 40) for _ in range(5)] for _ in range(5)]

def exibir_matriz(matriz):
    print("Matriz de Temperaturas (°C):")
    for linha in matriz:
        print('  '.join(f"{temp:>2}°" for temp in linha))
    print ('='*30)

def media_geral(matriz):
    total = sum(sum(linha) for linha in matriz)
    return total / 25

def extremos(matriz):
    maior = menor = matriz[0][0]
    maior2 = menor2 = (0, 0)
    for a in range(5):
        for b in range(5):
            if matriz[a][b] > maior:
                maior = matriz[a][b]
                pos_maior = (a, b)
            elif matriz[a][b] < menor:
                menor = matriz[a][b]
                pos_menor = (a, b)
    return maior, maior2, menor, menor2

def media_linhas(matriz):
    return [sum(linha)/5 for linha in matriz]

def media_colunas(matriz):
    return [sum(matriz[i][j] for i in range(5))/5 for j in range(5)]

def substituir(matriz):
    try:
        linha = int(input("Digite o número da linha: "))
        print ('-'*30)
        coluna = int(input("Digite o número da coluna: "))
        print ('-'*30)
        novo_valor = int(input("Digite a nova temperatura em °C: "))
        if 0 <= linha < 5 and 0 <= coluna < 5:
            matriz[linha][coluna] = novo_valor
            print ('-'*30)
            print("Temperatura atualizada.")
            print ('='*30)
        else:
            print("Coordenadas inválidas, dê os números de 1 a 4!")
    except ValueError:
        print("Entrada inválida.")

def converter_para_fahrenheit(matriz):
    return [[round(c * 1.8 + 32, 1) for c in linha] for linha in matriz]

matriz = gerar_matriz()
exibir_matriz(matriz)

print(f"Média da cidade: {media_geral(matriz):.2f}°C")

maior, maior2, menor, menor2 = extremos(matriz)
print(f"Maior temperatura: {maior}°C na posição {maior2}")
print(f"Menor temperatura: {menor}°C na posição {menor2}")
print ('='*30)

print("Média por linha:")
for i, media in enumerate(media_linhas(matriz)):
    print(f"Linha {i}: {media:.2f}°C")
print ('='*30)

print("Média por coluna:")
for i, media in enumerate(media_colunas(matriz)):
    print(f"Coluna {i}: {media:.2f}°C")
print ('='*30)

substituir(matriz)
exibir_matriz(matriz)

matriz_fahrenheit = converter_para_fahrenheit(matriz)
print("Matriz convertida para Fahrenheit:")
for linha in matriz_fahrenheit:
    print('  '.join(f"{temp:>5}°" for temp in linha))

print ('='*30)