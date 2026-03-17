import random
import json

def generar_cliente():
    """
    Genera un diccionario con datos sintéticos aleatorios de un cliente.
    """
    nombres_posibles = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
    
    cliente = {
        "nombre": random.choice(nombres_posibles),
        "edad": random.randint(18, 65)
    }
    return cliente

# Generación del lote de datos sintéticos
base_de_datos = []
for _ in range(100):
    base_de_datos.append(generar_cliente())

# Exportación a formato JSON para consumo del modelo
with open("clientes_sinteticos.json", "w") as archivo:
    json.dump(base_de_datos, archivo, indent=4)

print("Lote de 100 clientes sintéticos generado y exportado exitosamente.")