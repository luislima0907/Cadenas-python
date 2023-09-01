#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
#y muestre por pantalla cada uno de los productos en una línea distinta.

productos_de_la_cesta = input("Ingrese los productos que tiene en su cesta \n")
print(productos_de_la_cesta.replace(",", "\n"))