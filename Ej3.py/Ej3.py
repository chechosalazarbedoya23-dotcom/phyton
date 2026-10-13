# Presupuesto personal

print("=== PRESUPUESTO PERSONAL ===")

ingresos = float(input("Ingrese sus ingresos: "))
gastos = float(input("Ingrese sus gastos: "))

saldo = ingresos - gastos

print("\n=== RESULTADOS ===")
print("Ingresos totales:", ingresos)
print("Gastos totales:", gastos)
print("Saldo disponible:", saldo)

if saldo > 0:
    print("Tiene dinero disponible.")
elif saldo == 0:
    print("Sus ingresos son iguales a sus gastos.")
else:
    print("Atención: sus gastos superan sus ingresos.")
