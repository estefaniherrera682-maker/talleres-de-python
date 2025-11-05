#Un atleta tiene la costumbre de medir el tiempo (en minutos) y la distancia (en metros)
#durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
#tiempo que duro el entrenamiento, la distancia recorrida, y el promedio del tiempo y la
#distancia recorrida.

# dia 1
tiempo1 = float(input("Tiempo día 1 (min) : "))
distancia1 = float(input("Distancia día 1 (m) : "))

# dia 2
tiempo2 = float(input("Tiempo día 2 (min) : "))
distancia2 = float(input("Distancia día 2 (m) : "))

# dia 3
tiempo3 = float(input("Tiempo día 3 (min) : "))
distancia3 = float(input("Distancia día 3 (m) : "))

# el total y promedio
tiempo_total = tiempo1 + tiempo2 + tiempo3
distancia_total = distancia1 + distancia2 + distancia3

prom_tiempo = tiempo_total / 3
prom_distancia = distancia_total / 3

print(f"\nTiempo total : {tiempo_total} min")
print(f"Distancia total : {distancia_total} m")
print(f"Promedio de tiempo : {prom_tiempo:.2f} min")
print(f"Promedio de distancia : {prom_distancia:.2f} m")