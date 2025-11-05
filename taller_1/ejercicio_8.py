#Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
#segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
#llamadas a cada operador, y el total de las cuatro llamadas.


# llamadas al primer operador
llamada1_op1 = float(input("Costo de la primera llamada al operador 1 : "))
llamada2_op1 = float(input("Costo de la segunda llamada al operador 1 : "))

# llamadas al segundo operador
llamada1_op2 = float(input("Costo de la primera llamada al operador 2 : "))
llamada2_op2 = float(input("Costo de la segunda llamada al operador 2 : "))

# totales por operador
total_op1 = llamada1_op1 + llamada2_op1
total_op2 = llamada1_op2 + llamada2_op2

# total general
total_general = total_op1 + total_op2

print(f"\nTotal llamadas operador 1 : ${total_op1:.2f}")
print(f"Total llamadas operador 2 : ${total_op2:.2f}")
print(f"Total general de las cuatro llamadas : ${total_general:.2f}")