# CRIE UM FOR QUE EXIBA OS IGREDIENTES DE UM SANDUICHE 
 
for ingredientes in 'duas fatias de pão', 'hambúrguer', 'alface', 'tomate', 'queijo', 'milho', 'catupiry':
    print (f'Os igredientes desse sanduíche são: {ingredientes}')

INGREDIENTES = ['pão', 'hambúrguer', 'alface', 'tomate', 'queijo', 'milho', 'catupiry']
contador = 1
for INGREDIENTE in INGREDIENTES:
    print (f'Ingrediente {contador}: {INGREDIENTE}')
    contador+=1

x = 0
while x < 10:
    x = float (input ('Digite um valor para X: '))


senha = '123456'
m = ''
while m != senha:
    m=input ('Digite a senha: ')