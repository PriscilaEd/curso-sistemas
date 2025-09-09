print ('='*30)

numero = 30
soma = 0
for divisor in range (1, numero):
    resto = numero % divisor
    if resto == 0:
        soma = soma + divisor
        print (divisor, end = '+')
print (f' = {soma}')
if soma == numero:
    print (f'{numero} perfeito')

else: print (f'{numero} IMperfeito')

print ('='*30)