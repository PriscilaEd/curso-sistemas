'''
Receba o número final da placa de um carro (ex: 1234).
Baseado no último dígito:
1 ou 2: proibido na segunda
3 ou 4: proibido na terça
5 ou 6: proibido na quarta
7 ou 8: proibido na quinta
9 ou 0: proibido na sexta
'''
print ('='*30)

placa = int (input (f'Digite o número final da placa do carro: '))
final = placa % 10

print ('-'*30)

if final == 1 or final == 2:
    print (f'Proibido na segunda-feira.')

elif final == 3 or final == 4:
    print (f'Proibido na terça-feira.')

elif final == 5 or final == 6:
    print (f'Proibido na quarta-feira.')

elif final == 7 or final == 8:
    print (f'Proibido na quinta-feira.')

else:
    print (f'Proibido na sexta-feira.')

print ('='*30)