# ============================================
# 1. Crear listas vacías y llenarlas por teclado
# ============================================

aprendices = []
edades = []

cantidad = int(input("¿Cuántos aprendices desea registrar?: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del aprendiz: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# ============================================
# 2. Imprimir las listas
# ============================================
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# ============================================
# 3. Mostrar el aprendiz con mayor edad
# ============================================
mayor = max(edades)
pos = edades.index(mayor)
print(f"El aprendiz con mayor edad es: {aprendices[pos]} ({mayor} años)")

# ============================================
# 4. Insertar nombre de la instructora en posición 1
# ============================================
instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, instructora)
print("Lista actualizada:", aprendices)

# ============================================
# 5. Contar cuántos aprendices tienen 18 años
# ============================================
conteo_18 = edades.count(18)
print(f"Cantidad de aprendices con 18 años: {conteo_18}")

# ============================================
# 6. Agregar aprendiz “x” al final de la lista
# ============================================
aprendices.append("x")
print("Lista con aprendiz 'x' agregado:", aprendices)

# ============================================
# 7. Borrar el nombre de la instructora
# ============================================
aprendices.remove(instructora)
print("Lista después de borrar la instructora:", aprendices)

# ============================================
# 8. Buscar un nombre en lista de aprendices
# ============================================
buscar = input("Ingrese un nombre a buscar: ")
if buscar in aprendices:
    print(f"{buscar} SÍ se encuentra en la lista.")
else:
    print(f"{buscar} NO se encuentra en la lista.")

# ============================================
# 9. Mostrar los primeros 10 aprendices
# ============================================
print("Primeros 10 aprendices:", aprendices[:10])

# ============================================
# 10. Mostrar los 10 últimos aprendices
# ============================================
print("Últimos 10 aprendices:", aprendices[-10:])

# ============================================
# 11. Mostrar del elemento 10 al 20
# ============================================
print("Aprendices del 10 al 20:", aprendices[9:20])

# ============================================
# 12. Mostrar elementos cuyo índice sea PAR
# ============================================
print("Elementos con índice PAR:")
for i in range(0, len(aprendices), 2):
    print(f"Índice {i}: {aprendices[i]}")