#El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
#25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
#metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
#para otros proyectos.

#solicitamos
area_total = float(input("Ingrese el área total del terreno (m²) : "))

#calculamos los porcentajes 
cultivos = area_total * 0.40
vivienda = area_total * 0.25
zonas_verdes = area_total * 0.15
otros = area_total - (cultivos + vivienda + zonas_verdes)

print(f"Cultivos : {cultivos:.2f} m²")
print(f"Vivienda : {vivienda:.2f} m²")
print(f"Zonas verdes: {zonas_verdes:.2f} m²")
print(f"Área disponible para otros proyectos : {otros:.2f} m²")