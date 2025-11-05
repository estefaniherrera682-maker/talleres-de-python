
alto = float(input("Ingrese el alto del muro (m): "))
ancho = float(input("Ingrese el ancho del muro (m): "))
area = alto * ancho
cajas = area / 3.5

print(f"Área total del baño: {area:.2f} m²")
print(f"Cajas necesarias: {cajas:.2f}")