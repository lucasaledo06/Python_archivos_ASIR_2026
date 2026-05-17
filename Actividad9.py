# --- Importar módulos ---
import random
import os
from os import sys
# --- Programa principal ---
aleatorio = random.randint(1,10) # Generar número aleatorio con el módulo RANDOM
# print(aleatorio) # <-- Descomentar para depurar el condicional
adivinar = int(input("Adivina el número secreto (1 al 10): ")) # Pedir al usuario un número por teclado
if adivinar == aleatorio: # Condición de igualdad
    print("\n¡FELICIDADES! Has acertado.")
    print(f"Tu sistema operativo es: {os.name}") # Mostrar el sistema operativo donde se ejecuta con el módulo OS
    print(f"Estás trabajando en: {os.getcwd()}") # Mostrar la ruta de ejecución del programa con el módulo OS
    print(f"Versión de Python: {sys.version}") # Mostrar la versión de python con el módulo SYS

else: # si no se cumple sale del programa
    print(f"No has acertado, el número secreto era {aleatorio}") # Mostrar cual era el número correcto
    sys.exit() # Salir del programa con el módulo SYS
