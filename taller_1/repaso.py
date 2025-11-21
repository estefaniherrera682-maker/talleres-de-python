      # Pedir tres notas al usuario 
#nota1 = int(input("Ingresa la primera nota: "))

#nota2 = int(input("Ingresa la segunda nota: "))
#nota3 = int(input("Ingresa la tercera nota: "))

#promedio = (nota1 + nota2 + nota3) / 3  # Calcular el promedio
#print("Tu promedio es:", promedio)

#if promedio >= 70:
    
    #print("Aprobaste ")
#else:
    #print("Reprobaste ")

#Calcular el total a pagar por la compra de zapatillas. Si se compran tres o más zapatillas se
#aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un
#descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el
#valor a pagar una vez aplicado el descuento.

cantidad = int(input("Ingresa la cantidad de zapatillas: "))
precio = float(input("Ingresa el precio de cada zapatilla: "))

total_compra = cantidad * precio

if cantidad >= 3:
    descuento = total_compra * 0.20   # 20% de descuento
else:
    descuento = total_compra * 0.10   # 10% de descuento

total_pagar = total_compra - descuento

print("Valor de la compra:", total_compra)
print("Valor del descuento:", descuento)
print("Total a pagar:", total_pagar)
 
