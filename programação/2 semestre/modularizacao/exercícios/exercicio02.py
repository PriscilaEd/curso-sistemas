'''Teste'''

def status(nota):
    if nota >= 6:
        return "Aprovado"
    elif nota >= 4: # and nota < 6, não precisa verificar esse
        return "Verificação suplementar"
    else: 
        return "Reprovado"

if __name__ == "__main__":
    valor_nota = float(input("Nota: "))
    resultado = status(valor_nota)
    print (f"Situação = {resultado}")