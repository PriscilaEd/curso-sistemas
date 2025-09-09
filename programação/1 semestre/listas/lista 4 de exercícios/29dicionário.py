'''
29- Desenvolva um programa que leia uma frase e exiba um dicionário com a frequência de cada palavra encontrada.
Entrada: frase = 'olá mundo olá'
Saída esperada: {'olá': 2, 'mundo': 1}
'''

frase = input("Digite uma frase: ")
palavras = frase.lower().split()
frequencia = {}
for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
print(frequencia)