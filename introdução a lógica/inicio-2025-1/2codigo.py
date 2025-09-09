# Crie um código que receba 3 cores para definir uniforme de time
# (cor1, cor2 e cor3)
# faça o teste: se cor1 = cor2 e cor3 = cor1 OU
# se cor1 diferente de cor2 e cor1 diferente de cor3
# imprima "ótima escolha de cores"

print ('Vamos definir as cores do time:')
cor1 = str (input ('Digite a primeira cor: '))
cor2 = str (input ('Digite a segunda cor: '))
cor3 = str (input ('Digite a terceira cor: '))

if (cor1 == cor2 and cor2+cor3 == cor1) or (cor1 != cor2 and cor1 != cor3):
    print ('Ótima escolha de cores!')