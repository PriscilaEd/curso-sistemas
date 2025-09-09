pequena = float (input ('Digite a quantidade de camisetas pequenas vendidas: ')) 
média = float (input ('Digite a quantidade de camisetas médias vendidas: '))
grande = float (input ('Digite a quantidade de camisetas grandes vendidas: ')) 

print ("-"*30)
valor = (pequena*10.00)+(média*12.00)+(grande*15.00)

print (f'O valor total de {pequena} camisetas pequenas, {média} camisetas médias e {grande} camisetas grandes é de R${valor}')
