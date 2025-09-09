x1 = float (input (f'Digite o X1 da primeira coodernada: '))
y1 = float (input (f'Digite o Y1 da primeira coodernada: '))

print ('-'*30)

x2 = float (input (f'Digite o X2 da segunda coodernada: '))
y2 = float (input (f'Digite o Y2 da segunda coodernada: ')) 

print ('-'*30)

distância = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print (f'A distância entre esses dois pontos é de {distância}')