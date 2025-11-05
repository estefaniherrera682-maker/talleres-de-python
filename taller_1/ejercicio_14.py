#En clase de programación, se sacan 4 notas del 15%,30%,30%,25% respectivamente. Se
#pide diseñar un algoritmo que permita mostrar la nota definitiva de un estudiante.
#Teniendo en cuenta que la primera nota consta del promedio de dos talleres, la segunda
#de tres evaluaciones, la tercera nota de un trabajo final y la última es el promedio de 4
#quizzes.


# primera nota: promedio de 2 talleres
taller1 = float(input("Nota del taller 1 : "))
taller2 = float(input("Nota del taller 2 : "))
nota1 = (taller1 + taller2) / 2

# segunda nota: promedio de 3 evaluaciones
eval1 = float(input("Evaluación 1 : "))
eval2 = float(input("Evaluación 2 : "))
eval3 = float(input("Evaluación 3 : "))
nota2 = (eval1 + eval2 + eval3) / 3

# tercera nota: trabajo final
nota3 = float(input("Nota del trabajo final: "))

# cuarta nota: promedio de 4 quizzes
quiz1 = float(input("Quiz 1 : "))
quiz2 = float(input("Quiz 2 : "))
quiz3 = float(input("Quiz 3 : "))
quiz4 = float(input("Quiz 4 : "))
nota4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4

# nota definitiva
nota_definitiva = (nota1 * 0.15) + (nota2 * 0.30) + (nota3 * 0.30) + (nota4 * 0.25)

print(f"\nLa nota definitiva del estudiante es : {nota_definitiva:.2f}")