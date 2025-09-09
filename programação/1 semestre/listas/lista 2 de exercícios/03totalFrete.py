'''
O usuário deve informar a distância em km e o peso do pacote.
Regras:
Se a distância for maior que 100 km, o frete é R$ 20 + R$ 0.10 por km extra
Se o peso for maior que 10 kg, adicione R$ 5 por quilo extra
Exiba o valor total do frete.
'''
print ('='*30)

distância = int (input ('Digite a distância em km: '))
print ('-'*30)
peso = int (input ('Digite o peso do pacote: '))
print ('-'*30)


extra = max(0, distância - 100)
frete = 20 + (extra * 0.10)

extra2 = max(0, peso - 10)
frete2 = frete + (extra2 * 5)


if distância <= 100: 
    print (f'O frete, calculando apenas a distância, é R$20,00')
else:
    print (f'O frete, calculando apenas a distância, é R${frete}')

if peso <= 10:
    print (f'O frete continua sendo R${frete}')
else:
    print (f'O frete total, calculando distância e peso, é R${frete2}')

print ('='*30)