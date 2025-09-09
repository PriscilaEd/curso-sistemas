'''
Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês, sem usar a fórmula de juros compostos
O usuário deve informar quanto será investido por mês e qual será a taxa de juros mensal
O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês considerando os juros compostos), e perguntar ao usuário se ele deseja que seja calculado o ano seguinte, sucessivamente
Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma taxa de juros de 1% ao mês, o programa forneceria a seguinte saída:
Saldo do investimento após 1 ano: R$ 1268.25
Deseja processar mais um ano? (S/N)
'''

print ('='*30)
valor = float (input (f'Insira o valor que será investido mensalmente: '))
juros = float (input (f'Digite a taxa de juros em %: ')) / 100
print ('-'*25)

saldo = 0

while True:
    for mes in range(12):
        saldo += valor
        saldo += saldo * juros

    print (f'O saldo após um ano é R${saldo},00')
    print ('='*30)

    repetição = input ('Deseja calcular mais um ano? (S/N): ')
    print ('-'*30)
    if repetição != 'S':
        break
print ('='*30)
