# Escreva um algoritmo em pseudocódigo para:
# Calcular a média de um aluno numa disiplina, sendo Média = (Provas + 4 x Prova1 + 3 x Prova2)

print ("="*30)
prova_1 = int(input (f'Digite a nota da primeira prova: '))
prova_2 = int(input (f'Digite a nota da segunda prova: '))
trabalho = int(input (f'Digite a nota do trabalho: '))
participação = int(input (f'Digite a nota da participação: '))
print ("="*30)

provas = 3*prova_1+3*prova_2
média = (provas+3*trabalho+participação)/10
print (f'A média foi de {média}')