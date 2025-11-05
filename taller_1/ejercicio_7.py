#Convertir de quintales a kilogramos

# Solicitar al usuario la cantidad de quintales
quintales = float(input("Ingrese la cantidad de quintales: "))

# Calcular los kilogramos (1 quintal = 100 kg)
kilogramos = quintales * 100

# Mostrar el resultado
print(f"\n{quintales:.2f} quintales equivalen a {kilogramos:.2f} kilogramos")