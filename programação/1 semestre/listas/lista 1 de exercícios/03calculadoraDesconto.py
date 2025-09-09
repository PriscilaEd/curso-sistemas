original = float (input (f'Digite o valor original do produto: '))
desconto = float (input (f'Digite a porcentagem do desconto: '))
print ("-"*30)

Cálculo = original*desconto/100
Valor = original-Cálculo
print (f'O valor com desconto será de R${Valor}')