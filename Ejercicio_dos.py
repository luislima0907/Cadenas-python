#Escribir un programa que pregunte el nombre completo del usuario en la consola 
#y después muestre por pantalla el nombre completo del usuario tres veces, 
#una con todas las letras minúsculas, otra con todas las letras mayúsculas 
#y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_del_usuario = input("Ingrese su nombre \n")

nombre_del_usuario_con_mayusculas = nombre_del_usuario.upper()
print(f"Nombre con mayúsculas: {nombre_del_usuario_con_mayusculas}")
nombre_del_usuario_con_minusculas = nombre_del_usuario.lower()
print(f"Nombre con minúsculas: {nombre_del_usuario_con_minusculas}")
nombre_del_usuario_con_inicial_mayuscula = nombre_del_usuario.title()
print(f"Nombre y apellido con inicial mayúscula: {nombre_del_usuario_con_inicial_mayuscula}")
