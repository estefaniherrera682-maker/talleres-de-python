#El sistema de liquidación que hacen los conductores de buses y los colectivos a las
#diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro
#al terminarlo. La diferencia de estos dos números determina el número de pasajeros
#transportados en el día. Realizar un algoritmo que permita leer estos dos números y el
#valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y
#el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes
#del dinero mientras el conductor recibe el resto.

inicio = int(input("Número inicial de la registradora: "))
fin = int(input("Número final de la registradora: "))
valor_pasaje = float(input("Valor del pasaje: "))

total_pasajeros = fin - inicio
total_recaudo = total_pasajeros * valor_pasaje
empresa = total_recaudo * 0.75
conductor = total_recaudo * 0.25

print(f"Total pasajeros : {total_pasajeros}")
print(f"Valor total recaudado : ${total_recaudo:.2f}")
print(f"Empresa recibe : ${empresa:.2f}")
print(f"Conductor recibe : ${conductor:.2f}")