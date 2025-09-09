porcentagem = 30
valor = float (input(f'Digite o valor da roupa: R$'))

print ('-'*30)

desconto = (porcentagem/100)*valor
total = valor-desconto

print (f'O valor dessa roupa com desconto passa de R${valor} para R${total}')
