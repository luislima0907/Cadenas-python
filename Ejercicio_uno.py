#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre_del_usuario = input("Ingrese su nombre \n")
numero_entero_ingresado = int(input("Ingrese un número entero \n"))

print((f"Tu nombre es: {nombre_del_usuario}" + "\n") * numero_entero_ingresado)