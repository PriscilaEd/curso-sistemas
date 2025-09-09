temperatura = int (input (f'Coloque o valor da temperatura: '))

if temperatura < 7:
    print (f'Congelando!')

elif temperatura < 10:
    print (f'Frio!')

elif temperatura < 26:
    print (f'Ótimo!')

else:
    print (f'Muito quente!')