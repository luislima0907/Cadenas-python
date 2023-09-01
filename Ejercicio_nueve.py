#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
#y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione 
#cuando el día o el mes se introduzcan con un solo carácter.

dia_de_nacimiento_del_usuario = int(input("Ingrese el día de su nacimiento \n"))
mes_de_nacimiento_del_usuario = int(input("Ingrese el mes de su nacimiento \n"))
anio_de_nacimiento_del_usuario = int(input("Ingrese el año de su nacimiento \n"))

if dia_de_nacimiento_del_usuario == 0 or dia_de_nacimiento_del_usuario > 31 or mes_de_nacimiento_del_usuario == 0 or mes_de_nacimiento_del_usuario > 12:
    print("Esta no es un fecha valida")
else:
    print(f"Naciste el: {dia_de_nacimiento_del_usuario}/{mes_de_nacimiento_del_usuario}/{anio_de_nacimiento_del_usuario}")
