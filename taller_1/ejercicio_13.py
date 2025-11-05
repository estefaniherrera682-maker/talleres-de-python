
area_total = float(input("Ingrese el área total del terreno (m²): "))
cultivos = area_total * 0.40
vivienda = area_total * 0.25
zonas_verdes = area_total * 0.15
otros = area_total - (cultivos + vivienda + zonas_verdes)

print(f"Cultivos: {cultivos:.2f} m²")
print(f"Vivienda: {vivienda:.2f} m²")
print(f"Zonas verdes: {zonas_verdes:.2f} m²")
print(f"Área disponible para otros proyectos: {otros:.2f} m²")