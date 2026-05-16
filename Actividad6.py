def mostrar_factura(producto:str, precio_base:float):
    def calcular_iva(cantidad):
        return cantidad * 0.21
    iva = calcular_iva(precio_base)
    precio_total = iva + precio_base

    print(f"Producto: {producto}")
    print(f"Precio Base: {precio_base}")
    print(f"Subtotal IVA (21%): {iva:.2f}")
    print(f"Total: {precio_total:.2f}")

print ("--- Generador de Facturas ---")
producto = str(input("Introduce el nombre de tu producto: "))
precio_base = float(input("Introduce el precio base: "))

print("--- Factura Simplificada ---")
mostrar_factura(producto, precio_base)