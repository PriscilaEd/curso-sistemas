def inversor(var_valor):
    print(f"---antes: {var_valor}")     # 10
    var_valor = var_valor * (-1)
    print(f"---depois: {var_valor}")  # -10

def inversor_lista(var_valores):
    """
    inverter todos os sinais da lista
    """
    for indice in range(len(var_valores)):
        var_valores[indice] *= (-1)

if __name__ == "__main__":
    numero = 10
    print(f"-antes: {numero}")        # 10
    inversor(numero)
    print(f"-depois: {numero}")         # 10
    print("-----------------")
    lista = [5,8,16,-10]
    print(f"l-antes: {lista}")
    inversor_lista(lista)
    print(f"l-depois: {lista}")