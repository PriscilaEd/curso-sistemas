# Crie um condicional que teste o valor de 3 variáveis (A, B, C) e exiba "ok" SE (A e B são iguais e C seja diferente de 5) ou (A e B sejam diferentes de 5 e C não seja um número inteiro)

A = input ('Digite o valor de A: ')
B = input ('Digite o valor de B: ')
C = input ('Digite o valor de C: ')

if (A==B and C !=5) or (A != 5 and B !=5 and C.isdigit ()== True):
    print ('Ok, condição atendida')
else:
    print ('Condição NÃO atendida')