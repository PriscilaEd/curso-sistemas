'''
M´edia de temperaturas semanais
Crie uma fun¸c˜ao que receba uma lista com 7 temperaturas e retorne a m´edia. Depois,
escreva fun¸c˜oes para retornar o maior e menor valor da lista. Crie uma fun¸c˜ao final
para exibir os resultados formatados.
'''

# parametro valores do tipo list (lista)
def media(valores: list):
    m = sum(valores) / len(valores)
    return round (m, 2)

def menor(valores):
    m = valores[0]
    for i in range(len(valores)):
        if valores[i] < m: 
            # atualia o m
            m = valores[i]
    return m    # min(valores)

def maior(valores):
    return max(valores)

def le_temperaturas():
    dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
    temp = []
    for dia in dias:
        t = float(input(f"Temperatura - {dia}: "))
        temp.append(t)
    return temp

'''
if __name__ == "__main__":
    x = media([10, 20])
    print (x)
    y = menor([7, 9, 5])
    print (y)
    '''

if __name__ == "__main__":
    temperaturas = le_temperaturas()
    med_temp = media(temperaturas)
    temp_min = menor(temperaturas)
    temp_max = maior(temperaturas)
    print("----------------------------")
    print(temperaturas)
    print(f"temperatura media: {med_temp}°C")
    print(f"temperatura minima: {temp_min}°C")
    print(f"temperatura maxima: {temp_max}°C")