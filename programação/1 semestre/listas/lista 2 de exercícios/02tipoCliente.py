'''
Peça o tipo de cliente (comum, premium ou vip) e o valor de uma compra.
Regras de desconto:
comum: sem desconto
premium: 10% de desconto
vip: 20% de desconto
Mostre o valor final com o desconto aplicado.
'''

cliente = input (f'Insira o tipo de cliente (comum, premium ou vip): ')
print ('='*30)
valor = float (input (f'Insira o valor da compra: R$'))
print ('='*30)

if cliente == 'comum': 
    print (f'Sem desconto. O valor final é o mesmo do total: R${valor}.')

elif cliente == 'premium':
    totalA = valor - (valor*0.10)
    print (f'Desconto de 10%. O valor final é de R${totalA}.')

elif cliente == 'vip':
    totalB = valor - (valor*0.20)
    print (f'Desconto de 20%. O valor final é de R${totalB}.')

else: 
    print (f'Digite um cliente válido.')