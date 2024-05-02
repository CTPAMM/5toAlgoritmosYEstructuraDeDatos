#Calculadora de multiplicaciones y divisiones

while True:
    print("**********Menú de opciones********")
    print("1-Multiplicacion")
    print("2-Division")
    print("3-Sumar")
    print("4-Resta")
    print("5-Potenciación")
    print("6-Radicación (Raíz cuadrada)")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        multiplicacion = numero1 * numero2
        
        print("             ")
        print(f"La multiplicacion de {numero1} y {numero2} es: {multiplicacion}")
        print("             ")

    elif opcion == 2:
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        division = numero1 / numero2
        
        print("             ")
        print(f"La division de {numero1} y {numero2} es: {division}")
        print("             ")
        
    elif opcion == 3:
        numero1 = int(input("INgrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        sumar =numero1 + numero2 
        
        print("             ")
        print(f"La suma de {numero1} y {numero2} es: {sumar}")
        print("             ")
    
    elif opcion == 4:
        numero1 = int(input("INgrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        
        restar = numero1 ** numero2 
        
        print("             ")
        print(f"La resta de {numero1} y {numero2} es: {restar}")
        print("             ")


    elif opcion == 6:
        numero1 = int(input("Ingrese el primer numero: "))
        
        radicacion = numero1 ** 0.5 
        
        print("             ")
        print(f"La raíz cuadrada de {numero1} es: {radicacion}")
        print("             ")

    
    else:
        print("Opcione incorrecta!")
        print("             ")