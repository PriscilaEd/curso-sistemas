'''
12- Implemente um programa que substitua palavras proibidas em uma frase por '***'. As palavras proibidas devem ser fornecidas em uma lista.
Entrada: texto = 'Isso é feio e chato' proibidas = ['feio', 'chato']
Saída esperada: 'Isso é *** e ***'
'''

texto = input('Digite uma frase: ')
proibidas = ['feio', 'chato']
palavras = texto.split()
resultado = []

for palavra in palavras:
    limpa = palavra.strip('.,!?;:')
    if limpa.lower() in proibidas:
        resultado.append('***')
    else:
        resultado.append(palavra)

frase_filtrada = ' '.join(resultado)
print("Frase filtrada:", frase_filtrada)