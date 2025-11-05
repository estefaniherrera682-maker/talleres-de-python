# Convertir minutos a horas

# Solicitar al usuario la cantidad de minutos
minutos = int(input("Ingrese la cantidad de minutos: "))

# Calcular horas y minutos restantes
horas = minutos // 60        # división entera para obtener las horas completas
minutos_restantes = minutos % 60  # el resto son los minutos sobrantes

# Mostrar el resultado
print(f"\n{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos")