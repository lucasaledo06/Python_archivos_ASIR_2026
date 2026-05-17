# --- Importar Módulos ---
import datetime
import math
# --- Programa Principal ---
anio = int(input("¿En que año naciste? (YYYY): ")) # Pedir al usuario su año 
mes = int(input("¿En que mes? (1-12): ")) # Pedir al usuario su mes
dia = int(input("¿En que día?: ")) # Pedir al usuario su dia

fecha_nacimiento = datetime.datetime(anio, mes, dia) # juntar la fecha con el módulo DATETIME
hoy = datetime.datetime.now() # Sacar la fecha de hoy con DATETIME
diferencia = hoy - fecha_nacimiento # calcular la diferencia restando las dos fechas

dias_vividos = diferencia.days # Obtener los días de una fecha con el módulo DATETIME

raiz = math.sqrt(dias_vividos) # Calcular la raíz cuadrada con el módulo MATH

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Has vivido", dias_vividos, "días")
print("La raíz cuadrada de tus días vividos es:", raiz)
print(f"El valor de PI es: {math.pi}" )