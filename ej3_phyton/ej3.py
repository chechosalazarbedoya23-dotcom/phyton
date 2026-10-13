# Ejercicio: Presupuesto personal

# 1. Entrada de datos y conversión de tipos
usuario = str(input("Ingresa tu nombre: "))
ingresos = float(input("Ingresa tus ingresos totales: "))
gastos = float(input("Ingresa tus gastos totales: "))

# 2. Cálculo del saldo disponible
saldo_disponible = ingresos - gastos

# 3. Variable tipo booleano para verificar si el saldo es positivo
tiene_ahorro = saldo_disponible > 0

# 4. Salida por pantalla
print("\n--- RESUMEN DE PRESUPUESTO PERSONAL ---")
print(f"Usuario: {usuario}")
print(f"Ingresos totales: ${ingresos:,.2f}")
print(f"Gastos totales: ${gastos:,.2f}")
print(f"Saldo disponible: ${saldo_disponible:,.2f}")
print(f"¿Tiene saldo a favor?: {tiene_ahorro}")