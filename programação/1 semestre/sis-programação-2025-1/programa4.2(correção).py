# ENTRADA
qtd_pasteis = int (input ("Digite a quantidade de pasteis: "))
qtd_refri = int (input ("Digite a quantidade de refrigerantes: "))
valor_pasteis = int (input ("Digite o valor do pastel: R$"))
valor_refri = int (input ("Digite o valor do refrigerante: R$"))

# PROCESSAMENTO
pasteis = qtd_pasteis*valor_pasteis
refri = qtd_refri*valor_refri
resultado = pasteis+refri

# SAÍDA 
print ("-"*30)
print (f'O valor de vendas de pasteis foi de R${pasteis}')
print (f'O valor de vendas de refrigerantes foi de R${refri}')
print (f'O valor total de vendas foi de R${resultado}')