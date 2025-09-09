'''
Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y, além do resto da divisão. Não é permitido usar as operações de divisão e resto de divisão do Python (use apenas soma e subtração).
'''
print ('='*30)
x = int(input("Digite o valor do dividendo: "))
print ('-'*25)
y = int(input("Digite o valor do divisor: "))
print ('-'*25)

if y == 0:
    print("Erro: divisão por zero não é permitida.")
else:
    quociente = 0
    resto = x
    while resto >= y:
        resto = resto - y
        incremento = 1
        quociente = quociente - (-incremento)  

    print(f'Quociente = {quociente}')
    print(f'Resto = {resto}')
print ('='*30)