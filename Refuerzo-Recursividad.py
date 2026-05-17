def es_palindromo(frase):
    # Eliminar espacios y convertir a minúsculas
    frase = frase.replace(" ", "").lower()

    # Caso base
    if len(frase) <= 1:
        return True

    # Comparar extremos
    if frase[0] != frase[-1]:
        return False

    # Llamada recursiva
    return es_palindromo(frase[1:-1])


# Pruebas
texto = input("Introduce una frase: ")

if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

