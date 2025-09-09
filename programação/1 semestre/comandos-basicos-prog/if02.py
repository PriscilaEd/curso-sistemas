valor = int (input ('Digite um valor inteiro: '))
p = valor > 500
novo_valor = 0
if valor > 500:
    print (f'{valor} MAIOR que 500')
    novo_valor = 10
else:
    print (f'{valor} MENOR ou IGUAL a 500')
    novo_valor = 2
print ('...FIM DO PROGRAMA...')
print (f'novo valor: {novo_valor}')