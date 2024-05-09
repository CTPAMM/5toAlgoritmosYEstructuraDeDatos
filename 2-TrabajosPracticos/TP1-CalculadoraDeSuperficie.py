"""
#Curso: 5° 2°
#Estudiante: Noelia Escobar
#Fecha: 29/04 
"""
##Definir funciones

def SuperfiecieCuadrado(lado):
    SuperCuadrado = lado ** 2
    print(f"La superfiecie del cuadrado de lado {lado} es: {SuperCuadrado}")
    print("             ")


def SuperficieRectalngulo(base, altura):
    SuperRectangulo = base * altura
    print(f"La superficie del rectangulo de base {base} y altura {altura} es: {SuperRectangulo}")
    print("             ")


def SuperficieTriangulo (base, altura):  
    SuperTriangulo = base * altura / 2
    print(f"La superficie del triangulo de base {base} y altura {altura} es: {SuperTriangulo}")
    print("             ")

def SuperficieCirculo (radio):
    SuperficieCirculo = 3.14 * radio**2
    print(f"La superficie del circulo es: {SuperficieCirculo} ")
    print("             ")


while True:

    print("             Menu Calculador de superficies               ")
   
    print("1-Superficie de cuadrado")
    print("2-Superficie de rectangulo")
    print("3-Superficie de triangulo")
    print("4-Superficie de circulo")
    print("                         ")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        lado = int(input ("Ingrese el lado del cuadrado: "))
        SuperfiecieCuadrado(lado)
        print("             ")


    elif opcion ==2:
        base = int(input ("Ingrese la base del rectangulo: "))
        altura = int(input ("Ingrese la altura del rectangulo: "))
        SuperficieRectalngulo(base, altura)
        print("             ")


    elif opcion ==3:
        base = int(input ("Ingrese la base del triangulo: "))
        altura = int(input ("Ingrese la altura del triangulo: "))

        SuperficieTriangulo(base, altura)/2
        print("             ")

    elif opcion ==4:
        radio = int(input("Ingrese el radio del circulo: "))
        SuperficieCirculo (radio)
        print("             ")

    else:
        print ("                  ")
        print("Opcion incorrecta!")
        print("             ")