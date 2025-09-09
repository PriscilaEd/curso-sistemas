# Pergunte ao usuário o mês do ano em números entre 1 e 12. Seu programa deve retornar por extenso o mês correspondente.
# Ex: mes = 1 -> retorna janeiro
# mês = 7 -> retorna julho

número = int (input (f'Digite o número do mês desejado: '))

print ('-'*30)

if número == 1:
    print ('O mês é janeiro')
elif número == 2:
    print ('O mês é fevereiro')
elif número == 3:
    print ('O mês é março')
elif número == 4:
    print ('O mês é abril')
elif número == 5:
    print ('O mês é maio')
elif número == 6:
    print ('O mês é junho')
elif número == 7:
    print ('O mês é julho')
elif número == 8:
    print ('O mês é agosto')
elif número == 9:
    print ('O mês é setembro')
elif número == 10:
    print ('O mês é outubro')
elif número == 11:
    print ('O mês é novembro')
elif número == 12:
    print ('O mês é dezembro')
else:
    print ('Mês inválido')
