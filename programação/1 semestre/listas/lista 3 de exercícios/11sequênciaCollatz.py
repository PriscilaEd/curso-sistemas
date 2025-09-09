'''
Implemente um programa que peça ao usuário um número positivo n e mostre a sequência de Collatz para ele:
Se n é par, divida por 2.
Se n é ímpar, multiplique por 3 e some 1.
Repita até n se tornar 1.

Exemplo para n = 6:
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
'''

numero = int(input("Digite um número positivo: "))

if numero <= 0:
    print("Erro! Esse número não é positivo.")
else:
    while numero != 1:
        print(numero, end=" → ")
        if numero % 2 == 0:
            numero = numero // 2  
        else:
            numero = 3 * numero + 1  
    print(1)  
