#que el usuario ingrese el salario basico del empleado
salario_basico = int(input("ingrese el salario básico del empleado: "))

#calcula la retencion del 18%
retencion = salario_basico * 0.18

#calcula la bonificacion del 1.3%
bonificacion = salario_basico * 0.013

#calcula el salario neto
salario_neto = salario_basico - retencion + bonificacion

#imprime los resultados
print(f"salario basico : {salario_basico}")
print(f"retencion (18%): {retencion}")
print(f"bonificacion (1.3%): {bonificacion}")
print(f"salario neto: {salario_neto}")

