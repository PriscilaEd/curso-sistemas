numero = 100
pares = 0

while numero <= 200:
    print (numero)
    if numero % 2 == 0:
        # significa que é par
        pares = pares + 1
    numero += 1   # numero = numero + 1

print ("-"*30)
(print (f'Par: {pares}'))