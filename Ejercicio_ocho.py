#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio_del_producto = float(input("Ingrese el precio del producto con números decimales \n"))
precio_del_producto_entero = precio_del_producto.__trunc__()
precio_del_producto_caracter = str(precio_del_producto)
precio_del_producto_decimal = precio_del_producto_caracter[precio_del_producto_caracter.find(".")+1:]
print(f"El precio del producto es de: {precio_del_producto_entero} Euros, con {precio_del_producto_decimal} centimos")