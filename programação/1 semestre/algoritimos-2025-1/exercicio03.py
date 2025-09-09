# Escreva um algoritmo em pseudocódigo para:
# Calcular o peso ideal de uma pessoa, assumindo (Homem: Peso = 72,7* Altura - 58); (Mulher: Peso = 62,1 * Altura - 44,7)
# float = número real

altura = float (input (f'Digite a altura: '))

homem = (72.7*altura)-58
mulher = (62.1*altura)-44.7

print (f'H: {homem: .2f} kg')
print (f'M: {mulher: .2f} kg')