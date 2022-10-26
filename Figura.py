class Figura:
    def __init__(self):
        self

    def areaTriangulo(self, base, altura):
        area = (base * altura) / 2
        print("El área del triángulo es: ", area)
        print("")

    def perimetroTriangulo(self, lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        print("El perímetro del triángulo es: ", perimetro)

    def areaCuadrado(lado1, lado2):
        pass

    def perimetroCuadrado(lado1, lado2, lado3, lado4):
        pass

    def areaRectangulo(longitud, ancho):
        pass

    def perimetroRectangulo(longitud, ancho):
        pass

    def areaCirculo(radio):
        pass

    def perimetroCirculo(radio):
        pass


if __name__ == "__main__":
    inicio = True
    while inicio:
        print("-------- Bienvenido a la calculadora de áreas y perímetro de alguans figuras --------")
        print("************ Seleccione una opción de las siguientes ************")
        print("1. Triángulo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("4. Circulo")
        print("5. Salir")
        opcion = int(input("Ingrese una acción de las anteriores: "))
        if opcion == 1:
            print("*********************************")
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            lado1 = float(input("Ingrese la medida del lado 1: "))
            lado2 = float(input("Ingrese la medida del lado 2: "))
            lado3 = float(input("Ingrese la medida del lado 3: "))
            print("*********************************")
            triangulo = Figura()
            triangulo.areaTriangulo(base, altura)
            triangulo.perimetroTriangulo(lado1, lado2, lado3)
            print("\n")
        elif opcion == 2:
            print("*********************************")
            print("Función para el cuadrado")
            print("*********************************")
            print("\n")
        elif opcion == 3:
            print("*********************************")
            print("Función para el rectangulo")
            print("*********************************")
            print("\n")
        elif opcion == 4:
            print("*********************************")
            print("Función para el circulo")
            print("*********************************")
            print("\n")
        elif opcion == 5:
            print("*********************************")
            print("Gracias, hasta la proxima")
            print("*********************************")
            print("\n")
            inicio = False
        else:
            print("********************************************")
            print("Favor de seleccionar un ana opción correcta")
            print("********************************************")
            print("\n")
