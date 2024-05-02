# Crear una suma de 2 números sin función
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2

print(f"La suma de {num1} y {num2} es: {suma}")
"""
# Crear una suma de 2 números con función
# Defino las variables num1 y num2
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Defino la función sumar
def sumar(num1, num2):
    suma = num1 + num2
    
    print(f"La suma de {num1} y {num2} es: {suma}")
    
# Llamo a la función sumar y le paso las variables num1 y num2
suma = sumar(num1, num2)

# Defino la función restar
def restar(num1, num2):
    resta = num1 - num2
    
    print(f"La resta de {num1} y {num2} es: {resta}")
    
# Llamo a la función sumar y le paso las variables num1 y num2
resta = restar(num1, num2)