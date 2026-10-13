# Ejercicio: Calculadora de costos de eventos

# 1. Definición de la función para calcular el costo total
def calcular_costo_evento(alquiler, materiales, transporte, alimentacion):
    total = alquiler + materiales + transporte + alimentacion
    return total

# 2. Entrada de datos por parte del usuario
print("--- CALCULADORA DE COSTOS DE EVENTO ---")
costo_alquiler = float(input("Ingresa el gasto de alquiler: "))
costo_materiales = float(input("Ingresa el gasto de materiales: "))
costo_transporte = float(input("Ingresa el gasto de transporte: "))
costo_alimentacion = float(input("Ingresa el gasto de alimentación: "))

# 3. Llamada a la función pasando los argumentos
total_evento = calcular_costo_evento(
    costo_alquiler, 
    costo_materiales, 
    costo_transporte, 
    costo_alimentacion
)

# 4. Mostrar el resultado
print("\n--- RESUMEN DE GASTOS ---")
print(f"Alquiler: ${costo_alquiler:,.2f}")
print(f"Materiales: ${costo_materiales:,.2f}")
print(f"Transporte: ${costo_transporte:,.2f}")
print(f"Alimentación: ${costo_alimentacion:,.2f}")
print(f"-----------------------------")
print(f"Costo Total del Evento: ${total_evento:,.2f}")