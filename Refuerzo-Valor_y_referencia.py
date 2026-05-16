def actualizar_sistema(nombre_responsable, lista_servidores):
    print("---[ Ejecutando dentro de la función ]---")
    nombre_responsable = "Administrador Root"
    lista_servidores.append("SRV-Seguridad")
    
    print(f"VALOR LOCAL -> Responsable: {nombre_responsable}")
    print(f"VALOR LOCAL -> Servidores: {servidores}")
# --- Programa Principal ---
responsable = "Juan Pérez"
servidores = ["SRV-Web", "SRV-Datos"]

print("--- ESTADO INICIAL ---")
print(f"Responsable: {responsable}")
print(f"Servidores: {servidores}")

# Llamada a la función enviando las variables
actualizar_sistema(responsable, lista_servidores=servidores)

print("--- ESTADO FINAL (FUERA DE LA FUNCIÓN) ---")
print(f"Resposable: {responsable}")
print(f"Servidores: {servidores}")

