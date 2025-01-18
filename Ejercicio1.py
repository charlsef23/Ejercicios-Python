# EJERCICIO:
# Crea una lista de diccionarios en python
# Y muestrala por pantalla

estudiantes = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Pepe", "edad": 21},
    {"nombre": "Juan", "edad": 19},
    {"nombre": "Maria", "edad": 18},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Carlos", "edad": 19},
    {"nombre": "Daniel", "edad": 21},
    {"nombre": "Jose", "edad": 20},
]
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']} Edad: {estudiante['edad']}")