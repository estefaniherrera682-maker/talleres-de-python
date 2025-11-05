
herencia_total = float(input("Ingrese el valor total de la herencia: "))

esposa = herencia_total * 0.40
hijo1 = herencia_total * 0.30
hijo2 = herencia_total * 0.20
hijo3 = herencia_total * 0.40
hijo4 = herencia_total * 0.10

print(f"Esposa recibe: ${esposa:.2f}")
print(f"Hijo 1 recibe: ${hijo1:.2f}")
print(f"Hijo 2 recibe: ${hijo2:.2f}")
print(f"Hijo 3 recibe: ${hijo3:.2f}")
print(f"Hijo 4 recibe: ${hijo4:.2f}")