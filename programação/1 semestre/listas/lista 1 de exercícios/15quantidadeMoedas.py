
valor = int(input("Informe o valor em centavos: "))

print ('-'*30) 

moedas1 = valor // 100
valor = valor % 100
moedas50 = valor // 50
valor = valor % 50
moedas25 = valor // 25
valor = valor % 25
moedas10 = valor // 10
valor = valor % 10
moedas5 = valor // 5
valor = valor % 5
moedas01 = valor

print("\nMenor quantidade de moedas:")
if moedas1 > 0:
    print(f"{moedas1} moeda(s) de 1 real")
if moedas50 > 0:
    print(f"{moedas50} moeda(s) de 50 centavos")
if moedas25 > 0:
    print(f"{moedas25} moeda(s) de 25 centavos")
if moedas10 > 0:
    print(f"{moedas10} moeda(s) de 10 centavos")
if moedas5 > 0:
    print(f"{moedas5} moeda(s) de 5 centavos")
if moedas01 > 0:
    print(f"{moedas01} moeda(s) de 1 centavo")
