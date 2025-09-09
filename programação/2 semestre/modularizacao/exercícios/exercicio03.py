def visor(valor):
    print("-"*10)
    print(valor)
    print("-"*10)

def menu():
    print ("Opções:")
    print ("(1) Somar")
    print ("(2) Subtrair")
    print ("(3) Multiplicar")
    print ("(4) Dividir")
    print ("(5) Limpar memória")
    print ("(6) Sair do programa")
    print ("Qual opção você deseja?")
    opcao = input('>>> ')
    return opcao

def soma(a, b):
    '''
    r = a + b
    reutrn = r
    '''
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    if b != 0:
        return a/b
    else: 
        print("Alerta!!! Divisão por 0 não é permitido")
        return a # manter valor da memória sem quebrar o programa

def limpar_tela():
    import os 
    os.system("cls") #windows
    #linux: os.system("clear")

if __name__ == "__main__":
    memoria = 0
    op = "0"
    while op != "6":
        limpar_tela()
        visor(memoria)
        op = menu()
        if op == "6":
            print("encerrando")
        elif op in ["1", "2", "3", "4"]:
            numero = float(input("digite valor: "))
            if op == "1":
                memoria = soma(memoria, numero)
                print ('memoria')
            if op == "2":
                memoria = subtracao(memoria, numero)
            if op == "3":
                memoria = multiplicacao(memoria, numero)
            if op == "4":
                memoria = divisao(memoria, numero)
        elif op == "5":
            memoria = 0
        else:
            print("opção incorreta")