#El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
#trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.

desempleoInicial= int (input ("Ingrese el valor inicial del desempleo : "))

#aumento del 9.5% 
aumento= desempleoInicial * 0.095
despuesAumento= desempleoInicial + aumento

#caida del 1.5% en el segundo trimestre
disminucion= despuesAumento *0.015
desempleoActual = despuesAumento - disminucion

print(f"Desempleo inicial : {desempleoInicial}")
print(f"Aumento (9,5%) : {aumento}")
print(f"Despues del aumento : {despuesAumento}")
print(f"Disminucion (1,5%) : {disminucion}")
print(f"Desempleo Actual :  {desempleoActual}")
