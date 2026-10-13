
# Sistema de calificaciones

nota = float(input("Ingrese la nota del estudiante (0 a 5): "))

if nota >= 0 and nota <= 5:
    if nota >= 3:
        print("El estudiante aprobó.")
    else:
        print("El estudiante reprobó.")
else:
    print("Error: la nota debe estar entre 0 y 5.")
