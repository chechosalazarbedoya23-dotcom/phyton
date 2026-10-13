from datetime import datetime

# 1. Solicitar el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# 2. Obtener la fecha actual
fecha_actual = datetime.now().strftime("%d/%m/%Y")

# 3. Mostrar el mensaje de bienvenida y la fecha
print(f"\n¡Hola, {nombre}! Bienvenido/a a tu primer programa.")
print(f"Fecha de ejecución: {fecha_actual}")