#Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
#referente al dinero que les corresponde en una herencia dejada por su esposo y padre
#respectivamente.

herencia_total = float(input("Ingrese el valor total de la herencia : "))
personas = 5  # la madre y los 4 hijos
monto_por_persona = herencia_total / personas

print(f"Cada uno recibe : ${monto_por_persona:.2f}")