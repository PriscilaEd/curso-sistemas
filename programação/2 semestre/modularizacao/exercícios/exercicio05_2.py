from exercicio05_1 import *
# * para pra importar todas as funções

print ("1- Circulo")
print ("2- Triagulo")
print ("3- Retangulo")
opcao = int(input("Escolha a figura: "))
if opcao == 1:
    tipo = "circulo"
    raio = float(input("Digite raio: "))
    area = area_circulo(raio)
    perimetro = perimetro_circulo(raio)
elif opcao == 2:
    tipo = "triangulo"
    l1 = float(input('Digite lado1: '))
    l2 = float(input('Digite lado2: '))
    l3 = float(input('Digite lado3: '))
    area = area_triangulo(l1,l2,l3)
    perimetro = perimetro_triangulo(l1,l2,l3)
elif opcao == 3:
    tipo = "retangulo"
    l1 = float(input('Digite lado1: '))
    l2 = float(input('Digite lado2: '))
    area = area_retangulo(l1, l2)
    perimetro = perimetro_retangulo(l1, l2)

print(f"Calculos - {tipo}")
print(f"Área calculada {round(area, 1)}")
print(f"Perimetro: {round(perimetro, 3)}")