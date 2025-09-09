'''
11- Crie um programa que leia 11 dígitos numéricos e exiba o valor formatado como um CPF (xxx.xxx.xxx-xx).
Entrada: cpf = '12345678900'
Saída esperada: '123.456.789-00'
'''

cpf = input("Digite os 11 dígitos do CPF: ")

if len(cpf) == 11 and cpf.isdigit():
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    print(cpf_formatado)
else:
    print("Entrada inválida! Certifique-se de digitar exatamente 11 números.")