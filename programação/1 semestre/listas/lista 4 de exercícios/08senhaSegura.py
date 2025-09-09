'''
8- Desenvolva um programa que verifique se uma senha é segura. Uma senha segura deve ter pelo menos 8 caracteres, incluir ao menos uma letra maiúscula, um número e um caractere especial.
Entrada: senha = 'Segura123!'
Saída esperada: 'Senha segura'   
'''

senha = input('Digite a senha: ')

maiuscula = any(letra.isupper() for letra in senha)
numero = any(letra.isdigit() for letra in senha)
especial = any(not letra.isalnum() for letra in senha) 
tamanho = len(senha) >= 8

if maiuscula and numero and especial and tamanho:
    print('Senha segura')
else:
    print('Senha insegura')