def maior(valor_a, valor_b):
    '''
    valor_a: primeiro numero
    valor_b: segundo numero
    '''
    if valor_a > valor_b:
        valor_maior = valor_a
    else:
        valor_maior = valor_b
    return valor_maior
    '''return max'''

num_a = int(input('Digite primeiro valor: '))
num_b = int(input("Digite segundo valor: "))
num_maior = maior(num_a, num_b)
print(f"Maior valor {num_a} ou {num_b}? >>>>> {num_maior}")

maior_todos = maior(80,num_maior)
print(f"Maior de todos {maior_todos}")