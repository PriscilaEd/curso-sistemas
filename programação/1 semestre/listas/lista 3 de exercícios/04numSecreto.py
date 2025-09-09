'''
Crie um jogo onde o usuário precisa adivinhar um número secreto entre 1 e 100.
O programa deve dar dicas como "mais alto" ou "mais baixo".
Se o jogador acertar em menos de 5 tentativas, ganha um bônus.
Se não acertar em 10 tentativas, perde.
'''
numero = 44

for tentativa in range (1,11):
    print ('='*30)
    adivinhe = int (input (f'Adivinhe um número secreto entre 1 e 100 (obs: você tem 10 chances): ') )
    print ('-'*30)

    if adivinhe == 44:
        if tentativa < 5:
            print (f'Parabéns, você ganhou um bônus por acertar em menos de 5 tentativas!')
            print ('='*30)
            break

        else:
            print ('Parabéns, você acertou!')
            print ('='*30)

    elif adivinhe < 44:
        print ('Mais alto!')
        print ('-'*30)

    else:
        print (f'Mais baixo!')
        print ('-'*30)

else:
    print ('Que pena, acabaram suas chances...')
    print ('='*30)