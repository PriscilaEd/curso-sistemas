'''
Escreva um programa que peça ao usuário uma senha e permita até 3 tentativas para acertá-la.
Se acertar, exiba "Acesso Permitido".
Se errar 3 vezes, exiba "Acesso Bloqueado".
'''

senha = '*abc123'

for tentativa in range (1,4):
    print ('='*30)
    digite = input (f'Digite a senha: ')
    print ('-'*25)

    if digite == senha:
        print ('Acesso permitido.')
        break
    
    elif tentativa < 3:
        print ('Erro, tente novamente.')
    
else:
    print ('Acesso bloqueado.')
print ('='*30)




