'''
Crie um código que peça ao usuário para digitar 2 valores, n e k
O código deve resolver o coeficiente binominal de n e k
Afim de ganhar tempo de processamento, faça uma verificação em cima das 3 regras dos coeficientes binominais antes do código chegar na operação matemática.
'''
import math

n = int (input('Digite o valor de n: '))
k = int (input('Digite o valor de k: '))

if n == k or k == 0:
    print (f'O coeficiente binominal é 1.')

elif k == 1:
    print (f'O coeficiente binominal é {n}.')

else:
    resultado = math.factorial(n) // (math.factorial(k)*(math.factorial(n-k)))
    print (f'O coeficiente binominal é {resultado}.')