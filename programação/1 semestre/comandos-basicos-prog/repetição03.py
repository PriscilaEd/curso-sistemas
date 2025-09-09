# COMO FAZER PARA CONTAR A QUANTIDADE DE NÚMEROS PARES ENTRE DOIS NÚMEROS QUAISQUER?

numero = int (input ('Digite o primeiro valor:'))
numero2 = int (input ('Digite o segundo valor: '))

pares = 0
while numero <= numero2:
    print (numero)
    if numero % 2 == 0:
        # par
        # print (f'par)
        pares = pares + 1
    numero += 1 # numero = numero + 1
print ("-"*20)
print (f'Par: tem {pares} numeros')