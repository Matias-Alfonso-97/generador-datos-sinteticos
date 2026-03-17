import random
import json  # 1. Traemos la herramienta para exportar datos

def generar_cliente():
    nombres_posibles = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
    nombre_elegido = random.choice(nombres_posibles)
    edad_elegida = random.randint(18, 65)
    
    cliente = {
        "nombre": nombre_elegido,
        "edad": edad_elegida
    }
    return cliente

# Inicializamos la lista vacía
base_de_datos = []

# Iteramos 100 veces
for i in range(100):
    nuevo_cliente = generar_cliente()
    base_de_datos.append(nuevo_cliente)

# --- LAS 3 LÍNEAS NUEVAS AL FINAL DE TODO ---

# 2. Abrimos (o creamos) un archivo en modo escritura ("w" de write)
with open("clientes_sinteticos.json", "w") as archivo:
    # 3. Volcamos nuestra lista en el archivo. El indent=4 es para que quede prolijo y legible.
    json.dump(base_de_datos, archivo, indent=4)

print("¡Archivo JSON guardado con éxito en tu carpeta!")