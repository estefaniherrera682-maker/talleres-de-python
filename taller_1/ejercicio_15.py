
inicio = int(input("Número inicial de la registradora: "))
fin = int(input("Número final de la registradora: "))
valor_pasaje = float(input("Valor del pasaje: "))

total_pasajeros = fin - inicio
total_recaudo = total_pasajeros * valor_pasaje
empresa = total_recaudo * 0.75
conductor = total_recaudo * 0.25

print(f"Total pasajeros: {total_pasajeros}")
print(f"Valor total recaudado: ${total_recaudo:.2f}")
print(f"Empresa recibe: ${empresa:.2f}")
print(f"Conductor recibe: ${conductor:.2f}")