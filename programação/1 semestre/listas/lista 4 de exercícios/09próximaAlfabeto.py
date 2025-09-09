'''
9- Implemente um programa que substitua cada letra de uma string pela próxima no alfabeto (z deve se tornar a).
Entrada: texto = 'abcxyz'
Saída esperada: 'bcdyza'
'''

texto = input('Digite o texto: ')
resultado = ''

for letra in texto:
    if letra.isalpha():  
        if letra == 'z':
            resultado += 'a'
        elif letra == 'Z':
            resultado += 'A'
        else:
            resultado += chr(ord(letra) + 1)
    else:
        resultado += letra  

print(f'{resultado}')