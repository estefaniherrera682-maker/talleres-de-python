#El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
#enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
#alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
#número de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros
#cuadrados.

alto = float(input("Ingrese el alto del muro (m) : "))
ancho = float(input("Ingrese el ancho del muro (m) : "))

# area del baño
area = alto * ancho

# cada caja trae 3.5 m²
cajas = area / 3.5

print(f"Área total del baño : {area:.2f} m²")
print(f"Cajas necesarias : {cajas:.2f}")