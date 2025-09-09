n_linhas = 3      # poderia vir pelo input
n_colunas = 5
matriz = []

# inicializar matriz com zeros
for i in range (n_linhas):
    linha = [0]*n_colunas
    matriz.append(linha)

# imprimir 
print (matriz)
print ("--------------------")
for linha in range(n_linhas):
    print (matriz[0])