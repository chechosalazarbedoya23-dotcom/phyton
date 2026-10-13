from datetime import datetime

# 1. Solicitar el nombre al usuario
nombre = input("Por favor, ingresa tu nombre: ")

# 2. Obtener la fecha de ejecución actual
fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# 3. Mostrar el mensaje de bienvenida y la fecha
print(f"\n¡Hola, {nombre}! Bienvenido/a.")
print(f"Fecha y hora de ejecución: {fecha_actual}")