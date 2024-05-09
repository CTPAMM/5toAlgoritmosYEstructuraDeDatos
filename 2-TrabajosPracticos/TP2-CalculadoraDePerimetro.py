'''
#Curso: 5° 2°
#Estudiante: Noelia Escobar
#Fecha: 07/05
'''
#Calculadora de Perimetro

def PerimetroCuadrado(lado):
    PeriCuadrado = lado * 4
    print(f"El perimetro del cuadrado de lado {lado} es: {PeriCuadrado}")
    print("             ")

def PerimetroRectalngulo(base, altura):
    PeriRectangulo = base *2 + altura *2
    print(f"El perimetro del rectangulo de base {base} y altura {altura} es: {PeriRectangulo}")
    print("             ")

def PerimetroTriangulo (lado):  
    PeriTriangulo = lado *3
    print(f"El perimetro del triangulo de sus lados es: {PeriTriangulo}")
    print("             ")

def PerimetroCirculo (radio):
    PeriCirculo = 3.14 * radio*2
    print(f"El perimetro del circulo es: {PeriCirculo} ")
    print("             ")

#Menu

while True:

    print("             Menu Calculadora de Perimetro               ")
    
    print("1-Perimetro de cuadrado")
    print("2-Perimetro de rectangulo")
    print("3-Perimetro de triangulo")
    print("4-Perimetro de circulo")
    print("             ")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
            lado = int(input ("Ingrese el lado del cuadrado: "))
            PerimetroCuadrado(lado)
            print("             ")

    elif opcion ==2:
            base = int(input ("Ingrese la base del rectangulo: "))
            altura = int(input ("Ingrese la altura del rectangulo: "))
            PerimetroRectalngulo(base, altura)
            print("             ")


    elif opcion ==3:
            lado = int(input ("Ingrese el lado del triangulo: "))

            PerimetroTriangulo(lado)
            print("             ")

    elif opcion ==4:
            radio = int(input("Ingrese el radio del circulo: "))
            PerimetroCirculo(radio)
            print("             ")
    else:
        print ("                  ")
        print("Opcion incorrecta!")
        print("             ")