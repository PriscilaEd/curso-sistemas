'''
Escreva um programa que peça dois números inteiros a e b (com a < b) e calcule a soma de todos os números ímpares entre eles.
Exemplo:
Entrada: 1 e 10 → Saída: 1 + 3 + 5 + 7 + 9 = 25
'''

print ('='*30)
a = int(input("Digite o menor valor: "))
b = int(input("Digite o maior valor: "))
print ('-'*25)

# Verifica se a < b
if a >= b:
    print("Erro: o primeiro número deve ser o menor valor.")
else:
    soma = 0
    print("Soma dos ímpares:", end=" ")
    primeiro = True
    for i in range(a, b + 1):
        if i % 2 == 1:
            if not primeiro:
                print("+", end=" ")
            print(i, end=" ")
            soma += i
            primeiro = False
    print("=", soma)

print ('='*30)