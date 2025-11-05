
herencia_total = float(input("Ingrese el valor total de la herencia: "))
personas = 5  # madre + 4 hijos
monto_por_persona = herencia_total / personas

print(f"Cada uno recibe: ${monto_por_persona:.2f}")