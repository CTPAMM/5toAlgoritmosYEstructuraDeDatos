# Repaso de modelos de ejercicios.

# Ejemplo de ejercicio 1: Imprima en pantalla "Hola Mundo".

print("Hola Mundo, bienvenidos a Python")

# Ejemplo de ejercicio 2: Imprima un menú de opciones a elección

print("****Menú de Lenguajes de Programación*****")
print("1- Python")
print("2- PHP")
print("3- Java")
print("4- C++")
print("*************************")

# Multiplique 2 números e imprima en pantalla el resultado
#(Resta(-); Multiplicación(*); División(/); Potenciación(**))

numero1 = 23
numero2 = 15

print("La multiplicación de los números es: ")
print(numero1 * numero2)

# Ingrese por teclado 2 números e imprima en pantalla el resultado de su resta.
#(Resta(-); Multiplicación(*); División(/); Potenciación(**))


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("La resta de los números es: ")
print(numero1 - numero2)


# Crear una lista e imprimirla en pantalla

lista_lenguajes_programacion = ['Python', 'PHP', 'Java', "C++"]

print(lista_lenguajes_programacion)

# Bucle for
for lenguaje in lista_lenguajes_programacion:
    print(lenguaje)