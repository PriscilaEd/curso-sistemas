# FAÇA UM CÓDIGO QUE RECEBA DOIS NÚMEROS. EM SEGUIDA, FAÇA O TESTE SE OS DOIS SÃO NÚMEROS PARES OU SE A SOMA DOS DOIS NÚMEROS É MAIOR QUE 10

n1 = int (input ('Digite o primeiro número: '))
n2 = int (input ('Digite o segundo número: '))

if n1 % 2 == 0 and n2 % 2 == 0 or (n1 + n2 > 10):
    print ('Condição satisfeita')
else:
    print ('Condição não atendida... foi mal')