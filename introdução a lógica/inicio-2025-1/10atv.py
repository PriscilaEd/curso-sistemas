# Adivinhar um numero secreto. (sai do sistema depois de adivinhar)
# Fazer numero secreto é 7. Continue pedindo até acertar

while True:
    num = int (input (f'Adivinhe o número secreto: '))
    print (f'Você digitou {num}')
    if num == 7:
        print (f'Parabéns, você acertou!')
        break
    else: 
        print (f'Número errado, continue tentando!')

# Peça ao usuário números e some todos
# até que ele digite 0. Exiba a soma final.

soma = 0
num = int (input ('Digite um número (o para parar): '))
while num != 0:
    soma+=num
    num = int (input ('Digite um número (0 para parar): '))
    print (f'Soma total: {soma}')

soma = 0
while True:
    num = int (input ('Digite um número (0 para parar): '))
    if num == 0:
        print (f'Soma total: {soma}')
        break
    soma+=num

