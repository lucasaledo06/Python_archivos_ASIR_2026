def calcular_costo_envio(peso, distancia, seguro_adicional:bool):
    coste = (peso*2.5) + (distancia * 0.1)
    if seguro_adicional == True:
        coste += 10
    return coste

print("=== Calculadora de envíos ===")
try:
    peso_usuario = float(input("Introduce el peso de tu paquete: "))
    distancia_usuario = float(input("Introduce la distancia que recorre tu paquete: "))
    confirmacion_SA = input("¿Desea usted seguro adicional? (S/N): ").upper()

    if confirmacion_SA == 'S':
        confirmacion_SA = True
    elif confirmacion_SA == 'N':
        confirmacion_SA = False
    else:
        print("ERROR 20031: Confirmación no válida")
        exit()
except ValueError:
    print("ERROR 20001: Parámetro no válido")
    exit()


coste_final = calcular_costo_envio(peso_usuario, distancia_usuario, confirmacion_SA)

print("============================")
print(f"Peso: {peso_usuario} kg")
print(f"Distancia: {distancia_usuario} km")
if confirmacion_SA == True:
    print("Seguro: Si")
else:
    print("Seguro: No")
print(f"Total: {calcular_costo_envio(peso=peso_usuario, distancia=distancia_usuario, seguro_adicional=confirmacion_SA):.2f}€")