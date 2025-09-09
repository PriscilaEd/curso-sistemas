'''
Implemente o código e comente o que acontece em cada linha. Código de implementação do Triângulo de Pascal
+++++ SEM USAR A FÓRMULA DOS COEFICIENTES BINOMINAIS 

      1
    1   1
  1   x   1
1  x   x   1

'''

def gerar_triangulo(n): # gera o triângulo até a linha n, começando com 'None'; assim não tem que fazer ele todo manualmente!!!
    triangulo = [[1]] # a primeira linha vai sempre ser 1
    for i in range(1, n+1): # código pra colocar os None no meio
        linha = [1]+[None]*(i-1)+[1]
        triangulo.append(linha)
        # aplicando a regra de Pascal!!!
    for i in range(2, n+1): # a partir da segunda linha
        for j in range (1,i): # pra substituir os do meio
            if triangulo[i][j] is None:
                triangulo[i][j] = triangulo[i-1][j-1]+ triangulo[i-1][j] # o cálculo da regra, sem usar a fórmula
   
    return triangulo

print ("-"*30)

# agora solicitar para o usuário informar os valores dos coeficientes
n = int(input("Digite o valor de cima: "))
k = int(input("Digite o valor de baixo: "))

print ("="*30)

# gerar o triângulo até n 
triangulo = gerar_triangulo(n)

for linha in triangulo:
    print(linha)

print ("="*30)
print(f"O valor de ({n} sobre {k}) é: {triangulo[n][k]}")
print ("-"*30)