#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de teléfono con este formato 
#y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

numero_telefonico_del_usuario = input("Ingrese su número de teléfono \n")
eliminar_prefijo_y_extension = numero_telefonico_del_usuario

print(eliminar_prefijo_y_extension [4:-3])