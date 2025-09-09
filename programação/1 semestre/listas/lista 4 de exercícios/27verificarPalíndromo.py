'''
27- Desenvolva um programa que leia uma frase e verifique se ela é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, ignorando espaços e letras maiúsculas.
Entrada: texto = 'Socorram me subi no onibus em Marrocos'
Saída esperada: 'É palíndromo'
'''

texto = input("Digite uma frase: ")
normalizado = ''.join(texto.lower().split())

if normalizado == normalizado[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")