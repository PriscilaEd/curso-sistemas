def altera_valor(idade):
    print(f"inicio da função: {idade}")
    idade = idade*10
    print(f"termino da função: {idade}")

idade = 5
print(f"fora da função (antes): {idade}")
altera_valor(idade)
print(f"fora da função (depois): {idade}")
