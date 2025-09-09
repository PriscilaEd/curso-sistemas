'''
Um número inteiro pode ser igual ao produto de 3 números inteiros consecutivos, como, por exemplo, 120 = 4 x 5 x 6. Elabore um programa que, após ler um número n do teclado, verifique se n tem essa propriedade.
'''

print('=' * 30)
numero = int(input('Digite um número: '))
print('-' * 25)

resultado = 0
i = 1
achei = False
while not achei and resultado <= numero:  
    resultado = i * (i + 1) * (i + 2)
    if resultado == numero:
        print(f"{i} x {i+1} x {i+2} = {numero}")
        print('-' * 25)
        achei = True
    i = i + 1

if not achei:
    print(f"{numero} não é produto de três inteiros consecutivos.")
    print('-' * 25)

print('FIM')
print('=' * 30)