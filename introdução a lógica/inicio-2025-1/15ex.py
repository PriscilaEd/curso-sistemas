totais_linhas = []
possibilidades = {True, False}
tabelas = []
totais_verdadeiros = []
totais_falsos = []


for i in 1, 2:
    tabelas = []
    totalLinhas = 0 
    totalVerdadeiro = 0
    totalFalso = 0 

Fórmula = input ('Digite a fórmula {i} (use a, b, c como variáveis): ')
for a in possibilidades:
     for b in possibilidades:
           for c in possibilidades:
                if eval (Fórmula):
                    resultadoFórmula = True 
                    totalVerdadeiro += 1
                else:
                    resultadoFórmula = False 
                    totalFalso += 1

                    tabelas.append (resultadoFórmula)
                print (f'A = {a} \t B = {b} \t C = {c} \t Fórmula - resultadoFórmula')
                totalLinhas += 1

tabelas.append (tabelas)
totais_linhas.append (totalLinhas)
totais_verdadeiros.append (totalVerdadeiro)
totais_falsos.append (totalFalso)

print (f'Total de linhas: {totalLinhas}')
print (f'Total de linhas com resultado FALSO: {totalFalso}')
print (f'Total de linhas com resultado VERDADEIRO: {totalVerdadeiro}')

print (f'Análise de propriedade semântica da fórmula {Fórmula}: ')
if totalVerdadeiro == totalLinhas:
     Fórmula = 'TAUTOLOGICA'
elif totalFalso == totalLinhas:
     Fórmula = 'CONTRADITORIA'
else:
     Fórmula = 'SATISFATORIA'
print (f'Esta fórmula é {Fórmula}')
print ()

print ('FAZENDO ANÁLISE DE EQUIVALÊNCIA ENTRE AS FÓRMULAS:')
if tabelas[0] == tabelas[1]:
     print ('As fórmulas são equivalentes.')
else:
     print ('As fórmulas não são equivalentes.')




