
# Calculadora básica

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Ingrese una opción (1-4): ")

if opcion == "1":
    resultado = numero1 + numero2
    print("El resultado de la suma es:", resultado)

elif opcion == "2":
    resultado = numero1 - numero2
    print("El resultado de la resta es:", resultado)

elif opcion == "3":
    resultado = numero1 * numero2
    print("El resultado de la multiplicación es:", resultado)

elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: no se puede dividir entre cero.")

else:
    print("Opción no válida.")
