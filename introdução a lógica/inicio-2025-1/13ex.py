
'''
totalLinhas = 0
possibilidades = [True, False]

for x in possibilidades:
    for y in possibilidades:
        if (x and y) or x: #fórmula a ser testada
            resultadoFormula = True 
        else:
            resultadoFormula = False
        print (f'X = {x} Y = {y} Fórmula = {resultadoFormula}')
        totalLinhas += 1

print (f'Total de linhas: {totalLinhas}')
'''

'''
totalLinhas = 0
possibilidades = [True, False]

for x in possibilidades:
    for y in possibilidades:
        if (x or y) and (x and not y): #fórmula a ser testada
            resultadoFormula = True 
        else:
            resultadoFormula = False
        print (f'X = {x} \t Y = {y} \t Fórmula = {resultadoFormula}')
        totalLinhas += 1

print (f'Total de linhas: {totalLinhas}')
'''
'''
totalLinhas = 0
possibilidades = [True, False]

for x in possibilidades:
    for y in possibilidades:
        if not (x or not y) and (not x and y):
            resultadoFormula = True 
        else:
            resultadoFormula = False
        print (f'X = {x} \t Y = {y} \t Fórmula = {resultadoFormula}')
        totalLinhas += 1

print (f'Total de linhas: {totalLinhas}')



totalLinhas = 0
possibilidades = [True, False]

for a in possibilidades:
    for b in possibilidades:
        if not (a or b) == (not a and b):
            resultadoFormula = True 
        else:
            resultadoFormula = False
        print (f'X = {x} \t Y = {y} \t Fórmula = {resultadoFormula}')
        totalLinhas += 1

print (f'Total de linhas: {totalLinhas}')



totalLinhas = 0
possibilidades = [True, False]

for a in possibilidades:
    for b in possibilidades:
        if (a and not (b==a)) == ((not a) == (not b)):
            resultadoFormula = True 
        else:
            resultadoFormula = False
        print (f'X = {x} \t Y = {y} \t Fórmula = {resultadoFormula}')
        totalLinhas += 1

print (f'Total de linhas: {totalLinhas}')

'''

'''
totalLinhas = 0
possibilidades = [True, False]

for p in possibilidades:
    for q in possibilidades:
        for r in possibilidades:
            for s in possibilidades: 
                if (p and q) == (not (r or s)):
                 resultadoFormula = True 
                else:
                 resultadoFormula = False
                print (f'P = {p} \t Q = {q} \t R = {r} \t S = {s} \t Fórmula = {resultadoFormula}')
                totalLinhas += 1
print (f'Total de linhas: {totalLinhas}')
'''
'''
totalLinhas = 0
possibilidades = {True, False}

qualFormula = input ('Digite a fórmula (utilize nomenclatura "a" e "b"): ')
for a in possibilidades:
    for b in possibilidades: 
        if eval (qualFormula):
            resultadoFormula= True
        else:
            resultadoFormula = False
            (f'A = {a} \t B = {b} \t Fórmula = {resultadoFormula}')
            totalLinhas += 1
print (f'Total de linhas: {totalLinhas}')
'''
'''
totalLinhas = 0
possibilidades = {True, False}

qualFormula = input ('Digite a fórmula (utilize nomenclatura "a", "b", "c", "d" e "e"): ')
for a in possibilidades:
    for b in possibilidades: 
        for c in possibilidades:
            for d in possibilidades:
              for e in possibilidades:
                    if eval (qualFormula):
                        resultadoFormula= True
                    else:
                        resultadoFormula = False
                        print (f'A = {a} \t B = {b} \t Fórmula C = {c} \t D = {d} \t E = {e} \t = {resultadoFormula}')
                        totalLinhas += 1
print (f'Total de linhas: {totalLinhas}')
'''

totalLinhas = 0
totalVerdadeiro = 0
totalFalso = 0
possibilidades = {True, False}

qualFormula = input ('Digite a fórmula (utilize nomenclatura "a", "b", "c"): ')
for a in possibilidades:
    for b in possibilidades: 
        for c in possibilidades:
            if eval (qualFormula):
                resultadoFormula=True
                totalVerdadeiro+=1
            else:
                resultadoFormula=False
                totalFalso+=1
            print (f'A={a} \t B= {b} \t C={c} \t Fórmula = {resultadoFormula}')
            totalLinhas+=1
print (f'Total de linhas: {totalLinhas}')
print (f'Total de linhas com resultado FALSO: {totalFalso}')
print (f'Total de linhas com resultado VERDADEIRO: {totalVerdadeiro}')