'''
1- Crie um programa que receba uma frase e conte quantas vogais (a, e, i, o, u) ela possui, considerando letras maiúsculas e minúsculas.
Entrada: frase = 'Programação é divertido'
Saída esperada: 8
'''

vogais = ['a', 'e', 'i', 'o', 'u']
# entrada de dados
frase = input ('Digite a frase: ')
# conventer para minúsculo
frase_min = frase.lower ()
# contar quantas vogais
soma = 0
for letra in frase_min:
    if letra in vogais:
        soma += 1

print(f'{soma}')

'''
Opção feita em sala:
ocorrencia_a = frase.count ('a')
ocorrencia_e = frase.count ('e')
ocorrencia_i = frase.count ('i')
ocorrencia_o = frase.count ('o')
ocorrencia_u = frase.count ('u')
soma = ocorrencia_a+ocorrencia_e+ocorrencia_i+ocorrencia_o+ocorrencia_u
print (f'Tem {soma} letras')
'''