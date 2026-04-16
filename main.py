
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

import os
os.system("cls")

#precions
pokebola = 1000
pocion = 1500
revivir = 3000
baya = 500
tienda = True

contador1= 0
#Compra productos
compra_pokebola= 0
compra_pocion= 0
compra_revivir = 0
compra_baya= 0
compra_final = 0
#Total productos
total_pokebola = 0
total_pocion = 0
total_revivir = 0
total_baya = 0



try:
    print("Bienvenido a la poketienda")
    contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
    #validar opcion ingresada sea correcta
    while contador1 not in range(1,6):
        contador1 = int(input("El valor ingresado no es pokevalido\nIngrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
    
    #poketienda
    while tienda:
        compra_total = (pokebola * total_pokebola) + (pocion * total_pocion) + (revivir * total_revivir) + (baya * total_baya)
        if contador1 == 1:
            compra_pokebola = int(input("Seleccione cantidad de pokébolas:\n"))
            total_pokebola = total_pokebola + compra_pokebola
            contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
            if compra_pokebola <=0:
                print("El valor no es pokevalido")
        elif contador1 == 2:
            compra_pocion = int(input("Seleccione cantidad de pociones:\n"))
            total_pocion = total_pocion + compra_pocion
            contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
            if compra_pocion <= 0:
                print("El valor no es pokevalido")
        elif contador1 == 3:
            compra_revivir =int(input("Seleccione cantidad de revivir:\n"))
            total_revivir =total_revivir + compra_revivir
            contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
            if compra_revivir <=0:
                print("El valor no es pokevalido")
        elif contador1 == 4:
            compra_baya = int(input("Seleccione cantidad de bayas:\n"))
            total_baya = total_baya + compra_baya
            contador1 = int(input("Ingrese unda de las siguientes opciones:\n1.Pokébola $1000\n2.Pocion $1500\n3.Revivir $3000\n4.Baya $500\n5.Finalizar compra.\n"))
            if compra_baya <= 0:
                print("El valor no es pokevalido")
        elif contador1 == 5 and compra_total == 0:
            print(f"Hasta la pokeproxima")
            tienda = False
        elif contador1 == 5 and compra_total > 0:
            tienda = False
    cantidad_producto = total_pokebola + total_pocion + total_revivir + total_baya
    #descuentos
    if compra_total > 5000:
        descuento_precio = compra_total * 0.1
    else:
        descuento_precio = 0
    if cantidad_producto >= 10:
        descuento_cantidad = compra_total * 0.05
    else:
        descuento_cantidad = 0
    if total_revivir >= 3:
        descuento_revivir = (total_revivir * revivir) * 0.15
    else:
        descuento_revivir = 0
    
    if compra_total > 0:
        print(f"Su poketotal sin descuentos es ${compra_total}")
        print(f"Lleva {total_pokebola} pokebolas")
        print(f"Lleva {total_pocion} pociones")
        print(f"Lleva {total_revivir} revivir")
        print(f"Lleva {total_baya} bayas")
        total_final = compra_total - descuento_cantidad - descuento_precio - descuento_revivir
        
        print(f"Su total final es:${total_final}")






except:
    print("Los valores ingresados no son pokevalidos")
