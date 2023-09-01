#Escribir un programa que pregunte el correo electrónico del usuario en la consola 
#y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo_del_usuario = input("Ingrese su correo electrónico \n")
print(correo_del_usuario[:-9] + "ceu.es" )