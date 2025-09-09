x = list ('SUBINOONIBUS')
print (x)
x.reverse ()
print (x)

print (f'Vamos criar uma lista A')
A = []

print (f'Conteúdo da lista A: {A}')
A.append (12)
print (f'Conteúdo da lista A: {A}')
A.append ('obabão')
print (f'Conteúdo da lista A: {A}')
A.append ('19')
print (f'Conteúdo da lista A: {A}')
A.append ('-5')
print (f'Conteúdo da lista A: {A}')

A.insert (0, 'teste')
print (f'Conteúdo da lista A: {A}')

del A [2]
print (f'Conteúdo da lista A: {A}')

A.remove (1)
print (f'Conteúdo da lista A: {A}')

print (f'Conteúdo da lista A: {A}')
tirar=input ('Digite o nome do elemento para remover: ')
A.remove (tirar)
print (f'Conteúdo da lista A: {A}')

B = ['hello', 'abacate', 'oi']
B.sort ()
print (f'Conteúdo da lista A: {B}')

C = [5, 8, 140, 1, 0]
C.sort ()
print (f'Conteúdo da lista A: {C}')
