A = 'obabão'
B = "zezinho"

print (f'A = {A}, B = {B}')

C = A+B
print (f'C = {C}')

D = 12
E = 14.3
F = 20.1

print (f'D= {D}, E = {E}, F = {F}')

print (f'O tipo de dado A é {type(A)}')
print (f'O tipo de dado B é {type(B)}')
print (f'O tipo de dado C é {type(C)}')
print (f'O tipo de dado D é {type(D)}')
print (f'O tipo de dado E é {type(E)}')
print (f'O tipo de dado f é {type(F)}')

G = input (f'Digite algo para ser colocado na variável 6: ')
print (f'O valor digitado para G foi {G}. Este dado é do tipo {type (G)}')

G = int (G)
print (f'O valor de G é do tipo {type(G)}')

idade = int(input (f'Digite a idade: '))
print (f'A idade digitada foi {idade}. Esta informação é do tipo {type (idade)}')

preço = float(input(f'Digite o preço: '))
print (f'O preço do produto é {preço}. Esta informação é do tipo {type (preço)}')

numero = input('Digite o número: ')

print (f'É um número? {numero.isdigit ()}')

num1 = input ('Digite o valor do primeiro número: ')
num2 = input ('Digite o valor do segundo número: ')

if (num1.isdigit () and num2.isdigit () ):
    print ('Ótimo, você digitou números inteiros')
else:
    print ('Que pena, deu ruim...')

