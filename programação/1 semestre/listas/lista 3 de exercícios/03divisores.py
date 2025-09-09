'''
Faça um programa para listar todos os divisores de um número ou dizer que o número é primo caso não existam divisores
Ao final, verifique se o usuário deseja analisar outro número
'''

while True:
    numero = int (input (f'Digite um número: '))
    primo = True

    for i in range (2, numero):
        if numero % i == 0:
            print (f'Divisor: {i}')
            primo = False
        
    if primo:
        print (f'O número é primo.')
    
    print ('='*30)
    
    continuar = int (input (f'Deseja testar outro número? (S/N): ')) 
    print ('='*30)
    if continuar == 'N':
        break

    elif continuar != 'S':
        print ('Resposta inválida.')