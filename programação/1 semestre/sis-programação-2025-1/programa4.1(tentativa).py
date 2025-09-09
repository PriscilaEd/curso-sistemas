# Faça um algoritmo que calcula o valor a pagar em uma lanchonete, dada a quantidade de pastéis comprados e o preço de cada pastel, e a quantidade de refrigerantes comprados e o preço de cada refrigerante, determine o valor a ser pago!

#input = entrada de dados
#int = para indicar número inteiro

qtd_pasteis = int (input ("Digite a quantidade de pasteis: "))
valor_pasteis = int (input ("Digite o valor do pastel: R$"))
pasteis = qtd_pasteis*valor_pasteis

print (f'O valor total dos pasteis foi R${pasteis},00')
print ("-"*30)

qtd_refri = int (input ("Digite a quantidade de refrigerantes: "))
valor_refri = int (input ("Digite o valor do refrigerante: R$"))
refri = qtd_refri*valor_refri

print (f'O valor total dos refrigerantes foi R${refri},00')
print ("-"*30)

resultado = pasteis+refri

print (f'O valor total de vendas foi de R${pasteis},00 de pasteis e R${refri},00 de refrigerantes, totalizando R${resultado},00')