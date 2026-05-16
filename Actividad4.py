# =========== MODIFICAR INMUTABLE ===========
def modificar_inmutable(x):
    print(f"ID del valor antes del cambio: {id(x)}")
    x = x + 10
    print(f"Valor tras cambio: {x}")
    print(f"ID dentro de la función (Tras cambio): {id(x)}")
# =========== MODIFICAR MUTABLE ===========
def modificar_mutable(lista):
    nuevo_valor = input("Introduce un valor para añadir a la lista: ").strip()
    lista.append(nuevo_valor)
    print(f"ID dentro de la función (tras append): {id(lista)}")
    print(f"lista dentro de la funcion: {lista}")


# =========== MODIFICAR INMUTABLE ===========
print("--- 1. Comportamiento INMUTABLE (entero) ---")
mi_numero = int(input("Introduce un número entero: "))
print(f"Valor antes de la llamada: {mi_numero}")
print(f"ID del valor antes de la llamada: {id(mi_numero)}")

# llamo a la función
modificar_inmutable(mi_numero)
print(f"Valor después de la llamada: {mi_numero}")
print(f"ID del valor después de la llamada: {id(mi_numero)}")
print("Conclusión: no ha cambiado")

# =========== MODIFICAR MUTABLE ===========
print("--- 2. Comportamiento MUTABLE (Lista) ---")
mi_lista = []
entrada = ""
print("Rellena la lista. Pulsa ENTER sin escribir para terminar")

while True:
    entrada = input("Introduce un elemento para la lista: ").strip()
    if entrada == "":
        break
    mi_lista.append
if not mi_lista:
    mi_lista = ["rojo", "azul"]

print(f"\n[P] Lista antes de la llamada: {mi_lista}")
print(f"[P] ID antes de la llamada: {id(mi_lista)}")

modificar_mutable(mi_lista)

print(f"\n[P] Lista DESPUES de la llamada: {mi_lista}")
print(f"[P] ID DESPUÉS de la llamada: {id(mi_lista)}")
print("Conclusion: El valor sf ha cambiado fuera de la funcion (Paso por Referencia).\n")