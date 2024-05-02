# Elige tu propia aventura

while True:
    
    print("***********************************************")
    print("Bienvenido al juego Elige tu propia aventura   ")
    print("                                               ")
    print("                               Creado por Pablo")
    
    print("Elija una opción del menú: ")
    
    print("0- SALIR")
    print("1- INICIAR JUEGO")
    
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 0:
        exit
    elif opcion == 1: 
        respuesta = input("Estás en un camino de tierra, ha llegado a su fin y puedes ir a izquierda o derecha. ¿Qué camino te gustaría tomar? (izquierda/derecha)")
    
        if respuesta = "izquierda":
            respuesta = input("Cuando llegas a un río, ¿puedes rodearlo o cruzarlo nadando? (caminar/nadar)")
            
            elif respuesta = "nadar":
                print("Había cocodrilos, perdés")    
            
            elif respuesta = "caminar"
                print("Encontraste un refugio, ganaste")
            
        elif respuesta = "derecha":
            print("Llegas a un puente, se tambalea y perdés")
            exit
                   
    
    else
    