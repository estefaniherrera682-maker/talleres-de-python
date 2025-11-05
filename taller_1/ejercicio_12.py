#El testamento tiene las siguientes condiciones: A la esposa le corresponde el 40% mientras
#que a los hijos les corresponde: 30% 20% 40% 10% respectivamente. Se pide un algoritmo
#que lea los datos necesarios, y muestre lo que le corresponde a la esposa y a los hijos.

#solicita el valor de la herencia
herencia_total = float(input("Ingrese el valor total de la herencia : "))
#calculamos los porcentajes 
esposa = herencia_total * 0.40
hijo1 = herencia_total * 0.30
hijo2 = herencia_total * 0.20
hijo3 = herencia_total * 0.40
hijo4 = herencia_total * 0.10

print(f"esposa : ${esposa:.2f}")
print(f"hijo 1 : ${hijo1:.2f}")
print(f"hijo 2 : ${hijo2:.2f}")
print(f"hijo 3 : ${hijo3:.2f}")
print(f"hijo 4 : ${hijo4:.2f}")