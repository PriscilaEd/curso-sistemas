texto = "Lorem ipsum"

# encontra apenas a primeira ocorrencia
ind = texto.find ('a')
print (ind)
comprimento = len(texto) # total de caracteres 
ind = -10
while ind != -1:
    if ind != -10:
        ind = texto.find ('a', ind+1, comprimento)
    else:
        ind = texto.find ('a')

    print (f'indices {ind}')