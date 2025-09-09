PI = 3.14

def area_circulo(raio):
    return PI*(raio**2)

def area_retangulo(lado1, lado2):
    return lado1*lado2

def area_triangulo(lado1, lado2, lado3):
    s_p = perimetro_triangulo(lado1, lado2, lado3)/2
    fator = s_p*(s_p-lado1)*(s_p-lado2)*(s_p-lado3)
    return fator**0.5

def perimetro_circulo(raio):
    return 2*PI*raio

def perimetro_retangulo(lado1, lado2):
    return 2*lado1+2*lado2

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1+lado2+lado3