import random
import json

def generar_cliente():
    """
    Genera un diccionario con datos sintéticos aleatorios aplicando reglas de negocio.
    """
    nombres_posibles = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Matias", "Sofi", "Bruna"]
    profesiones_activas = ["Desarrollador IA", "Médica", "Docente", "Comerciante", "Contador"]
    
    edad = random.randint(18, 75)
    
    # Reglas de Lógica de Negocio
    esta_jubilado = edad >= 65
    
    if esta_jubilado:
        profesion = "Jubilado"
        salario = random.randint(300000, 600000) # Rango de jubilación
    else:
        profesion = random.choice(profesiones_activas)
        salario = random.randint(800000, 2500000) # Rango de trabajador activo
        
    cliente = {
        "nombre": random.choice(nombres_posibles),
        "edad": edad,
        "profesion": profesion,
        "salario_ars": salario,
        "esta_jubilado": esta_jubilado
    }
    return cliente

# Generación del lote usando List Comprehension
base_de_datos = [generar_cliente() for _ in range(100)]

# Exportación a formato JSON
with open("clientes_sinteticos.json", "w", encoding="utf-8") as archivo:
    json.dump(base_de_datos, archivo, indent=4, ensure_ascii=False)

print("Lote de 100 clientes con lógica de negocio generado exitosamente.")