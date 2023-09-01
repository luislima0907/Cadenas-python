#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase_del_usuario = str(input("Ingrese un frase \n"))
vocal_ingresada = input("Ingrese una vocal \n")
frase_con_vocal_ingresada_mayuscula = frase_del_usuario.replace(vocal_ingresada, vocal_ingresada.upper())
print(f"Tu frase es: {frase_con_vocal_ingresada_mayuscula}")