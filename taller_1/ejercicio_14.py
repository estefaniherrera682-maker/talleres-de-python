
t1 = float(input("Taller 1: "))
t2 = float(input("Taller 2: "))
prom_talleres = (t1 + t2) / 2

e1 = float(input("Evaluación 1: "))
e2 = float(input("Evaluación 2: "))
e3 = float(input("Evaluación 3: "))
prom_evaluaciones = (e1 + e2 + e3) / 3

trabajo_final = float(input("Nota trabajo final: "))

q1 = float(input("Quiz 1: "))
q2 = float(input("Quiz 2: "))
q3 = float(input("Quiz 3: "))
q4 = float(input("Quiz 4: "))
prom_quiz = (q1 + q2 + q3 + q4) / 4

nota_final = (prom_talleres * 0.15) + (prom_evaluaciones * 0.30) + (trabajo_final * 0.30) + (prom_quiz * 0.25)

print(f"La nota definitiva es: {nota_final:.2f}")