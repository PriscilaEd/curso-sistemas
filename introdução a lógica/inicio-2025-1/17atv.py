'''
Faça um código python que gere a tabela verdade de uma fórmula com 2 ou 3 variáveis e informe a propriedade semântica (tautológica, satisfatória ou contraditória). Antes de iniciar, o sistema deve perguntar ao usuário quantas variáveis haverá na fórmula. Também deverá ser solicitado na inicialização o nome do aluno para que ele seja exibido ao final da análise.
'''
from itertools import product

aluno = input ('Digite seu nome: ')
qntd = int (input ('Digite 2 caso duas variáveis, e 3 caso três variáveis: '))

if qntd == 2:
    variaveis = ['A', 'B']

elif qntd == 3:
    variaveis = ['A', 'B', 'C']

else:
    print (f'Resposta inválida.')
    exit ()

formula = input ('Digite a fórmula com as variáveis A e B, ou A, B e C: ')

valores = list(product([False, True], repeat=len(variaveis)))

print("\nTabela Verdade:")
print(" | ".join(variaveis) + " | Resultado")
print("-" * (len(variaveis) * 6 + 13))

resultados = []

for linha in valores:
    contexto = dict(zip(variaveis, linha))
    try:
        resultado = eval(formula, {}, contexto)
    except Exception as e:
        print(f"Erro ao avaliar a fórmula: {e}")
        exit()
    resultados.append(resultado)
    valores_str = " | ".join(str(v) for v in linha)
    print(f"{valores_str} | {resultado}")

if all(resultados):
    tipo = "Tautológica"
elif any(resultados):
    tipo = "Satisfatória"
else:
    tipo = "Contraditória"

print(f"\nFórmula: {formula}")
print(f"Propriedade semântica: {tipo}")
print(f"Análise realizada por: {aluno}")