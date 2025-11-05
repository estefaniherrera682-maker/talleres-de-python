
costo_op1_ll1 = float(input("Costo llamada 1 (operador 1): "))
costo_op1_ll2 = float(input("Costo llamada 2 (operador 1): "))
costo_op2_ll1 = float(input("Costo llamada 1 (operador 2): "))
costo_op2_ll2 = float(input("Costo llamada 2 (operador 2): "))

total_op1 = costo_op1_ll1 + costo_op1_ll2
total_op2 = costo_op2_ll1 + costo_op2_ll2
total_general = total_op1 + total_op2

print(f"Total operador 1: ${total_op1:.2f}")
print(f"Total operador 2: ${total_op2:.2f}")
print(f"Total general: ${total_general:.2f}")