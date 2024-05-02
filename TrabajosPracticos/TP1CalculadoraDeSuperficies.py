"""
Curso: 5°2°
Estudiante: Pablo
Fecha: 29/04
"""

# Calculadora de superficies

# Definir funciones

def superficieCuadrado(lado):
    superfCuadrado = lado ** 2
    print(f"La superficie del cuadrado de lado {lado} es: {superfCuadrado}")
    
def superficieRectangulo(base, altura):
    superfRectangulo = base * altura
    print(f"La superficie del rectángulo de base {base} y altura {altura} es: {superfRectangulo}")
    
def superficieTriangulo(base, altura):        
    superfTriangulo = (base * altura)/2
    print(f"La superficie del triángulo de base {base} y altura {altura} es: {superfTriangulo}")
    
# Comienza el bucle while

while True:
    #Paso 1:Menú de la computadora
    print("***MENÚ CALCULADORA DE SUPERFICIES****")
    print("1- CUADRADO")
    print("2- RECTÁNGULO")
    print("3- TRIÁNGULO")
    print("0- SALIR")
    
    #Paso 2:Pedir al usuario que ingrese una opción
    opcion = int(input("ingrese una opcion: "))
    
    #Paso 3: Hacer que la computadora decida
    if opcion == 1:
        lado = int(input("Ingrese el lado del cuadrado: "))
        superficieCuadrado(lado)
        
    elif opcion == 2:
        base = int(input("Ingrese la base del rectángulo: "))
        altura = int(input("Ingrese la altura del rectángulo: "))
        superficieRectangulo(base, altura)
        
    elif opcion == 3:
        base = int(input("Ingrese la base del triángulo: "))
        altura = int(input("Ingrese la altura del triángulo: "))
        superficieTriangulo(base, altura)
        
    elif opcion == 0:
        print("Gracias por utilizar nuestra app!")
        break
            
    else:
        print("¡Opción incorrecta. Vuelva a intentarlo!")    
