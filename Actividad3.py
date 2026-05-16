PRECIO_BASE = 50.0
RECARGO_EXPRESS = 15.0


def procesar_pedido(item, cantidad, descuento, envio_express=False):
    total = PRECIO_BASE * cantidad

    total = total - (total * descuento)

    if envio_express:
        total += RECARGO_EXPRESS

    return total


print("---- Procesador de Pedidos en Linea ----")
print("Precio base del artículo: 50.00 €")

item = input("1. Introduce el nombre del articulo: ")
cantidad = int(input("2. Introduce la cantidad de unidades: "))
descuento_input = float(input("3. Introduce el porcentaje de descuento (ej: 10 para 10%): "))
envio = input("4. ¿Desea envío Express (S/N)? ").upper()

# convertir datos
descuento = descuento_input / 100

if envio == "S":
    envio = True
else:
    envio = False


# llamada con parámetros posicionales + por nombre
total = procesar_pedido(
    item,
    cantidad,
    descuento=descuento,
    envio_express=envio
)

print("\n---- Resultado del Pedido ----")
print(f"Artículo: {item}")
print(f"Unidades: {cantidad}")
print(f"Descuento: {descuento_input}%")
print(f"Envío Express: {'Sí' if envio else 'No (Default: No)'}")

print(f"\n💰 El COSTO TOTAL del pedido es: € **{total:.2f}**")