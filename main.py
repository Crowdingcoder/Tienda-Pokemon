
#Requerimientos
#1.	Mostrar menú de productos: 
#El programa debe mostrar el siguiente menú:
#1. Pokébola → $1000
#2. Poción → $1500
#3. Revivir → $3000
#4. Baya → $500
#5. Finalizar compra

#El usuario debe poder seleccionar productos ingresando el número correspondiente. 
#Validar que la opción ingresada sea correcta (entre 0 y 4). 
#Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 


#Cantidad de productos: 
#Por cada producto seleccionado, pedir la cantidad. 
#Validar que la cantidad sea un número entero positivo. 

#Acumulación de compra: 
#Calcular el total acumulado de la compra. 
#Llevar un contador de la cantidad total de productos comprados. 

#Aplicar los siguientes descuentos:
#Si el total de la compra supera los $5000 → aplicar 10% de descuento. 
#Si compra más de 10 productos en total → aplicar un 5% adicional. 
#Si el entrenador compra al menos 3 “Revivir” → aplicar un 15% adicional SOLO sobre ese producto. 
#Los descuentos son acumulables.

#Uso de bandera (flag): 
#Usar una bandera para verificar si el usuario compró al menos un producto antes de finalizar. 
#Si no compró nada, mostrar un mensaje:
#"No has realizado ninguna compra." 


#Manejo de errores: 
#Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 

#Manejo de errores: 
#Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 

import os
os.system("cls")

pokebola = 1000
pocion = 1500
revivir = 3000
baya = 500
tienda = True
contador1= 0
compra_pokebola= 0
compra_pocion= 0
compra_revivir = 0
compra_baya= 0
compra_total = (pokebola * compra_pokebola) + (pocion * compra_pocion) + (revivir * compra_revivir) + (baya * compra_baya)
try:
    print("Bienvenido a la poketienda")
    contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
    while contador1 not in range(1,6):
        contador1 = int(input("El valor ingresado no es pokevalido\nIngrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
    
    while tienda:
        if contador1 == 1:
            compra_pokebola = int(input("Seleccione cantidad de pokébolas:\n"))
            if compra_pokebola <=0:
                print("El valor no es pokevalido")
        elif contador1 == 2:
            compra_pocion = int(input("Seleccione cantidad de pociones:\n"))
            if compra_pocion <= 0:
                print("El valor no es pokevalido")
        elif contador1 == 3:
            compra_revivir =int(input("Seleccione cantidad de revivir:\n"))
            if compra_revivir <=0:
                print("El valor no es pokevalido")
        elif contador1 == 4:
            compra_baya = int(input("Seleccione cantidad de bayas:\n"))
            if compra_baya <= 0:
                print("El valor no es pokevalido")
        elif contador1 == 5:
            print("Hasta la pokeproxima")
            tienda = False


except:
    print("Los valores ingresados no son pokevalidos")
