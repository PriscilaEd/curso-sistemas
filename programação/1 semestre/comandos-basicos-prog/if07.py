# A IDEIA DE ALGORITMO, PSEUDOCODIGO
# PROGRAMAÇÃO SEQUENCIAL - ENTRADA, PROCESSAMENTO, SAIDA
# PROGRAMAÇÃO CONDICIONAL - IF, IF-ELSE, IF-ELIF-ELIF-ELSE
# RECONHECER SYNTAXE DE PROGRAMA EM PYTHON

"""
FAZER UM PROGRAMA PARA IDENTIFICAR SE UM NUMERO INTEIRO É PAR OU IMPAR
"""

num = int (input ('Digite um número: '))
if num % 2 == 0:
    print (f'{num} é par')
else: 
    print (f'{num} é ímpar')

"""
PEÇA UMA TEMPERATURA EM CELCIUS E MOSTRE A CLASSIFIAÇÃO:
    Menor que 10: muito frio
    Entre 10 e 25: clima agradável
    Acima de 25: Calor
"""

temp = int (input ('Digite a temperatura: '))
if temp < 10:
    print (f'Muito frio')
elif temp >= 10 and temp < 25: 
    print (f'Clima agradável')
else: 
    print (f'Calor')

"""
Peça ao usuário que digite uma senha. Se a senha for "admin123", mostre "Acesso concedido"; senão, "Senha incorreta".
"""

senha = input ('Digite a senha: ')
if senha == 'admin123':
    print (f'Acesso concedido')
else:
    print (f'Senha incorreta')
