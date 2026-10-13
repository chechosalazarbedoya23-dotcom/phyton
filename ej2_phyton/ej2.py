# Ejercicio: Calculadora básica

# 1. Entrada de datos (solicitar dos números al usuario)
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# 2. Operaciones matemáticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Manejo de división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# 3. Salida por pantalla de los resultados
print("\n--- RESULTADOS ---")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")