
# Gestor de eventos

class Evento:
    def __init__(self, nombre, presupuesto, asistentes, costo_total):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.asistentes = asistentes
        self.costo_total = costo_total

    def calcular_costo_participante(self):
        if self.asistentes > 0:
            return self.costo_total / self.asistentes
        else:
            return 0

    def consultar_presupuesto(self):
        return self.presupuesto - self.costo_total


print("=== GESTOR DE EVENTOS ===")

nombre = input("Ingrese el nombre del evento: ")
presupuesto = float(input("Ingrese el presupuesto del evento: "))
asistentes = int(input("Ingrese el número de asistentes: "))
costo_total = float(input("Ingrese el costo total del evento: "))

evento = Evento(nombre, presupuesto, asistentes, costo_total)

print("\n=== RESULTADOS ===")
print("Nombre del evento:", evento.nombre)
print("Presupuesto:", evento.presupuesto)
print("Número de asistentes:", evento.asistentes)
print("Costo por participante:", evento.calcular_costo_participante())
print("Presupuesto disponible:", evento.consultar_presupuesto())
