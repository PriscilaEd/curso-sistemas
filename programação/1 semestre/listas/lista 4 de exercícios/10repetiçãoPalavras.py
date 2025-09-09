'''
10- Desenvolva um programa que conte quantas vezes uma determinada palavra aparece em uma frase, sem diferenciar maiúsculas de minúsculas.
Entrada: frase = 'Python é bom. python é divertido.' palavra = 'python'
Saída esperada: 2
'''

frase = input ('Digite a frase: ')
palavra = input ('Digite a palavra que deseja contar: ')
frase_minuscula = frase.lower()
palavra_minuscula = palavra.lower()
ocorrencias = frase_minuscula.count(palavra_minuscula)
print(f'{ocorrencias}')