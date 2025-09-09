'''
 5. Validador de CPF (Simplificado)
 Crie uma fun¸c˜ao que verifique se um CPF est´a no formato xxx.xxx.xxx-yy. Use
 outra fun¸c˜ao para ler v´arios CPFs e verificar todos.
 '''

def verifica_separadores(doc):
    resultado = doc[3]=='.' and doc[7] =="." and doc[11]=="-"
    return resultado

def eh_digito(caracter):
    return caracter.isdigit

def le_cpf():
    cpf = input ("Digite o cpf no formato correto (###.###.##-##): ")
    cpf_digitos = cpf[0:3]+cpf[4:7]+cpf[8:11]+cpf[12:]
    print (cpf_digitos)
    if verifica_separadores(cpf) and eh_digito(cpf_digitos):
        print (f"respeita a regra: {cpf}")
    else:
        print(f"não respeita a regra: {cpf}")

if __name__ == "__main__":
   op = "sim"
   while op == "sim":
        le_cpf()
        op = input("deseja continuar? sim ou não?")
