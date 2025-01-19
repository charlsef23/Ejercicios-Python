# EJERCICIO: Buscar un objeto en la lista
# Busca un estudiante por su nombre en la lista
# y muestra su información.

estudiantes = [
    {"nombre": "Ana", "edad": 20, "clase": "A"},
    {"nombre": "Pedro", "edad": 21, "clase": "B"},
    {"nombre": "Carlos", "edad": 19, "clase": "C"}
    ]

nombre_estudiante = str(input("INGRESE EL NOMBRE DEL ESTUDIANTE: "))
encontrado = False

for estudiante in estudiantes:
    if estudiante["nombre"].lower() == nombre_estudiante.lower():
        print(f"Estudiante encontrado.")
        encontrado = True
        break

if not encontrado:
    print("Estudiante no encontrado.")