'''
Peça ao usuário que informe uma senha.
Verifique as seguintes regras:
Deve ter ao menos 8 caracteres
Deve conter pelo menos um número
Deve conter pelo menos uma letra
Exiba mensagens indicando quais critérios foram ou não atendidos.
'''

senha = input ('Insira uma senha: ')

critérios = True

if len(senha) >= 8:
    print("A senha atende ao critério de 8 ou mais caracteres.")
else:
    print("Erro! A senha deve conter pelo menos 8 caracteres.")
    critérios = False

print ('='*30)

if any(char.isdigit() for char in senha):
    print("A senha atende ao critério de conter pelo menos um número.")
else:
    print("Erro! A senha deve conter pelo menos um número.")
    critérios = False

print ('='*30)

if any(char.isalpha() for char in senha):
    print("A senha atende ao critério de conter pelo menos uma letra.")
else:
    print("Erro! A senha deve conter pelo menos uma letra.")
    critérios = False

print ('='*30)

if critérios:
    print("Parabéns, essa é sua nova senha!")
else:
    print("Senha inválida. Corrija os erros acima.")
