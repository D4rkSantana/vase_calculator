# calculo retangulo (base, altura)
#   A = base * altura
#
# calculo poligono regular (lado, numero de lados)
#   A = semi_perimetro * apotema
#       semi_perimetro = (numero de lados * tamanho do lado) / 2
#       apotema = tamanho do lado / (2 * tangente de Thetha)
#           Theta = 360° / (2 * numero de lados)
#
#   calculo losangulo (diametro maior, diametro menor)
#       A = (diametro maior * diametro menor) / 2
#
# calculo triangulo
#   #triangulo equilatero(lado)
#       A = ((lado * lado ) * 1,73205) / 4
#   #triangulo escaleno(lado 1, lado 2, lado 3)
#       A = ((p * (p - lado1) * (p - lado2 ) * (p - lado3))) ** 0.5
#           p = (lado1 + lado2 + lado3) / 2 "semi perimetro"
#   #triangulo isosciles (base, lado)
#       A = (base * altura) / 2
#           altura = ((base ** 2) - (lado ** 2)) ** 0.5
#   #triangulo retangulo(lado menor, lado medio)
#       A = (base * altura) / 2
#
# calculo circulo (raio)
#   A = Pi * (raio * raio)
#
# calculo semi circulo (raio)
#   A = (pi * (raio * raio)) / 2
#

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return ((lado1 * lado1) * 1,73205) / 4
    else

def area_triangulo_equilatero(lado):
    return ((lado * lado) * 1,73205) / 4

def area_triangulo_isosceles(base, lado):
    h = ((lado ** 2) - ((base / 2) ** 2)) ** 0.5

    return (base * h) / 2

def area_triangulo_retangulo(cateto_maior, cateto_menor):
    pass