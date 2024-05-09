# Elige tu propia operación Versión 2

# Definir funciones

def multiplicar(a, b):
    multiplicación = a + b
    return multiplicación


# Inicio el bucle while
while True:
    # PASO 1: Menú de la calculadora

    print("***********MENÚ*************")
    print("1- Multiplicación")
    print("2- División")
    print("3- Suma")
    print("4- Resta")

# PASO 2: Pedir al usuario ingrese una opción.

    opcion = int(input("Ingrese su opción: "))

    # PASO 3: Hacer que la computadora decida.
    
    if opcion == 1:
        
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese e segundo número: "))
        
        multiplicacion = multiplicar(num1, num2) # llamada a la función multiplicar
        
        print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
        
    elif opcion == 2:
        
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese e segundo número: "))
        
        division = dividir(num1, num2) # llamada a la función multiplicar
        
        print(f"La división de {num1} y {num2} es: {division}")
        
    ...
    
    else:
        print("¡Opción incorrecta!")    