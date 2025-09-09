'''
28- Crie um programa que verifique se uma lista B é sublista da lista A, ou seja, se todos os elementos de B aparecem em A.
Entrada: a = [1, 2, 3, 4] b = [2, 3]
Saída esperada: 'Sim'
'''
'''
Em sala
a = [1, 2, 3, 4]
b = [2,3, 0]
todos_presentes = False 
for elemento in b:
    if elemento not in a:
        todos_presentes = False
if todos_presentes:
    print ('Sim')
else: 
    print ('Não')
    '''

a = input("Digite a lista A (valores separados por vírgula): ")
b = input("Digite a lista B (valores separados por vírgula): ")
lista_a = [int(x.strip()) for x in a.split(',')]
lista_b = [int(x.strip()) for x in b.split(',')]

encontrado = False
for i in range(len(lista_a) - len(lista_b) + 1):
    if lista_a[i:i+len(lista_b)] == lista_b:
        encontrado = True
        break

print("Sim" if encontrado else "Não")