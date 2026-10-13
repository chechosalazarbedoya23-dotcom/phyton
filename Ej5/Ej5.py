
# Calculadora de costos de eventos

def calcular_costo(alquiler, materiales, transporte, alimentacion):
    total = alquiler + materiales + transporte + alimentacion
    return total

print("=== COSTOS DEL EVENTO ===")

alquiler = float(input("Ingrese el costo del alquiler: "))
materiales = float(input("Ingrese el costo de los materiales: "))
transporte = float(input("Ingrese el costo del transporte: "))
alimentacion = float(input("Ingrese el costo de la alimentación: "))

total = calcular_costo(alquiler, materiales, transporte, alimentacion)

print("\n=== RESUMEN DE COSTOS ===")
print("Alquiler:", alquiler)
print("Materiales:", materiales)
print("Transporte:", transporte)
print("Alimentación:", alimentacion)
print("Costo total del evento:", total)
