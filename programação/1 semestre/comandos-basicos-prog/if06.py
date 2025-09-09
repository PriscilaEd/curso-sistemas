número = int (input (f'Digite o número do mês desejado: '))

print ('='*30)

# 31 = (1, 3, 5, 7, 8, 10, 12)
# 30 = (4, 6, 9, 11)

if (número == 1) or (número == 3) or (número == 5) or (número == 7) or (número == 8) or (número == 10) or (número == 12): 
    print ('Esse mês tem 31 dias')
elif (número == 4) or (número == 6) or (número == 9) or (número == 11):
    print ('Esse mês tem 30 dias')
elif número == 2:
    print ('Esse mês tem 28 OU 29 dias')
else:
    print ('Mês inválido')

print ('='*30)

if número in [1,3,5,7,8,10,12]:
    print ('Esse mês tem 31 dias')
elif número in [4,6,9,11]:
    print ('Esse mês tem 30 dias')
elif número == 2:
      print ('Esse mês tem 28 OU 29 dias')
else:
    print ('Mês inválido')