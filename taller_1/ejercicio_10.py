
t1 = float(input("Tiempo día 1 (min): "))
t2 = float(input("Tiempo día 2 (min): "))
t3 = float(input("Tiempo día 3 (min): "))
d1 = float(input("Distancia día 1 (m): "))
d2 = float(input("Distancia día 2 (m): "))
d3 = float(input("Distancia día 3 (m): "))

tiempo_total = t1 + t2 + t3
distancia_total = d1 + d2 + d3
prom_tiempo = tiempo_total / 3
prom_distancia = distancia_total / 3

print(f"Tiempo total: {tiempo_total} min")
print(f"Distancia total: {distancia_total} m")
print(f"Promedio de tiempo: {prom_tiempo:.2f} min")
print(f"Promedio de distancia: {prom_distancia:.2f} m")