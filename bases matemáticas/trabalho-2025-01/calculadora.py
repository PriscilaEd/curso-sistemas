from fractions import Fraction
# Desenvolva um programa em Python que apresente um menu interativo para o usuário, permitindo a realização de diversas operações matemáticas. O programa deverá solicitar ao usuário que escolha uma das opções disponíveis e, com base na escolha, realizar a operação correspondente.

print (f'Escolha qual das operações matemáticas você deseja realizar:')

print ("-"*30)

while True:
    print (f'1: SOMA DE NÚMEROS INTEIROS OU DECIMAIS')
    print (f'2: SUBTRAÇÃO DE NÚMEROS INTEIROS OU DECIMAIS')
    print (f'3: DIVISÃO DE NÚMEROS INTEIROS OU DECIMAIS')
    print (f'4: MULTIPLICAÇÃO DE DOIS NÚMEROS INTEIROS OU DECIMAIS')
    print (f'5: SOMA DE FRAÇÕES')
    print (f'6: SUBTRAÇÃO DE FRAÇÕES')
    print (f'7: MULTIPLICAÇÃO DE FRAÇÕES')
    print (f'8: DIVISÃO DE FRAÇÕES')
    print (f'9: CÁLCULO DE POTÊNCIA')
    print (f'10: CÁLCULO DE RAÍZ ')
    print (f'0: ENCERRAR O PROGRAMA')

    print ("-"*30)

    número = int (input ("Digite o número da operação desejada: "))

    print ("-"*30)


# SOMA NÚMEROS INTEIROS E DECIMAIS
    if número == 1:
        a = float (input ("Digite o primeiro valor da soma: "))
        b = float (input ("Digite o segundo valor da soma: "))

        soma = a + b
        print (f'O resultado de {a} + {b} é {soma}')
        print ("-"*30)

    
# SUBTRAÇÃO NÚMEROS INTEIROS E DECIMAIS
    elif número == 2:
        a = float (input ("Digite o primeiro valor da subtração: "))
        b = float (input ("Digite o segundo valor da subtração: "))
        
        subtração = a - b
        print (f'O resultado de {a} - {b} é {subtração}')
        print ("-"*30)


# DIVISÃO NÚMEROS INTEIROS E DECIMAIS
    elif número == 3:
        a = float (input ("Digite o primeiro valor da divisão: "))
        b = float (input ("Digite o segundo valor da divisão: "))

        divisão = a / b
        print (f'O resultado de {a} / {b} é {divisão}')
        print ("-"*30)


# MULTIPLICAÇÃO NÚMEROS INTEIROS E DECIMAIS
    elif número == 4:
        a = float (input ("Digite o primeiro valor da multiplicação: "))
        b = float (input ("Digite o segundo valor da multiplicação: "))

        multiplicação = a * b
        print (f'O resultado de {a} * {b} é {multiplicação}')
        print ("-"*30)


# SOMA DE FRAÇÕES
    elif número == 5:
        a = Fraction (input('Digite a primeira fração: '))
        b = Fraction (input('Digite a segunda fração: '))

        somaf = a + b
        print (f'O resultado de {a} + {b} é {somaf}')
        print ("-"*30)


# SUBTRAÇÃO DE FRAÇÕES
    elif número == 6:
        a = Fraction (input('Digite a primeira fração: '))
        b = Fraction (input('Digite a segunda fração: '))

        subtraçãof = a - b
        print (f'O resultado de {a} - {b} é {subtraçãof}')
        print ("-"*30)


# MULTIPLICAÇÃO DE FRAÇÕES
    elif número == 7:
        a = Fraction (input('Digite a primeira fração: '))
        b = Fraction (input('Digite a segunda fração: '))

        multiplicaçãof = a * b
        print (f'O resultado de {a} * {b} é {multiplicaçãof}')
        print ("-"*30)


# DIVISÃO DE FRAÇÕES
    elif número == 8:
        a = Fraction (input('Digite a primeira fração: '))
        b = Fraction (input('Digite a segunda fração: '))

        divisãof = a / b
        print (f'O resultado de {a} / {b} é {divisãof}')
        print ("-"*30)


# CÁLCULO DE POTÊNCIA
    elif número == 9:
        a = float (input (f'Digite a base da potência: '))
        b = float (input (f'Digite o expoente da potência: '))

        potência = a ** b 
        print (f'O resultado dessa potência é {potência}')
        print ("-"*30)


# CÁLCULO DE RAÍZ QUADRADA
    elif número == 10:
        print (f'1: RAÍZ QUADRADA')
        print (f'2: RAÍZ CÚBICA')
        print (f'3: AMBAS AS RAÍZES')
        print ("-"*30)
        opção = float (input (f' Digite o número da raíz desejada: '))
        print ("-"*30)

        if opção == 1:
            a = float (input (f'Digite o valor da raíz quadrada: '))
            raízQuadrada = a ** (1/2)
            print (f'A raíz quadrada de {a} é {raízQuadrada}')
        elif opção == 2:
            b = float (input (f'Digite o valor da raíz cúbica: '))
            raízCúbica = b ** (1/3)
            print (f'A raíz cúbica de {b} é {raízCúbica}') 
            print ("-"*30)
        elif opção == 3:
            c = float (input (f'Digite o valor da raíz: '))
            raízQuadrada = c ** (1/2)
            raízCúbica = c ** (1/3)
            print (f'A raíz quadrada de {c} é {raízQuadrada}')
            print (f'A raíz cúbica de {c} é {raízCúbica}')  
            print ("-"*30)
        else:
            print (f'Digite uma opção válida.')


# ENCERRAR O PROGRAMA
    elif número == 0:
        print (f'Fim do programa, espero que tenha sido útil!')
        print ("-"*30)
        break

    else: 
        print (f'Escolha uma operação válida')
    
    print ("-"*30)