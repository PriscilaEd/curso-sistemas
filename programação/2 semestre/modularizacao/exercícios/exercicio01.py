# criar uma função para calcular o fatorial

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        r = 1
        for i in range(1,numero+1):
            r = r*i
        return r

'''
Teste: 

if __name__ == "__main__":
    n = int(input("Digite um número: "))
    x = fatorial(n)
    print (f"{n}! = {x}")
'''

def combinacao(n, m):
    c = fatorial(n)/(fatorial(m) * fatorial(n-m))
    return c

if __name__ == "__main__":
    total = int(input("Total alunos: "))
    parte = int(input("Número de alunos no grupo: "))
    possibilidades = combinacao(total, parte)
    print (f"Temos {possibilidades} combinações.")