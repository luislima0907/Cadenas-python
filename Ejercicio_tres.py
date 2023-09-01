#Escribir un programa que pregunte el nombre del usuario en la consola 
#y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
#donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

nombre_del_usuario = input("Ingrese su nombre \n")
cantidad_de_letras_del_nombre_ingresado = nombre_del_usuario.__len__()

print(f"{nombre_del_usuario} tiene {cantidad_de_letras_del_nombre_ingresado} letras")