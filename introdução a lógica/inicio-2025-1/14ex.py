# PERGUNTAR 2 OU 3 VARIÁVEIS
# PEDIR A FÓRMULA

totalLinhas = 0 
totalVerdadeiro = 0
totalFalso = 0 
possibilidades = {True, False}

variável = int (input ('Insira se serão uma ou duas variáveis: '))

if variável == 2:
    fórmula = int (input (f'Digite a fórmula (utilize a, b, c): '))
    for a in possibilidades:
        for b in possibilidades:
            for c in possibilidades:
                if eval (fórmula):
                    resultadoFórmula = True 
                    totalVerdadeiro += 1
                else:
                    resultadoFórmula = False 
                    totalFalso += 1
                print (f'A = {a} \t B = {b} \t C = {c} \t Fórmula - resultadoFórmula')
                totalLinhas += 1
    print (f'Total de linhas: {totalLinhas}')
print (f'Total de linhas: {totalLinhas: }')
print (f'Total de linhas com resultado FALSO: {totalFalso}')
print (f'Total de linhas com resultado VERDADEIRO: {totalVerdadeiro}')



