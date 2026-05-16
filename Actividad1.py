def calcular_area_triangulo (base, altura):
    area = (base * altura) / 2 
    return area
print("\n ==== Área Triángulo ====")
mi_base = int(input("Introduce la base de tu triángulo: "))
mi_altura = int(input("Introduce la altura de tu triángulo: "))
print(f"El área de tu triangulo es de {calcular_area_triangulo(mi_base, mi_altura)}m^2")
