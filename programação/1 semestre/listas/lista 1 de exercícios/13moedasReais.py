a = float (input (f'Digite a quantidade de moedas de 0,5 centavos: '))
b = float (input (f'Digite a quantidade de moedas de 0,10 centavos: '))
c = float (input (f'Digite a quantidade de moedas de 0,25 centavos: '))
d = float (input (f'Digite a quantidade de moedas de 0,50 centavos: '))
e = float (input (f'Digite a quantidade de moedas de 1,00 real: '))

reais = (a+0.05)+(b+0.10)+(c+0.25)+(d+0.50)+(e+1.00)
print ("-"*30)

print (f'O valor total economizado é de R${reais}')