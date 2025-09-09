# Faça um código que receba 3 valores inteiros e armazene nas seguintes variáveis: A, B e C. Em seguida, faça um teste condicional usando if para mostrar as seguintes respostas: se atendido (verdadeiro), o resultado é "OK", caso contrário será "NEGATIVO"
# A condição para verdadeiro será: A ou B receber 0, ou, C e A receber valor diferente de 7

A = int (input ('Digite o valor de A: '))
B = int (input ('Digite o valor de B: '))
C = int (input ('Digite o valor de C: '))
if (A == 0 or B == 0) or (C != 7 and A != 7):
    print ('Ok!!!')
else:
    print ('NEGATIVO!')

