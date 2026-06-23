# Generador de Datos Sintéticos

Proyecto de aprendizaje desarrollado en Python para generar perfiles ficticios y exportarlos en formato JSON.

## Objetivo

El objetivo de este proyecto es practicar fundamentos de programación en Python aplicados a la generación de datos estructurados.

El programa crea una lista de clientes sintéticos con información como nombre, edad, profesión, salario y estado jubilatorio.

## Tecnologías usadas

* Python
* JSON
* Git
* GitHub

## Funcionalidades actuales

* Genera clientes sintéticos de forma aleatoria.
* Aplica una regla simple de negocio para detectar si una persona está jubilada.
* Exporta los datos generados a un archivo JSON.
* Usa listas y diccionarios para estructurar la información.

## Archivos del proyecto

* `generador.py`: contiene la lógica principal para generar los clientes.
* `clientes_sinteticos.json`: archivo generado con datos de ejemplo.

## Cómo ejecutar el proyecto

```bash
python generador.py
```

## Ejemplo de dato generado

```json
{
  "nombre": "Carlos",
  "edad": 33,
  "profesion": "Docente",
  "salario_ars": 1009903,
  "esta_jubilado": false
}
```

## Qué aprendí

* Crear funciones en Python.
* Trabajar con listas y diccionarios.
* Usar condiciones para aplicar reglas de negocio.
* Exportar información en formato JSON.
* Documentar un proyecto en GitHub.

## Próximas mejoras

* Permitir elegir la cantidad de clientes desde la terminal.
* Separar el código en más funciones.
* Agregar exportación a CSV.
* Mejorar la estructura del proyecto.
* Agregar pruebas simples.
