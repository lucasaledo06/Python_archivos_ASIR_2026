def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)

posicion = int(input("Introduce un número de la lista fibonacci: "))
print(f"El número de Fibonacci en la posicion {posicion} es: {fibonacci(posicion)}")

lista = []

for i in range(posicion + 1):
    lista.append(fibonacci(i))
print(lista)