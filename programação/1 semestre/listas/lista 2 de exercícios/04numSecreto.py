'''
Peça um número ao usuário.
Compare com um número secreto fixo (ex: 7) e diga se:
Acertou
Está acima
Está abaixo
O usuário deverá ter 5 tentativas, para isso utilize uma estrutura de repetição.
'''

número = 22

for tentativa in range(1, 6):
    adivinhe = int (input (f'Adivinhe o número secreto: '))
    print ('='*30)

    if adivinhe == 22:
     print (f'Parabéns, você acertou!')
     print ('='*30)
     break

    elif adivinhe < 22:
        print (f'Chutou muito baixo!')
        print ('-'*30)

    else:
        print (f'Chutou muito acima!')
        print ('-'*30)

else:
    print(f'Que pena, suas atentativas acabaram!')
    print ('='*30)