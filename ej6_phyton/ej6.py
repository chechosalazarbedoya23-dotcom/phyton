# Ejercicio: Gestor de eventos (Programación Orientada a Objetos)

class Evento:
    def __init__(self, nombre, presupuesto, asistentes):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.asistentes = asistentes

    def calcular_costo_por_participante(self):
        if self.asistentes > 0:
            return self.presupuesto / self.asistentes
        else:
            return 0.0

    def mostrar_resumen(self):
        costo_persona = self.calcular_costo_por_participante()
        print("\n--- DETALLES DEL EVENTO ---")
        print(f"Nombre del Evento: {self.nombre}")
        print(f"Presupuesto Total: ${self.presupuesto:,.2f}")
        print(f"Número de Asistentes: {self.asistentes}")
        print(f"Costo por Participante: ${costo_persona:,.2f}")


# --- Entrada de datos por el usuario ---
print("--- SISTEMA GESTOR DE EVENTOS ---")
nombre_evt = input("Ingresa el nombre del evento: ")
presupuesto_evt = float(input("Ingresa el presupuesto total: "))
asistentes_evt = int(input("Ingresa el número de asistentes: "))

# Instanciación del objeto
mi_evento = Evento(nombre_evt, presupuesto_evt, asistentes_evt)

# Llamada al método
mi_evento.mostrar_resumen()