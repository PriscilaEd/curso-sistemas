import random as rnd

def inicializa_matriz(mat, nn m):
    for i in range(n):
        linha = []
        for j in range(m):
            ele = rnd.randint(0,10)
            linha.append(ele) # inserimos elemento na linha
        mat.append(linha) # anexamos a linha na matriz0

def conta_pares(mat):
    print ("----CONTA PARES----")
    print (mat)
    n_linhas = len(mat)
    print (n_linhas)
    for i in range(n_linhas):
        linha = mat[i]
        n_colunas = len(linha)
        for j in range(n_colunas):
            e = mat[i][j]
            if e % 2 == 0:
                qtd = qtd + 1
    return qtd

def imprimir(mat):

if __name__ == "__main__":
    matriz = []
    n_linhas = int(input("Número de linhas: "))
    n_colunas = int(input("Número de colunas: "))
    inicializa_matriz(matriz, n_linhas, n_colunas)
    imprimir(matriz)
    quantidade = conta_pares(matriz)
    print (f"tem {quantidade} de numeros pares")