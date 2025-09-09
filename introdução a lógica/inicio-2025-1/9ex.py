nota = int (input ('Digite uma nota (0-100): '))
while nota < 0 or nota>100: 
    print (f'Você digitou {nota}')
    nota = int (input ('Digite uma nota (0-100): '))

print (f'Nota digitada corretamente: {nota}')

while True:
    n=int (input ('Digite um número inteiro (9 p/sair): '))
    print (f'Você digitou {n}')
    if n == 9:
        print ('Parabéns, agora vamos sair no loop')
        break

a = [] # criando lista vazia
indice = 1 # contador de lançamentos 

while indice != 99:
    valor = int (input ('Digite o {indice} valor (ou 99 p/ finalizar) '))
    if valor == 99:
        print (f'A lista possui {indice-1} objetos')
        break
a.append (valor)
indice += 1

