# solicitar el area inicial del terreno
area_inicial = float(input("Ingrese el área inicial del terreno (en metros cuadrados): "))

# restarle el area en un 10%
area_reducida = area_inicial * (1 - 0.10)

# aumento de  area reducida en un 50%
area_final = area_reducida * (1 + 0.50)


print(f"\nÁrea inicial: {area_inicial:.2f} m²")
print(f"Área después de la reducción del 10%: {area_reducida:.2f} m²")
print(f"Área final después de aumentar el 50%: {area_final:.2f} m²")