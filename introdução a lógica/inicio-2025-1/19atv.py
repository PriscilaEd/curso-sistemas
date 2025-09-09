import itertools

def avaliar_formula(formula, valores):
    contexto = dict(zip(['A', 'B', 'C', 'D'], valores))
    return eval(formula, {}, contexto)

def converter_bool(valor):
    return 'T' if valor else 'F'

def analisar_formula(formula):
    variaveis = ['A', 'B', 'C', 'D']
    combinacoes = list(itertools.product([True, False], repeat=4))
    resultados = []

    print(f"\nAnalisando a fórmula: {formula}")
    for combinacao in combinacoes:
        resultado = avaliar_formula(formula, combinacao)
        resultados.append(resultado)

        linha = ' '.join([f"{var}={converter_bool(val)}" for var, val in zip(variaveis, combinacao)])
        linha += f" Fórmula={converter_bool(resultado)}"
        print(linha)

    total = len(resultados)
    total_T = resultados.count(True)
    total_F = resultados.count(False)

    print(f"\nTotal de linhas: {total}")
    print(f"Total de linhas com resultado F: {total_F}")
    print(f"Total de linhas com resultado T: {total_T}")

    if total_T == total:
        tipo = "TAUTOLOGICA"
    elif total_F == total:
        tipo = "CONTRADITORIA"
    else:
        tipo = "SATISFATORIA"

    print(f"Análise da propriedade semântica da fórmula {formula}:")
    print(f"Esta fórmula é {tipo}")

    return resultados

formula1 = input("Digite a fórmula 1 (use A, B, C, D como variáveis): ")
resultados1 = analisar_formula(formula1)

formula2 = input("\nDigite a fórmula 2 (use A, B, C, D como variáveis): ")
resultados2 = analisar_formula(formula2)

print("\nFAZENDO ANÁLISE DE EQUIVALÊNCIA ENTRE AS FÓRMULAS:")
if resultados1 == resultados2:
    print("As fórmulas são equivalentes.")
else:
    print("As fórmulas não são equivalentes.")