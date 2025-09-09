'''
13- Crie um programa que leia um nome completo e destaque o último sobrenome em letras maiúsculas, seguido do restante do nome.
Entrada: nome = 'Carlos Alberto Pereira'
Saída esperada: 'PEREIRA, Carlos Alberto'
'''

nome = input('Digite seu nome completo: ')
partes = nome.strip().split()
if len(partes) >= 2:
    ultimo_sobrenome = partes[-1].upper()
    restante_nome = ' '.join(partes[:-1])
    nome_formatado = f"{ultimo_sobrenome}, {restante_nome}"
    print(nome_formatado)
else:
    print("Digite pelo menos nome e sobrenome.")