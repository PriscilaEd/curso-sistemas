notas = []
qtd = 40
nomes = []

print (f'---lancar notas---')
for indice in range (qtd):
    nom = input ('digite nome: ')
    valor = float (input ('digite nota: '))
    nomes.append (nom)
    notas.append (valor)

##fora do for 
media= sum(notas)/len(notas)
for i in range (len(notas)):
    print (f'{i}- {nom[i]}: {notas[i]}')
    if notas [i] > media:
        print (f'Parabens {nomes[i]}')