'''
Faça um código python que gere a tabela verdade de uma fórmula com 3 variáveis e informe a propriedade semântica (tautológica, satisfatória ou contraditória). Você deverá aprimorar o código de maneira que ele apresente as expressões “Verdadeiro” e “Falso” ao invés de True e False.
'''

from itertools import product

fórmula = input("Digite a fórmula com TRÊS variáveis (A, B e C): ")

print("\nTESTADOR TABAJARA:")
print("A\t\tB\t\tC\t\tFórmula")

total_linhas = 0
total_verdadeiro = 0
total_falso = 0

for valores in product([True, False], repeat=3):
    A, B, C = valores
    try:
        resultado = eval(fórmula)
    except Exception as e:
        print(f"Fórmula inválida.")
        exit()

    resultado_legivel = "Verdadeiro" if resultado else "Falso"

    print(f"{'Verdadeiro' if A else 'Falso'}\t"
          f"{'Verdadeiro' if B else 'Falso'}\t"
          f"{'Verdadeiro' if C else 'Falso'}\t"
          f"Fórmula={resultado_legivel}")

    total_linhas += 1
    if resultado:
        total_verdadeiro += 1
    else:
        total_falso += 1

print(f"\nTotal de linhas: {total_linhas}")
print(f"Total de linhas (falso)): {total_falso}")
print(f"Total de linhas (verdadeiro): {total_verdadeiro}")

if total_verdadeiro == total_linhas:
    print("Esta fórmula é TAUTOLOGIA")
elif total_falso == total_linhas:
    print("Esta fórmula é CONTRADIÇÃO")
else:
    print("Esta fórmula é SATISFATÓRIA")