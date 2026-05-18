PRECIO_BASE = 50.0
RECARGO_EXPRESS = 15.0


def procesar_pedido(item, cantidad, descuento, envio_express=False):
    total = (PRECIO_BASE * cantidad) * (1 - descuento)

    if envio_express:
        total += RECARGO_EXPRESS

    return total


print("---- Procesador de Pedidos en Linea ----")

item = input("1. Introduce el nombre del articulo: ")
cantidad = int(input("2. Introduce la cantidad de unidades: "))
descuento = float(input("3. Descuento (ej: 10 para 10%): ")) / 100
envio_express = input("4. ¿Envio Express (S/N)? ").upper() == "S"

total = procesar_pedido(
    item,
    cantidad,
    descuento=descuento,
    envio_express=envio_express
)

print("\n---- Resultado del Pedido ----")
print(f"Artículo: {item}")
print(f"Unidades: {cantidad}")
print(f"Descuento: {descuento*100:.0f}%")
print(f"Envío Express: {'Sí' if envio_express else 'No'}")
print(f"\nTOTAL: € {total:.2f}")
