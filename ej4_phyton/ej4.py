# Ejercicio: Sistema de calificaciones

# 1. Entrada de datos
nota = float(input("Ingresa la calificación del estudiante (entre 0 y 5): "))

# 2. Validación del rango y control de flujo
if nota < 0 or nota > 5:
    print("\nError: La calificación debe estar dentro del rango de 0 a 5.")
elif nota >= 3.0:
    print(f"\nResultado: El estudiante APROBÓ con una nota de {nota}.")
else:
    print(f"\nResultado: El estudiante REPROBÓ con una nota de {nota}.")