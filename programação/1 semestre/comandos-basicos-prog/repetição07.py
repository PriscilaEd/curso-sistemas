'''
numero_inicial = int (input ('Primeiro valor: '))
numero_final = int (input ('Segundo valor: '))

for i in range (numero_inicial, numero_final+1): # i - iterador
    if i%2 == 0:
        print (i)
'''

times = ["SPFC", "SANTOS", "FLA", "FLU"]

'''
SPFC X SANTOS
SPFC X FLA 
SPFC X FLU 

SANTOS X SPFC
SANTOS X FLA
'''

for time_casa in times:
    for time_visitante in times:
        if time_casa != time_visitante:
            print (f'{time_casa} x {time_visitante}')
        